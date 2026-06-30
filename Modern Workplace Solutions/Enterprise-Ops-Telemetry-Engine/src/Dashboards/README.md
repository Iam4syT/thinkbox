# 📊 Power BI Dashboard Configuration

To complete the visualization layer (Step 5 of the lab instructions), configure your Power BI workspace using the anomalous logs output:

## Data Import Instructions
1. Open **Power BI Desktop**.
2. Select **Get Data** -> **Text/CSV**.
3. Point it to the generated anomaly insights CSV file:
   `src/Analytics/data/telemetry_anomaly_insights.csv`

## Dashboard Component Specifications
Build the following three key reporting components:

1. **Total Cost / Metric Log Count Card**:
   - Ingestion metric count to verify data volume.
2. **Anomalous Drift Rate Card**:
   - Visual gauge displaying percentage of events flagged as `Is_Anomaly = Yes`.
3. **License & Operational Drift Chart**:
   - A clustered bar chart tracking `Category` vs. `MetricValue` (filtered by anomalies) to isolate unmapped resource expenditures.

Save this configuration as a Power BI template: `src/Dashboards/ServiceIntelligence.pbit`.
