import pandas as pd
from sklearn.ensemble import IsolationForest
import os

def detect_systemic_anomalies():
    # Make sure we use relative path matching from workspace root or folder root
    raw_log_path = 'src/Analytics/data/azure_telemetry_raw.csv'
    
    # Fallback to local directory check if running from src/Analytics directory
    if not os.path.exists(raw_log_path) and os.path.exists('data/azure_telemetry_raw.csv'):
        raw_log_path = 'data/azure_telemetry_raw.csv'
        output_path = 'data/telemetry_anomaly_insights.csv'
    else:
        output_path = 'src/Analytics/data/telemetry_anomaly_insights.csv'
        
    if not os.path.exists(raw_log_path):
        raise FileNotFoundError(f"Raw telemetry data missing at {raw_log_path}. Run LogParser.py first.")
        
    df = pd.read_csv(raw_log_path)
    
    # Isolate numeric metric values for Isolation Forest training
    X = df[['MetricValue']].values
    
    # Configure the ML Model (Contamination factor handles the expected % of anomalies)
    model = IsolationForest(contamination=0.05, random_state=42)
    df['Anomaly_Score'] = model.fit_predict(X)
    
    # Mapping output: -1 indicates an anomaly, 1 indicates normal operational traffic
    df['Is_Anomaly'] = df['Anomaly_Score'].apply(lambda x: "Yes" if x == -1 else "No")
    
    anomalies_detected = df[df['Is_Anomaly'] == "Yes"]
    
    # Save the output for Power BI consumption
    df.to_csv(output_path, index=False)
    
    print(f"📊 Machine Learning Processing Complete.")
    print(f"⚠️ Flagged {len(anomalies_detected)} out of {len(df)} telemetry logs as systemic anomalies.")
    print(f"📁 Insights exported to {output_path} for Power BI modeling.")

if __name__ == "__main__":
    detect_systemic_anomalies()
