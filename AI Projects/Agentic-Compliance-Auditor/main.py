"""
Agentic Compliance Auditor — main.py
=====================================
A FastAPI backend that acts as an automated AI compliance officer.
Evaluates draft customer responses against corporate policies using
either standard OpenAI or Azure OpenAI (configured via .env).

Lab Architecture:
  [Client] → FastAPI → Policy Retrieval + AI Evaluation → Structured Log → JSON Response
"""

import os
import time
import json
import logging
from typing import List, Dict

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from openai import OpenAI, AzureOpenAI
from dotenv import load_dotenv

# ─────────────────────────────────────────────────────────────────────────────
# BOOTSTRAP
# ─────────────────────────────────────────────────────────────────────────────

load_dotenv()

app = FastAPI(
    title="Agentic Compliance Auditor",
    description=(
        "An automated AI compliance officer that evaluates draft customer "
        "responses against corporate policies and returns a strict APPROVED / "
        "REJECTED verdict with full audit trail logging."
    ),
    version="1.0.0",
)

# Allow browser-based testing tools (Swagger UI, Postman web, etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Structured Logging to the logs/ directory
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/compliance_audit.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

# Mirror audit logs to the console so you can watch them live
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
logging.getLogger("").addHandler(console)

# ─────────────────────────────────────────────────────────────────────────────
# PHASE 1 — PYDANTIC SCHEMAS
# ─────────────────────────────────────────────────────────────────────────────

class AuditRequest(BaseModel):
    """Incoming payload: the draft response to be evaluated."""
    customer_id: str = Field(..., example="CUST-9921")
    draft_response: str = Field(
        ...,
        example="We can guarantee a 50% return on investment within 3 days!",
    )


class ComplianceResult(BaseModel):
    """Structured AI output validated by Pydantic."""
    is_compliant: bool = Field(
        ..., description="True if the response passes all policies, False otherwise."
    )
    violated_policies: List[str] = Field(
        default=[],
        description="List of specific policy titles violated.",
    )
    reasoning: str = Field(
        ...,
        description="Detailed analytical breakdown of why the response passed or failed.",
    )


class AuditResponse(BaseModel):
    """Full response returned to the client."""
    customer_id: str
    status: str                     # "APPROVED" or "REJECTED"
    latency_seconds: float
    audit_details: ComplianceResult


# ─────────────────────────────────────────────────────────────────────────────
# PHASE 2 — CORPORATE POLICY KNOWLEDGE BASE
# ─────────────────────────────────────────────────────────────────────────────
# In production this would come from a database / RAG vector store.
# Here we simulate it as a structured static dataset.

CORPORATE_POLICIES: List[Dict[str, str]] = [
    {
        "id": "POL-001",
        "title": "No Financial Guarantees",
        "rule": (
            "Staff and automated systems must never guarantee investment returns, "
            "specific percentage gains, or time-bound financial profits to customers."
        ),
    },
    {
        "id": "POL-002",
        "title": "Data Privacy & PII",
        "rule": (
            "Never share or confirm specific backend database keys, system passwords, "
            "or unmasked Social Security numbers / National IDs in customer communications."
        ),
    },
    {
        "id": "POL-003",
        "title": "Professional Tone",
        "rule": (
            "All responses must be respectful, helpful, and objective. Avoid using "
            "overly emotional language, slang, or aggressive punctuation."
        ),
    },
    {
        "id": "POL-004",
        "title": "No Misleading Claims",
        "rule": (
            "Responses must not contain factually incorrect statements, "
            "unverified statistics, or claims that could be interpreted as "
            "misleading or deceptive by the customer."
        ),
    },
    {
        "id": "POL-005",
        "title": "Regulatory Compliance",
        "rule": (
            "All communications must align with applicable financial regulations "
            "(e.g. FCA, SEC). Do not provide advice that constitutes unlicensed "
            "financial guidance."
        ),
    },
]


# ─────────────────────────────────────────────────────────────────────────────
# PHASE 3 — AI CLIENT FACTORY
# ─────────────────────────────────────────────────────────────────────────────

def _build_ai_client():
    """
    Return the correct OpenAI client based on AI_PROVIDER env var.
    Supports 'openai' (standard) and 'azure' (Azure OpenAI Service).
    """
    provider = os.getenv("AI_PROVIDER", "openai").lower()

    if provider == "azure":
        return AzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", ""),
            api_key=os.getenv("AZURE_OPENAI_API_KEY", ""),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01"),
        ), os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "compliance-evaluator")

    # Default: standard OpenAI
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY", "")), os.getenv("OPENAI_MODEL", "gpt-4o")


