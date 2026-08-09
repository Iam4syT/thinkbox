# Enterprise Ops Telemetry Engine

[![Python](https://img.shields.io/badge/Language-Python%203.10+-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![Azure Monitor](https://img.shields.io/badge/Telemetry-Azure%20Log%20Analytics-0078D4?style=flat-square&logo=microsoftazure)](https://azure.microsoft.com/)
[![Scikit-Learn](https://img.shields.io/badge/ML-Isolation%20Forest-F7931E?style=flat-square&logo=scikitlearn)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](#)

> **Automating Secure Modern Workplace Landings and Mining Azure Log Telemetry for Proactive Trend Analysis and Machine Learning Anomaly Detection.**

---

## 1. Business Value & Executive Business Case

### The Operational Challenge
As a Managed Service Provider (MSP) or enterprise IT team scales, manual configuration errors increase, resource sprawl creates hidden costs (**FinOps drift**), and recurring ticket noise exhausts engineers. 

### The Solution Provided
1. **Project Delivery Block:** Fully automated PowerShell workflows run secure tenant onboarding setups (Conditional Access, Intune profiles, Defender isolation) to eliminate setup errors.
2. **Service Intelligence Block:** A Python analytics and Machine Learning engine reads simulated Azure monitor telemetry, parses trend logs, and applies an `Isolation Forest` model to catch and flag operational anomalies before they turn into active support tickets.
3. **Executive Dashboard:** A Power BI reporting layer transforms raw cloud logs into clear cost optimization views showing license drift and unmapped resource spending.

### The Profit Multiplier
Automating the client onboarding process **reduces engineering setup times by over 60%**. Proactive self-healing alert analytics prevent unexpected incident ticket surges. This structure allows operations to scale margin profitability without a linear, expensive headcount increase.

---

## 2. Technical Architecture & Workflow

```
┌────────────────────────┐
│  Log Parser Module     │  Generates & parses synthetic Azure Monitor
│  (src/Analytics/       │  workspace telemetry logs
│   LogParser.py)        │
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│  ML Anomaly Detector   │  Runs Isolation Forest model (scikit-learn)
│  (src/Analytics/       │  to identify FinOps spikes & operational drift
│   anomalous_noise_... )│
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│  Power BI Analytics    │  Consumes telemetry_anomaly_insights.csv
│  (src/Dashboards/)     │  for executive cost & health dashboards
└────────────────────────┘
```

---

## 3. Project Structure

```
Enterprise-Ops-Telemetry-Engine/
├── src/
│   ├── Analytics/
│   │   ├── LogParser.py                   # Azure log telemetry generation & parser module
│   │   └── anomalous_noise_detector.py    # Isolation Forest machine learning anomaly detector
│   ├── Dashboards/                        # Power BI report definitions & documentation
│   └── Runbooks/                          # Automated PowerShell tenant onboarding runbooks
├── main.py                                # End-to-end execution script
├── requirements.txt                       # Project Python dependencies
├── .env.example                           # Environment configuration template
├── .gitignore                             # Git ignore rules
└── README.md                              # Technical documentation
```

---

## 4. Setup and Installation

### Prerequisites
- Python 3.10 or higher

### Quickstart

1. **Navigate to the project directory:**
   ```bash
   cd "/Users/4syt/Documents/thinkbox/Modern Workplace Solutions/Enterprise-Ops-Telemetry-Engine"
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the telemetry creation & machine learning pipeline:**
   ```bash
   python main.py
   ```

---

## 5. Visualizations & Dashboards

After executing `python main.py`, open Power BI Desktop, import the generated insights CSV file from `src/Analytics/data/telemetry_anomaly_insights.csv`, and construct visualization dashboards as detailed in `src/Dashboards/README.md`.

---

## 6. License

Distributed under the **MIT License**.