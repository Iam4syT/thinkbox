# Enterprise AI Prioritization Engine

[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?style=flat-square&logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Language-Python%203.9+-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED?style=flat-square&logo=docker)](https://www.docker.com/)
[![Azure](https://img.shields.io/badge/Cloud-Microsoft%20Azure-0078D4?style=flat-square&logo=microsoftazure)](https://azure.microsoft.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](#)

> **A production-ready AI consulting tool that scores enterprise AI use cases against commercial impact, engineering feasibility, and environmental sustainability — packaged for the Microsoft Azure cloud ecosystem.**

---

## 1. Real-World Business Value & Objective

Enterprise organizations often chase AI trends without a structured evaluation framework. This leads to wasted engineering budgets, misaligned initiatives, and — increasingly — unquantified carbon footprints from large model inference workloads.

This engine solves both problems simultaneously: it applies the classic **2×2 consulting prioritization matrix** to rank AI initiatives by strategic value, and layers on a **Green AI estimator** that projects monthly Azure token costs and CO2e emissions before a single line of code is committed to build.

### Key Business Benefits

- **Strategic Clarity:** Instantly classifies any AI initiative into one of four actionable quadrants — Quick Win, Strategic Initiative, Low Hanging Fruit, or Divest.
- **Financial Governance:** Projects monthly and annual Azure OpenAI token costs per use case, enabling accurate budget forecasting.
- **Sustainability Reporting:** Quantifies data centre CO2e emissions per use case — directly supporting Net-Zero commitments and Microsoft Sustainability Manager alignment.
- **Executive Communication:** Translates raw scores into plain-English consulting recommendations and colour-coded sustainability bands.

---

## 2. End-to-End Technical Architecture

```
[ User Inputs Use Case ]
          │
          ▼
[ Streamlit Web UI  (app.py) ]
          │
          ├──► [ core_engine/scoring_engine.py ]
          │         └── Weighted 2×2 Matrix Math → Priority Score + Quadrant
          │
          └──► [ core_engine/green_ai_estimator.py ]
                    └── Token × Model Rate Card → Cost (USD) + CO2e (kg)
```

### Tech Stack

| Layer | Technology |
|---|---|
| Web UI | Streamlit 1.32.0 |
| Data Handling | Pandas 2.2.1 |
| Containerisation | Docker (python:3.11-slim) |
| Cloud Target | Azure Container Apps / App Services |
| Sustainability Framework | Microsoft Sustainability Manager (extension path) |

---

## 3. Core Scoring Framework

### Priority Score Formula

```
Priority Score = (Commercial Impact × 0.6) + (Engineering Feasibility × 0.4)
```

The 60/40 weighting reflects that **strategic value drives executive buy-in**, while delivery feasibility remains a strong secondary constraint.

### 2×2 Prioritization Matrix

```
             │  Low Feasibility    │  High Feasibility   │
─────────────┼─────────────────────┼─────────────────────┤
High Impact  │ 🎯 Strategic Init.  │ ⚡ Quick Win         │
Low Impact   │ ⚠️  Divest          │ 🍎 Low Hanging Fruit │
```

The quadrant threshold is **65/100** on both axes.

---

## 4. Green AI Model Registry

| Model Tier | Cost / 1M Tokens | CO2e / 1M Tokens | Best For |
|---|---|---|---|
| Lightweight (GPT-3.5 / Phi-3) | $1.50 | 0.05 kg | High-volume, lower-complexity tasks |
| Heavyweight (GPT-4o) | $15.00 | 0.45 kg | Complex reasoning, lower volume |

> Pricing approximated from public Azure OpenAI rate cards. Carbon metrics based on standard regional data centre emission averages.

### Sustainability Rating Bands

| CO2e / Month | Rating |
|---|---|
| < 0.5 kg | 🟢 Excellent — Aligns with Net-Zero targets |
| 0.5 – 2.0 kg | 🟡 Moderate — Review against sustainability roadmap |
| 2.0 – 5.0 kg | 🟠 High — Carbon offset strategy recommended |
| > 5.0 kg | 🔴 Critical — Executive sustainability review required |

---

## 5. Quick Start

### Prerequisites
- Python 3.9+
- (Optional) Docker Desktop for containerised deployment

### Step 1 — Navigate to Project
```bash
cd "AI Projects/Enterprise-AI-Prioritization-Engine"
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

### Step 4 — Launch the Application
```bash
streamlit run app.py
```

Open your browser at: **http://localhost:8501**

---

## 6. Docker Deployment

### Build the Container
```bash
docker build -t enterprise-ai-engine:latest .
```

### Run Locally in Container
```bash
docker run -p 8501:8501 enterprise-ai-engine:latest
```

Open: **http://localhost:8501**

---

## 7. Enterprise Blueprint: Microsoft Azure Deployment

### Step-by-Step Cloud Promotion

**1. Azure Container Registry (ACR)**
```bash
# Create registry and push image
az acr create --name acraiengine --resource-group rg-ai-engine --sku Basic
az acr login --name acraiengine
docker tag enterprise-ai-engine:latest acraiengine.azurecr.io/enterprise-ai-engine:latest
docker push acraiengine.azurecr.io/enterprise-ai-engine:latest
```

**2. Azure Container Apps** *(Serverless — scales to zero)*
```bash
az containerapp create \
  --name enterprise-ai-engine \
  --resource-group rg-ai-engine \
  --image acraiengine.azurecr.io/enterprise-ai-engine:latest \
  --target-port 8501 \
  --ingress external
```

**3. Azure Monitor**
Connect application logs to Azure Monitor for real-time usage and performance telemetry.

**4. Microsoft Sustainability Manager**
Feed the `estimated_co2` values from the Green AI Estimator directly into Microsoft Sustainability Manager to build an AI-specific carbon emissions report for executive stakeholders.

---

## 8. Project Structure

```
Enterprise-AI-Prioritization-Engine/
├── app.py                          # Streamlit UI — main entry point
├── requirements.txt                # Pinned Python dependencies
├── Dockerfile                      # Container build blueprint
├── .dockerignore                   # Docker build exclusions
├── .gitignore                      # Git exclusion rules
├── README.md                       # This file
├── core_engine/
│   ├── __init__.py                 # Package exports
│   ├── scoring_engine.py           # 2×2 matrix priority scoring logic
│   └── green_ai_estimator.py      # Cost & carbon estimation engine
└── docs/
    └── architecture.md             # Extended technical documentation
```

---

*Built as a production-ready AI consulting tool. Designed to extend with live Azure Pricing API integration, multi-use-case portfolio comparison, and Azure Monitor telemetry streaming.*