client, MODEL = _build_ai_client()

provider_label = os.getenv("AI_PROVIDER", "openai").upper()
print(f"\n✅ Compliance Auditor using {provider_label} — model: {MODEL}\n")


# ─────────────────────────────────────────────────────────────────────────────
# PHASE 3 — AGENTIC VERIFICATION LOOP & API ENDPOINT
# ─────────────────────────────────────────────────────────────────────────────

def _format_policies() -> str:
    """Render the corporate policy list into a readable prompt context block."""
    lines = []
    for p in CORPORATE_POLICIES:
        lines.append(f"- [{p['id']}] {p['title']}: {p['rule']}")
    return "\n".join(lines)


SYSTEM_PROMPT = (
    "You are an expert AI Governance and Compliance Officer working for a regulated "
    "financial institution. Your sole job is to strictly evaluate a proposed draft "
    "response against the provided corporate policies.\n\n"
    "You MUST output your analysis as a raw JSON object with exactly these keys:\n"
    "  • 'is_compliant'      — boolean (true only if ALL policies are satisfied)\n"
    "  • 'violated_policies' — array of strings (policy TITLES that were violated, empty if none)\n"
    "  • 'reasoning'         — string with a clear, concise explanation of your verdict\n\n"
    "Be strict. Even a subtle hint of a guarantee or a misleading tone is a violation."
)


@app.post("/api/v1/audit", response_model=AuditResponse, tags=["Compliance"])
async def audit_draft_response(request: AuditRequest):
    """
    **Agentic Compliance Audit Endpoint**

    Submits a draft customer response through the AI evaluation loop.
    Returns a type-safe APPROVED / REJECTED verdict with full reasoning
    and structured audit log entry.
    """
    start_time = time.time()

    # 1. Build the evaluation prompt
    policies_context = _format_policies()
    user_content = (
        f"--- CORPORATE POLICIES ---\n{policies_context}\n\n"
        f"--- DRAFT RESPONSE TO EVALUATE ---\n{request.draft_response}"
    )

    try:
        # 2. Call the AI model (zero temperature = deterministic, objective output)
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_content},
            ],
            temperature=0.0,
            response_format={"type": "json_object"},
        )

        # 3. Parse and validate AI output through Pydantic
        raw_ai_output = response.choices[0].message.content
        ai_json = json.loads(raw_ai_output)
        compliance_details = ComplianceResult(**ai_json)

    except Exception as e:
        logging.error(f"Audit FAILED for {request.customer_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Compliance Processing Failure: {str(e)}")

    # 4. Compute telemetry metrics
    latency = round(time.time() - start_time, 3)
    status_verdict = "APPROVED" if compliance_details.is_compliant else "REJECTED"
    tokens_used = response.usage.total_tokens if response.usage else 0

    # 5. Build final response payload
    final_response = AuditResponse(
        customer_id=request.customer_id,
        status=status_verdict,
        latency_seconds=latency,
        audit_details=compliance_details,
    )

    # 6. Write structured audit log entry (enterprise auditability)
    log_entry = {
        "customer_id": request.customer_id,
        "status": status_verdict,
        "latency_seconds": latency,
        "violated_policies": compliance_details.violated_policies,
        "tokens_used": tokens_used,
        "model": MODEL,
    }
    logging.info(f"AUDIT_METRICS: {json.dumps(log_entry)}")

    return final_response


# ─────────────────────────────────────────────────────────────────────────────
# UTILITY ENDPOINTS
# ─────────────────────────────────────────────────────────────────────────────

@app.get("/api/v1/health", tags=["Utility"])
async def health_check():
    """Returns the current operational status of the auditor."""
    return {
        "status": "online",
        "provider": os.getenv("AI_PROVIDER", "openai").upper(),
        "model": MODEL,
        "policies_loaded": len(CORPORATE_POLICIES),
    }


@app.get("/api/v1/policies", tags=["Utility"])
async def list_policies():
    """Returns the full list of active corporate compliance policies."""
    return {"total": len(CORPORATE_POLICIES), "policies": CORPORATE_POLICIES}
