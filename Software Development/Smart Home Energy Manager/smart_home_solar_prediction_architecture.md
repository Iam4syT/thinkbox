# Smart Home Energy Manager — 30-Min Solar Drop Prediction Engine Architecture

[![Python](https://img.shields.io/badge/Language-Python%203.9+-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![Semantic Kernel](https://img.shields.io/badge/AI-Semantic%20Kernel%20%7C%20OpenAI-412991?style=flat-square&logo=openai)](https://github.com/microsoft/semantic-kernel)
[![Architecture](https://img.shields.io/badge/Pattern-SOLID%20%7C%20Strategy%20%7C%20Observer-blue?style=flat-square)](#)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](#)

> **Architectural design blueprint, component flow, and integration guide for the 30-Minute Ahead Solar Irradiance (GHI) and Rooftop Photovoltaic (PV) Output Drop Prediction Engine in Smart Home Energy Management Systems.**

---

## 1. Executive Summary & Home Energy Value

Residential rooftop solar installations face rapid output fluctuations caused by approaching cloud fronts, shading, and micro-climatic weather shifts. Without advance warning, a sudden 50% drop in solar generation causes the home to automatically draw expensive peak-tariff power from the grid or deplete home storage batteries prematurely.

The **30-Minute Ahead Solar Irradiance Drop Prediction Engine** integrates into the **Smart Home Energy Manager** to:
1. **Forecast Rooftop PV Output (kW)** 30 minutes in advance based on GHI data ($W/m^2$) and cloud motion trends.
2. **Issue Proactive Load-Shedding Alerts** 30 minutes before solar output drops.
3. **Trigger Automated AI Mitigation**: Interacts with the Semantic Kernel AI assistant to provide personalized battery pre-charging, appliance deferral (EV chargers, HVAC, dryers), and peak-rate avoidance advice.

---

## 2. High-Level Data & Component Flow

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. HOME SENSOR & WEATHER INGESTION LAYER                               │
│    • Rooftop Pyranometer / Inverter Telemetry (GHI W/m²)              │
│    • OpenWeatherMap Satellite Cloud Cover / Forecast API               │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Real-Time GHI & Cloud Trend Telemetry
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 2. PREDICTIVE INTELLIGENCE LAYER (Where ML / Physics Model Resides)    │
│                                                                        │
│    ┌──────────────────────────────────────────────────────────────┐    │
│    │ GhiPredictionStrategy (Abstract Base Class / SOLID OCP & DIP)│    │
│    ├──────────────────────────────────────────────────────────────┤    │
│    │  ├── PhysicalGhiPredictionStrategy (Clear-sky baseline)      │    │
│    │  └── MlGhiPredictionStrategy / OnnxGhiModel  <-- [YOUR MODEL]│    │
│    └──────────────────────────────┬───────────────────────────────┘    │
│                                   │                                    │
│  Calculates: P_PV_30min = Area(m²) × Efficiency × GHI_30min × (1-Loss) │
│  Outputs:    SolarForecast Dataclass (30-min kW, % drop, warning)      │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Forecast & Drop Warning Signal
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 3. EVENT PUBLISHER / OBSERVER LAYER (Observer Pattern / SOLID ISP)     │
│    • PredictionObserver (ABC) -> ConsolePredictionObserver             │
│    • Dispatches 30-min warning alert to Terminal CLI & Smart Home Hubs │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Warning Event Trigger
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 4. AI MITIGATION & HOME AUTOMATION ORCHESTRATOR                        │
│    • Semantic Kernel AI Consultant (ask_kernel_for_solar_mitigation)   │
│    • Pre-charges Home Battery Storage (BESS) at current peak solar     │
│    • Defers heavy appliance cycles (EV Charger, Heat Pump, Dryer)      │
│    • Arms automated grid backup transition before peak tariff rates    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. SOLID Principles & OOP Architecture Matrix

| Principle / Pattern | Python Implementation | Technical & Functional Benefit |
|---|---|---|
| **Single Responsibility (SRP)** | `SolarForecast` dataclass holds prediction values; `SolarIntelligenceEngine` manages orchestration. | Separates data representation from notification and calculation logic. |
| **Open/Closed (OCP)** | `GhiPredictionStrategy` (ABC) allows plugging in ML models (XGBoost / PyTorch / ONNX) or physics models. | Extend prediction algorithms without modifying existing home energy manager code. |
| **Liskov Substitution (LSP)** | Subclasses (`PhysicalGhiPredictionStrategy`, `MlGhiPredictionStrategy`) cleanly implement `predict_30min_ahead`. | Orchestration engine operates seamlessly regardless of underlying ML framework. |
| **Interface Segregation (ISP)** | `PredictionObserver` interface is strictly focused on prediction events. | CLI, smart home MQTT brokers, and mobile push notifications implement only required callbacks. |
| **Dependency Inversion (DIP)** | `SolarIntelligenceEngine` depends on `GhiPredictionStrategy` ABC, not concrete implementations. | Decouples core energy management from specific predictive modeling libraries. |
| **Observer Pattern** | `PredictionObserver` & `ConsolePredictionObserver` subscribe to prediction events. | Decouples alert display from numerical prediction computation. |

---

## 4. Codebase Architecture & File Mapping

- **[`src/solar_prediction.py`](file:///Users/4syt/Documents/thinkbox/Software%20Development/Smart%20Home%20Energy%20Manager/src/solar_prediction.py)**:
  - `SolarForecast`: Dataclass storing current GHI, 30-min forecast GHI, current/future PV kW output, drop percentage, and warning flags.
  - `GhiPredictionStrategy`: Abstract Base Class (Strategy pattern).
  - `PhysicalGhiPredictionStrategy`: Physical prediction model calculating $P_{\text{PV}} = \text{Area} \times \text{Efficiency} \times \text{GHI} \times (1 - \text{Loss})$.
  - `PredictionObserver` & `ConsolePredictionObserver`: Observer pattern interface and terminal subscriber.
  - `SolarIntelligenceEngine`: Engine orchestrator.

- **[`src/energy_manager.py`](file:///Users/4syt/Documents/thinkbox/Software%20Development/Smart%20Home%20Energy%20Manager/src/energy_manager.py)**:
  - `ask_kernel_for_solar_mitigation`: Interacts with Semantic Kernel / OpenAI API to provide 3-step proactive home battery and load-shedding recommendations when a drop alert is triggered.

- **[`src/main.py`](file:///Users/4syt/Documents/thinkbox/Software%20Development/Smart%20Home%20Energy%20Manager/src/main.py)**:
  - Added Interactive CLI Menu **Option 6**: `Predict 30-Min Ahead Solar Irradiance Drop & PV Output`.

- **[`demo_solar_prediction.py`](file:///Users/4syt/Documents/thinkbox/Software%20Development/Smart%20Home%20Energy%20Manager/demo_solar_prediction.py)**:
  - Standalone multi-scenario test runner demonstrating clear solar conditions, approaching cloud fronts, and severe storm drop warnings.

---

## 5. How to Run the Demo & Interactive CLI

### Standalone Automated Demo
Run the multi-scenario demonstration script:
```bash
cd "/Users/4syt/Documents/thinkbox/Software Development/Smart Home Energy Manager"
python3 demo_solar_prediction.py
```

### Interactive CLI Menu
Launch the main application and select **Option 6**:
```bash
cd "/Users/4syt/Documents/thinkbox/Software Development/Smart Home Energy Manager"
python3 src/main.py
```

---

## 6. License

Distributed under the **MIT License**. Part of the Thinkbox Software Development portfolio.
