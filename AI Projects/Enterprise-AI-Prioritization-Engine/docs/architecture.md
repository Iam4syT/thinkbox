# Extended Technical Documentation

## Scoring Engine Deep Dive

### Weighting Rationale

The 60/40 split between commercial impact and engineering feasibility is a deliberate consulting design choice:

- **60% Commercial Impact** — In enterprise AI initiatives, strategic value and executive alignment are the primary drivers of project approval and budget allocation. A technically easy but commercially worthless initiative should never be prioritised.
- **40% Engineering Feasibility** — Data readiness, team skill gaps, and integration complexity are real delivery risks that cannot be ignored, but they are secondary to business value when making prioritization decisions.

This mirrors the weighting used in enterprise value-stream mapping frameworks and MoSCoW prioritization methodologies.

---

## Green AI Estimator Deep Dive

### Carbon Calculation Methodology

```
millions_of_tokens  = monthly_tokens ÷ 1,000,000
estimated_cost_usd  = millions_of_tokens × cost_per_million_tokens
estimated_co2_kg    = millions_of_tokens × co2_per_million_tokens
```

Carbon factors are based on average data centre Power Usage Effectiveness (PUE) metrics for Azure regions combined with regional grid carbon intensity averages. These represent approximations suitable for early-stage feasibility assessments.

For production-grade carbon accounting, integrate with the **Azure Carbon Optimization** API and **Microsoft Sustainability Manager** for organisation-specific, region-accurate emissions data.

---

## Extending the Model Registry

To add a new model tier, append to `MODEL_REGISTRY` in `core_engine/green_ai_estimator.py`:

```python
"Custom Fine-Tuned (e.g., Phi-3 Fine-Tune)": {
    "cost_per_million_tokens": 3.00,
    "co2_per_million_tokens": 0.10,
    "description": "Domain-specific fine-tuned model balancing accuracy and efficiency.",
},
```

The UI selectbox and comparison table will automatically reflect the new tier without any changes to `app.py`.

---

## Extending to a Multi-Use-Case Portfolio

The current implementation evaluates one use case at a time. To extend to a portfolio view:

1. Replace the single input panel with a `st.data_editor` table allowing multiple rows.
2. Loop `calculate_priority_score` and `estimate_green_ai_impact` over each row using `pandas.DataFrame.apply`.
3. Render an interactive scatter plot (impact vs. feasibility) using `st.plotly_chart` with each use case as a labelled data point — producing a live 2×2 bubble chart for executive presentations.

---

## Azure Live Pricing Integration

Replace the static `MODEL_REGISTRY` with a live Azure Pricing Calculator API call:

```python
import httpx

def fetch_azure_pricing(model_name: str, region: str = "eastus") -> dict:
    url = "https://prices.azure.com/api/retail/prices"
    params = {"$filter": f"serviceName eq 'Azure OpenAI' and armRegionName eq '{region}'"}
    response = httpx.get(url, params=params)
    return response.json()
```

This ensures cost projections always reflect the latest Azure rate card without manual updates.

---

## Docker Image Size Optimisation

The current Dockerfile uses `python:3.11-slim` (~130MB base). For further reduction:

- Use `python:3.11-alpine` (~50MB) — note: some pandas C-extensions require additional Alpine build flags.
- Use multi-stage builds to separate the dependency install layer from the runtime layer, minimising the final image to production code only.

```dockerfile
# Multi-stage example
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11-slim AS runtime
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```
