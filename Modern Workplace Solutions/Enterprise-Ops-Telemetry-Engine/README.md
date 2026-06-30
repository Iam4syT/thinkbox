# Enterprise-Ops-Telemetry-Engine 🚀

**Tagline:** Automating Secure Modern Workplace Landings and Mining Azure Log Telemetry for Proactive Trend Analysis.

---

## 💼 Executive Business Case

### The Operational Challenge
As a Managed Service Provider (MSP) scales, manual configuration errors increase, resource sprawl creates hidden costs (**FinOps drift**), and recurring ticket noise exhausts engineers. 

### The Solution Provided
1. **Project Delivery Block:** Fully automated PowerShell workflows run secure tenant onboarding setups (Conditional Access, Intune profiles, Defender isolation) to eliminate setup errors.
2. **Service Intelligence Block:** A Python analytics and Machine Learning engine reads simulated Azure monitor telemetry, parses trend logs, and applies an `Isolation Forest` model to catch and flag operational anomalies before they turn into active support tickets.
3. **Executive Dashboard:** A Power BI reporting layer transforms raw cloud logs into clear cost optimization views showing license drift and unmapped resource spending.

### The Profit Multiplier
Automating the client onboarding process **reduces engineering setup times by over 60%**. Proactive self-healing alert analytics prevent unexpected incident ticket surges. This structure allows operations to scale margin profitability without a linear, expensive headcount increase.

---

## 🚀 How to Run the Lab Engine

1. **Clone the project repository:**
   ```bash
   git clone https://github.com/Iam4syT/thinkbox.git
   cd "Modern Workplace Solutions/Enterprise-Ops-Telemetry-Engine"
   ```

2. **Run the telemetry creation and data science processing models:**
   ```bash
   pip install pandas scikit-learn
   python src/Analytics/LogParser.py
   python src/Analytics/anomalous_noise_detector.py
   ```

3. **Open Visualizations:** 
   Open Power BI Desktop, import the generated data from `src/Analytics/data/telemetry_anomaly_insights.csv`, and build the visualization dashboard as outlined in `src/Dashboards/README.md`.