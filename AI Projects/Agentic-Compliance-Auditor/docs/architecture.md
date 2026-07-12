# Extended Technical Documentation

## Architecture Deep Dive

### Agentic Review Loop

The core of the system is the agentic evaluation loop inside `POST /api/v1/audit`:

1. **Policy Retrieval** — The `CORPORATE_POLICIES` dataset is formatted into a structured prompt block, simulating a RAG-style knowledge retrieval step.
2. **Deterministic AI Evaluation** — The LLM is called with `temperature=0.0`, ensuring objective, reproducible verdicts with zero creative variance.
3. **Structured JSON Output** — The system prompt instructs the model to respond strictly in JSON matching the `ComplianceResult` schema.
4. **Pydantic Validation** — The AI JSON output is parsed through Pydantic, guaranteeing type safety before the response is returned.
5. **Telemetry Logging** — Latency, token usage, model ID, verdict, and violated policies are logged in a single structured JSON entry.

### Provider Factory Pattern

The `_build_ai_client()` function implements a simple factory pattern, constructing either a standard `OpenAI` or `AzureOpenAI` client based on the `AI_PROVIDER` environment variable. This means the same codebase runs locally with OpenAI and in Azure with zero code changes — only a `.env` swap.

---

## Extending the Policy Knowledge Base

To add new policies, append to the `CORPORATE_POLICIES` list in `main.py`:

```python
{
    "id": "POL-006",
    "title": "Cookie & Consent Compliance",
    "rule": "All digital communications must include appropriate consent language where personal data processing is involved, in line with GDPR Article 7."
}
```

---

## Scaling to Production RAG Architecture

In production, replace the static `CORPORATE_POLICIES` list with a vector database retrieval step:

```
[Audit Request]
      │
      ▼
[Embed draft_response via text-embedding-3-small]
      │
      ▼
[Vector Search → Azure AI Search / Pinecone]
      │  (Returns top-k relevant policies)
      ▼
[Build dynamic prompt with retrieved policies]
      │
      ▼
[LLM Evaluation → Structured verdict]
```

This RAG pattern supports thousands of policies without prompt size limitations.

---

## Token Usage & Cost Estimates

Based on observed token usage at `gpt-4o` pricing:

| Scenario | Avg Tokens | Approx Cost (per 1000 audits) |
|---|---|---|
| Short draft (~50 words) | ~420 tokens | ~$1.26 |
| Medium draft (~150 words) | ~600 tokens | ~$1.80 |
| Long draft (~500 words) | ~900 tokens | ~$2.70 |

*Pricing based on gpt-4o at $0.003/1K tokens (input+output blended estimate).*
