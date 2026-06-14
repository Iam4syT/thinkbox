"""
SmartLifecycle-Ops: Predictive Lifecycle Machine Learning Pipeline
Author: Lead Workplace Systems Engineer
"""

import os
import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def execute_model_training():
    print("[*] Starting Hardware Refresh Predictive Model Training...")
    
    # Target path setup
    data_dir = os.path.join(os.getcwd(), 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    # 1. Generate Synthetic Enterprise Endpoint Telemetry (2500 Devices)
    np.random.seed(42)
    sample_size = 2500
    
    data = {
        'battery_cycle_count': np.random.randint(10, 950, sample_size),
        'average_cpu_temp_c': np.random.uniform(40.0, 98.0, sample_size),
        'disk_read_error_rate': np.random.uniform(0.0, 0.08, sample_size),
        'device_age_months': np.random.randint(1, 48, sample_size)
    }
    
    df = pd.DataFrame(data)
    df.to_csv("data/devices.csv", index=False)

    
    # 2. Establish Concrete Enterprise Hardware Degradation Rules
    # Condition: High thermal throttling, exhausted battery cycles, or old age combined with faults
    df['requires_immediate_refresh'] = (
        (df['battery_cycle_count'] > 700) | 
        (df['average_cpu_temp_c'] > 88.5) | 
        ((df['device_age_months'] >= 36) & (df['disk_read_error_rate'] > 0.04))
    ).astype(int)
    
    # 3. Extract Features and Split Target Matrix
    X = df[['battery_cycle_count', 'average_cpu_temp_c', 'disk_read_error_rate', 'device_age_months']]
    y = df['requires_immediate_refresh']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    
    # 4. Initialize and Train Random Forest Model
    model = RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42)
    model.fit(X_train, y_train)
    
    # 5. Evaluate Operational Performance Matrix
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"[+] Model Training Finished Successfully. Test Accuracy Baseline: {accuracy * 100:.2f}%")
    
    # 6. Serialize and Persist Model Output
    model_path = os.path.join(data_dir, 'predictive_refresh_model.pkl')
    with open(model_path, 'wb') as file:
        pickle.dump(model, file)
    print(f"[+] Saved serialized production model asset to: {model_path}")

if __name__ == "__main__":
    execute_model_training()