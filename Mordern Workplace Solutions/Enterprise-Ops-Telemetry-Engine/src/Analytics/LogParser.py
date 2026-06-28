import os
import json
import pandas as pd
from datetime import datetime, timedelta
import random

def generate_mock_telemetry(num_records=1000):
    """Generates synthetic Azure Log Analytics workspace telemetry."""
    categories = ['Authentication', 'VirtualMachines', 'FinOps_Cost', 'Intune_Enrollment']
    severities = ['Informational', 'Warning', 'Critical']
    
    start_time = datetime.now() - timedelta(days=7)
    data = []
    
    for i in range(num_records):
        timestamp = start_time + timedelta(minutes=random.randint(1, 10080))
        category = random.choices(categories, weights=[0.4, 0.3, 0.2, 0.1])[0]
        severity = random.choices(severities, weights=[0.7, 0.2, 0.1])[0]
        
        # Simulate a standard message or inject an operational anomaly
        if category == 'FinOps_Cost' and random.random() > 0.95:
            message = "Unmapped Resource Cost Spike: Discovered orphaned premium storage tier."
            metric_val = random.uniform(500.0, 1500.0) # Anomaly
        else:
            message = f"Standard telemetry ping for operational category: {category}"
            metric_val = random.uniform(5.0, 50.0)
            
        data.append({
            "Timestamp": timestamp.isoformat(),
            "Category": category,
            "Severity": severity,
            "Message": message,
            "MetricValue": round(metric_val, 2)
        })
        
    df = pd.DataFrame(data)
    os.makedirs('src/Analytics/data', exist_ok=True)
    df.to_csv('src/Analytics/data/azure_telemetry_raw.csv', index=False)
    print("✅ Synthetic Azure Monitor log telemetry generated and saved to src/Analytics/data/azure_telemetry_raw.csv")

if __name__ == "__main__":
    generate_mock_telemetry()