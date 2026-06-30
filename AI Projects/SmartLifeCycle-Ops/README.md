# SmartLifecycle-Ops 🚄

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI Framework](https://img.shields.io/badge/FastAPI-0.110.0-green.svg)](https://fastapi.tiangolo.com)
[![Machine Learning Core](https://img.shields.io/badge/scikit--learn-1.4.1-orange.svg)](https://scikit-learn.org/)

An enterprise-grade IT Asset Management (ITAM) & Modern Workplace automation workflow architecture designed to handle identity management events, trigger automated device provisioning pipelines, and ingest telemetry monitoring logs to predict hardware failures before they disrupt operations.

---

## 1. Architectural Core Principles

This system serves as a central engine between HR/Identity vectors and live machine analytics to enable efficient, automated asset management.

### System Integration Schema
* **Zero-Touch Provisioning Core:** Listens for incoming employee system changes (onboarding/offboarding events). Based on the preferred OS platform parsed from the input schema, the system dynamically routes variables to either **Microsoft Intune / Autopilot** (Windows) or **JAMF Pro** (macOS).
* **Predictive Telemetry Core:** A trained **Random Forest Classifier** processes live engine logs containing system vitals—such as battery health degradation and operating temperatures—to forecast hardware replacement metrics before unexpected failures occur.

---

## 2. Technical Repository Breakdown

```text
SmartLifecycle-Ops/
├── app/
│   ├── __init__.py
│   ├── main.py                # Core FastAPI Engine Webhook Interface Gateway
│   └── models/
│       ├── __init__.py
│       └── train_model.py     # Random Forest Classification Machine Learning pipeline
├── data/
│   └── predictive_refresh_model.pkl  # Serialized Production Trained Model Binaries
├── requirements.txt           # Unified Manifest Packages File
└── README.md                  # Comprehensive Infrastructure Documentation
```

---

## 3. Local System Installation & Run Guide

### Prerequisite System Requirements

* **Python 3.11 or higher** installed on local host machine.
* **VS Code** with official Python extensions bundle active.

### 1. Repository Setup & Environment Provisioning

```bash
git clone https://github.com/enterprise/SmartLifecycle-Ops.git
cd SmartLifecycle-Ops

# Instantiate isolated virtual env structure
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\Activate.ps1

# Install required package artifacts
pip install -r requirements.txt
```

### 2. Execute Training Lifecycle

Run the orchestration script to generate the tracking data matrices and train the predictive algorithm asset:

```bash
python app/models/train_model.py
```

### 3. Spin Up Application Service

Launch the FastAPI development cluster infrastructure engine using the Uvicorn engine process manager:

```bash
python app/main.py
```

The active web portal dashboard documentation interface will sit at: **`http://127.0.0.1:8000/docs`**

---

## 4. Production API Interrogation Specifications

### Core Endpoint Mapping Matrix

| Verb | Routing Endpoint | Input Payload Target | Functional Objective |
| --- | --- | --- | --- |
| **GET** | `/` | *None Required* | Health Check & Operational Gateway status monitoring validation loop. |
| **POST** | `/webhook/onboard` | `EmployeeOnboardPayload` | Processes incoming employee metadata and triggers automated Intune/JAMF profiles. |
| **POST** | `/predict/refresh` | `TelemetryPayload` | Evaluates hardware diagnostics against the ML model to flag assets needing refresh. |

---

## 5. Mock Power BI Operational Dashboard Blueprint

This operational data layout maps directly to enterprise Power BI streaming semantic models for real-time fleet analytics tracking.

```text
=======================================================================================
               SMARTLIFECYCLE-OPS ENTERPRISE MODERN WORKPLACE ANALYTICS
=======================================================================================
 [ Total Hardware Fleet: 2,500 ]    [ Healthy Status: 2,120 ]   [ Refresh Required: 380 ]
---------------------------------------------------------------------------------------
  PLATFORM DISTRIBUTION ENGINE METRICS:
  ├─ Microsoft Intune (Windows 11): 62% [=======================>       ]
  └─ JAMF Pro Engine (Apple macOS): 38%  [=============>                 ]
---------------------------------------------------------------------------------------
  TOP INCIDENT TELEMETRY WARNING VECTOR ALERTS:
  1. Serial: TL-SN-9482-2026  --> FAILURE PROBABILITY: 98.4% [CRITICAL REPLACEMENT REQUIRED]
  2. Serial: TL-SN-4412-2026  --> FAILURE PROBABILITY: 91.2% [HIGH THERMAL DEGRADATION]
  3. Serial: TL-SN-0912-2026  --> FAILURE PROBABILITY: 87.9% [BATTERY END OF LIFE VALUE]
=======================================================================================
```
