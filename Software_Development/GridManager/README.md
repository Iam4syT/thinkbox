![Java](https://img.shields.io/badge/Java-24-orange?logo=openjdk)
![JavaFX](https://img.shields.io/badge/JavaFX-21-blue?logo=java)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success)
![Last Commit](https://img.shields.io/github/last-commit/Iam4syT/SWE7302)
![Issues](https://img.shields.io/github/issues/Iam4syT/SWE7302)

# ⚡ GridManager

**Advanced Software Development Portfolio (SWE7302)**  
A Java-based intelligent energy source management system that monitors industrial energy
demand in real time and automatically selects the most optimal power source — Solar, Wind,
Hybrid, or Grid — based on live sensor data, cost analysis, and time of day.

> Built by refactoring a legacy monolith using **SOLID principles** and core **design patterns**
> (Builder, Facade, Factory, Strategy, Singleton).

---

## 💡 Problem Statement

Modern industry needs power that never turns off. Renewables alone can't guarantee 24/7
uptime yet. GridManager bridges that gap — it maximises renewables when they're at peak,
and intelligently falls back to conventional sources only when needed. Every switching
decision is logged, costed, and reported.

---

## 🚀 Core Features

| Feature | Description |
|---------|-------------|
| 🔹 **Sensor Integration** | Ingests wind speed, solar irradiance, industrial demand, electricity cost, and time of day |
| 🔹 **Intelligent Switching** | Strategy Pattern evaluates all available sources and picks the best one |
| 🔹 **Automated Execution** | Calls `switchTo()` on the selected energy source automatically |
| 🔹 **Persistent Logging** | Every switch is saved to SQLite (`energy.db`) with timestamp and demand level |
| 🔹 **Cost Calculations** | Estimates real $ savings vs. all-Grid baseline per switch (IEA/IRENA rates) |
| 🔹 **CO₂ Reporting** | Calculates kg of CO₂ avoided per switch vs. Grid Electricity baseline |
| 🔹 **Daily Reports** | Filters today's switch history and prints source breakdown + recommendations |
| 🔹 **Multi-site Support** | Run multiple campus configs in one session |
| 🔹 **JavaFX Dashboard** | GUI with live sliders, System.out redirection, and progress bar |
| 🔹 **CLI Entry Point** | `GridSystem.java` for terminal-based operation |

---

## 🏗️ Architecture & Design Patterns

```
GridSystem.main()
    └── GridManagerConfig (Builder Pattern)
            └── GridSystemFacade (Facade Pattern)
                    └── GridSystemManager (Orchestrator)
                            ├── EnergySourceFactory (Factory Pattern)
                            │       ├── HybridStrategy  ─┐
                            │       ├── SolarStrategy    ├── (Strategy Pattern)
                            │       ├── WindStrategy    ─┘
                            │       └── GridEnergySource (fallback)
                            ├── GridReportDAO (Singleton)
                            │       └── GridDbHandler (Singleton → SQLite)
                            └── UsageReport (cost + CO₂ calculations)
```

### Decision Logic

| Condition | Source Selected |
|-----------|----------------|
| `solar ≥ wind` AND `solar ≥ demand` AND `wind ≥ demand` | **Hybrid** |
| `solar > wind` AND `solar > demand` | **Solar** |
| `wind > solar` AND `wind > demand` | **Wind** |
| None of the above | **Grid Electricity** (fallback) |

---

## 📊 Cost & CO₂ Model

All values are percentages (0–100) normalised against historical maxima.
Demand% maps to `demand × 10 kWh` against a 1,000 kWh baseline.

| Source | Cost ($/kWh) | CO₂ (kg/kWh) |
|--------|-------------|--------------|
| Grid Electricity | $0.10 | 0.450 |
| Solar Energy | $0.05 | 0.020 |
| Wind Energy | $0.04 | 0.010 |
| Hybrid | $0.045 | 0.015 |

*Sources: IEA World Energy Outlook 2024, IRENA Renewable Power Generation Costs 2023.*

---

## 📂 Project Structure

```
GridManager/
├── src/
│   ├── main/java/
│   │   ├── GridManagerCore/
│   │   │   ├── config/
│   │   │   │   └── GridManagerConfig.java      ← Builder pattern — immutable config
│   │   │   ├── database/
│   │   │   │   ├── GridDbHandler.java           ← Singleton SQLite connection
│   │   │   │   ├── GridReportDAO.java           ← Singleton DAO (INSERT / SELECT)
│   │   │   │   └── SwitchReport.java            ← Data model + cost/CO₂ helpers
│   │   │   ├── facade/
│   │   │   │   └── GridSystemFacade.java        ← Facade: single initialize() call
│   │   │   ├── factory/
│   │   │   │   └── EnergySourceFactory.java     ← Factory: creates best EnergySource
│   │   │   ├── log/
│   │   │   │   └── UsageReport.java             ← Prints daily report with calculations
│   │   │   ├── main/
│   │   │   │   └── GridSystem.java              ← CLI entry point (main method)
│   │   │   ├── sources/
│   │   │   │   ├── EnergySource.java            ← Interface (switchTo, getName)
│   │   │   │   ├── SolarEnergySource.java
│   │   │   │   ├── WindEnergySource.java
│   │   │   │   ├── HybridEnergySource.java
│   │   │   │   └── GridEnergySource.java        ← Fallback source
│   │   │   ├── strategy/
│   │   │   │   ├── SourceStrategy.java          ← Interface (isBest, getSource)
│   │   │   │   ├── HybridStrategy.java
│   │   │   │   ├── SolarStrategy.java
│   │   │   │   └── WindStrategy.java
│   │   │   ├── system/
│   │   │   │   └── GridSystemManager.java       ← Core orchestrator
│   │   │   └── ui/
│   │   │       └── GridManagerDashboard.java    ← JavaFX GUI dashboard
│   │   └── GridManagerLegacy/
│   │       └── GridManager.java                 ← Original monolith (preserved)
│   └── test/java/GridManagerTest/java/com/store/core/
│       ├── BuilderTest.java                     ← Tests Builder config construction
│       ├── StrategyTest.java                    ← Tests all 4 source selection scenarios
│       └── ReportTest.java                      ← Tests cost/CO₂ saving calculations
├── energy.db                                    ← SQLite database (auto-created)
├── pom.xml                                      ← Maven: Java 24, JavaFX 21, JUnit 5
├── run.sh                                       ← Shell launcher
└── README.md
```

---

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| Java | 24 | Core language |
| JavaFX | 21 | GUI dashboard |
| SQLite + JDBC | 3.45.1 | Persistent switch history |
| Maven | 3.x | Build & dependency management |
| JUnit Jupiter | 5.10 | Unit testing |
| SLF4J | 2.0.12 | Logging facade |

---

## 📦 Installation & Running

### Prerequisites
- Java 24+
- Maven 3.x

### Clone
```bash
git clone https://github.com/Iam4syT/SWE7302.git
cd GridManager
```

### Run via CLI
```bash
./run.sh
# or
mvn compile exec:java -Dexec.mainClass="GridManagerCore.main.GridSystem"
```

### Run the JavaFX Dashboard
```bash
mvn javafx:run -Djavafx.mainClass="GridManagerCore.ui.GridManagerDashboard"
```

### Run Tests
```bash
mvn test
```

---

## 📊 Sample Output

```
==== Initializing Grid System ====
====  Sensor Data at Amsterdam Campus . Time of the day : Daytime ====
 Industrial Demand : 60.0
 Wind Speed        : 50.0
 Solar Irradiance  : 70.0
 Electricity Price : 80.0
Analyzing data for choice of energy source at Amsterdam Campus
Solar is best choice for demand. Switching to Solar Energy

==== Saving Switch History at Amsterdam Campus ====
Switch data inserted successfully for Amsterdam Campus

==== Daily Switch Report for 2026-06-28 at Amsterdam Campus ====
Total Switches Made : 1
Cost Savings        :  $30.00 (vs. all-Grid baseline)
Estimated CO₂ Saved : 258.00 kg CO₂
Source Breakdown    : {Solar Energy=1}
Recommendations     : Prioritise 'Solar Energy' - most efficient source today.
====  Grid System Initialization Successful ====
```

---

## 🧪 Test Coverage

| Test Class | What it tests |
|------------|--------------|
| `BuilderTest` | Builder pattern constructs config correctly |
| `StrategyTest` | All 4 source selection scenarios + validation boundaries |
| `ReportTest` | Cost savings, CO₂ savings, zero baseline for Grid, demand scaling |

---

## 🔮 Roadmap

- [ ] Live sensor API integration (IoT / REST)
- [ ] Weather forecast API for predictive switching
- [ ] Full LCOE (Levelised Cost of Energy) implementation per the legacy formula
- [ ] Expanded JavaFX dashboard with charts and historical graphs
- [ ] REST API layer for remote monitoring

---

## 📜 License

Licensed under the **MIT License** — free to use, modify, and build upon with attribution.

---

## 👨‍💻 Author

Developed by **4syT Labs**  
🔗 [LinkedIn](https://linkedin.com/in/bunaminadams) | [GitHub](https://github.com/Iam4syT)  
🌐 [think4syt.com](https://think4syt.com) | ✉️ bunamin@think4syt.com
