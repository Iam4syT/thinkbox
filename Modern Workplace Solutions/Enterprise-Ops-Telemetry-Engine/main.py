import sys
import os

# Ensure src modules are resolvable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from Analytics.LogParser import generate_mock_telemetry
from Analytics.anomalous_noise_detector import detect_systemic_anomalies

def main():
    print("==========================================================================")
    print("STARTING: ENTERPRISE OPS TELEMETRY ENGINE PIPELINE")
    print("==========================================================================")
    
    print("\n[Step 1] Generating Synthetic Azure Monitor Log Telemetry...")
    generate_mock_telemetry()
    
    print("\n[Step 2] Executing Machine Learning Anomaly Detection Model...")
    detect_systemic_anomalies()
    
    print("\n==========================================================================")
    print("SUCCESS: Telemetry processing complete. Insights ready for Power BI.")
    print("==========================================================================")

if __name__ == "__main__":
    main()
