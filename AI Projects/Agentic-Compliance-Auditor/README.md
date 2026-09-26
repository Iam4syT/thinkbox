# Agentic Compliance Auditor Agent

[![FastAPI](https://img.shields.io/badge/Framework-FastAPI-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![OpenAI](https://img.shields.io/badge/AI-OpenAI%20%7C%20Azure%20OpenAI-412991?style=flat-square&logo=openai)](https://platform.openai.com/)
[![Python](https://img.shields.io/badge/Language-Python%203.9+-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](#)

> **An automated AI compliance officer backend that evaluates draft customer responses against enterprise corporate policies in real time — returning a strict APPROVED / REJECTED verdict with a full structured audit trail.**

---

## 1. Real-World Business Value & Objective

Large regulated organizations — banks, insurers, healthcare providers — face a critical blocker when adopting Generative AI for customer communications: **the risk of data leaks, hallucinations, and policy violations**. A single non-compliant AI-generated email can trigger regulatory fines, reputational damage, or legal liability.

This project solves that by acting as a lightweight **automated guardrail**: a backend compliance layer that intercepts every AI-generated draft before it reaches the customer, evaluates it against corporate rules using a live LLM call, and returns a typed, auditable verdict.

### Key Business Benefits

- **Risk Mitigation:** Catches financial guarantee violations, PII leaks, misleading claims, and unprofessional tone before any content is sent.
- **Regulatory Alignment:** Enforces FCA/SEC-aligned policies through structured, deterministic zero-temperature AI evaluation.
- **Enterprise Auditability:** Every audit decision is logged to a timestamped structured file — providing a tamper-resistant compliance trail.
- **Provider Flexibility:** Supports both standard OpenAI and Azure OpenAI via a single `.env` toggle — deployable in any cloud posture.

---

## 2. End-to-End Technical Architecture

```
[Client / Thunder Client / Swagger UI]
          │  POST /api/v1/audit  (draft_response)
          ▼
┌─────────────────────────────────────────────────────────┐
│  FastAPI Application  (main.py)                         │
│                                                         │
│  1. Pydantic Schema Validation (AuditRequest)           │
│  2. Agentic Review Loop                                 │
│     ├──► Load Corporate Policy Knowledge Base           │
│     └──► AI Evaluation Call (OpenAI / Azure OpenAI)     │
│             └── temperature=0.0  →  JSON response       │
│  3. Pydantic Output Validation (ComplianceResult)       │
│  4. Structured Log Entry  →  logs/compliance_audit.log  │
│  5. Return Type-Safe AuditResponse (APPROVED/REJECTED)  │
└─────────────────────────────────────────────────────────┘
```

### Tech Stack

| Layer | Technology |
|---|---|
| API Framework | FastAPI + Uvicorn |
| Schema Validation | Pydantic v2 |
| AI Provider | OpenAI `gpt-4o` / Azure OpenAI |
| Configuration | python-dotenv |
| Logging | Python `logging` → structured JSON entries |

---

## 3. Corporate Policy Knowledge Base

The auditor evaluates every draft against **5 enterprise compliance policies**:

| ID | Policy Title | Description |
|---|---|---|
| POL-001 | No Financial Guarantees | Prohibits guaranteeing investment returns or profit timelines |
| POL-002 | Data Privacy & PII | Prevents exposure of PII, passwords, SSNs, or database keys |
| POL-003 | Professional Tone | Enforces respectful, objective language — no slang or aggression |
| POL-004 | No Misleading Claims | Blocks factually incorrect or statistically unverified statements |
| POL-005 | Regulatory Compliance | Ensures alignment with FCA/SEC — no unlicensed financial guidance |

> In production, this dataset would be sourced from a database or a RAG vector store.

---

## 4. Quick Start

### Prerequisites
- Python 3.9+
- An OpenAI API key (or Azure OpenAI deployment)

### Step 1 — Clone & Navigate
```bash
cd "AI Projects/Agentic-Compliance-Auditor"
```

### Step 2 — Create Virtual Environment
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.\venv\Scripts\activate
```

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Configure Environment
```bash
cp .env.example .env
# Edit .env — add your OPENAI_API_KEY and set AI_PROVIDER
```

### Step 5 — Run the Server
```bash
uvicorn main:app --reload --reload-exclude venv --port 8000
```

Server is live at: **http://127.0.0.1:8000**

---

## 5. API Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/health` | Returns operational status, provider, model, and policy count |
| `GET` | `/api/v1/policies` | Returns all active corporate compliance policies |
| `POST` | `/api/v1/audit` | Submits a draft for AI compliance evaluation |

### Interactive Docs
FastAPI auto-generates full interactive documentation:
```
http://127.0.0.1:8000/docs
```

### Example: Audit Request
```json
POST /api/v1/audit
{
  "customer_id": "CUST-0012",
  "draft_response": "We can guarantee a 50% return on investment within 3 days!"
}
```

### Example: REJECTED Response
```json
{
  "customer_id": "CUST-0012",
  "status": "REJECTED",
  "latency_seconds": 2.17,
  "audit_details": {
    "is_compliant": false,
    "violated_policies": ["No Financial Guarantees", "Professional Tone"],
    "reasoning": "The draft violates POL-001 by guaranteeing a specific return..."
  }
}
```

### Example: APPROVED Response
```json
{
  "customer_id": "CUST-0013",
  "status": "APPROVED",
  "latency_seconds": 1.58,
  "audit_details": {
    "is_compliant": true,
    "violated_policies": [],
    "reasoning": "The draft complies with all 5 corporate policies..."
  }
}
```

---

## 6. Audit Trail Logging

Every audit decision is written to `logs/compliance_audit.log` in structured JSON format:

```
2026-07-10 07:55:32 | INFO | AUDIT_METRICS: {"customer_id": "CUST-0012", "status": "REJECTED", "latency_seconds": 2.17, "violated_policies": ["No Financial Guarantees"], "tokens_used": 482, "model": "gpt-4o"}
2026-07-10 07:55:42 | INFO | AUDIT_METRICS: {"customer_id": "CUST-0013", "status": "APPROVED", "latency_seconds": 1.584, "violated_policies": [], "tokens_used": 472, "model": "gpt-4o"}
```

---

## 7. Azure Deployment Blueprint

To promote from local to enterprise production:

1. **Source Control** — Push to Azure DevOps or GitHub (`.env` is git-ignored).
2. **Compute** — Deploy to an **Azure App Service** (Python 3.10+ runtime).
3. **Secrets** — Add `.env` values to the App Service **Environment Variables** blade — never in source code.
4. **Switch Provider** — Set `AI_PROVIDER=azure` and provide Azure OpenAI credentials.
5. **CI/CD** — Configure GitHub Actions or Azure DevOps pipeline to deploy on push.
6. **Log Persistence** — Stream `compliance_audit.log` to **Azure Log Analytics Workspace** via the `azure-monitor-opentelemetry` exporter for a permanent, tamper-proof audit trail.

---

## 8. Project Structure

```
Agentic-Compliance-Auditor/
├── main.py                   # FastAPI application — entry point
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variable template (safe to commit)
├── .env                      # Local secrets — git-ignored
├── .gitignore                # Git exclusion rules
├── README.md                 # This file
├── logs/
│   └── compliance_audit.log  # Structured audit trail (auto-generated)
└── docs/
    └── architecture.md       # Extended technical documentation
```

---

*Built as a foundational piece of enterprise AI infrastructure. Designed to be extended with RAG policy retrieval, multi-tenant support, and Azure Monitor integration.*
