"""
SmartLifecycle-Ops: Automated API Integration & Telemetry Validation Script
"""

import sys
import os

# Add root directory to sys.path to allow imports from app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from fastapi.testclient import TestClient
from app.main import app

def run_validation():
    print("[*] Initializing API Validation Test Suite...")
    with TestClient(app) as client:
        # 1. Health Check Test
        print("[*] Testing health check root endpoint '/'...")
        response = client.get("/")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        data = response.json()
        assert data["system_status"] == "ONLINE", f"Expected ONLINE, got {data['system_status']}"
        print("[+] Health check endpoint PASSED.")
        
        # 2. Onboarding Webhook Tests (macOS Platform)
        print("[*] Testing onboarding webhook with macOS payload...")
        macos_payload = {
            "employee_id": "usr-94827-2026",
            "full_name": "Jane Doe",
            "department": "Workplace Technology",
            "os_platform": "macOS",
            "corporate_email": "jane.doe@enterprise.com"
        }
        response = client.post("/webhook/onboard", json=macos_payload)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        data = response.json()
        assert data["status"] == "PROVISIONED", f"Expected PROVISIONED, got {data['status']}"
        assert data["telemetry_registration"]["mdm_platform"] == "JAMF Pro Automation Engine", "Expected JAMF Pro MDM"
        assert data["telemetry_registration"]["assigned_hardware_serial"] == f"TL-SN-{macos_payload['employee_id'][-5:].upper()}-2026", "Incorrect serial mapping"
        print("[+] Onboarding macOS webhook PASSED.")
        
        # 3. Onboarding Webhook Tests (Windows 11 Platform)
        print("[*] Testing onboarding webhook with Windows11 payload...")
        win11_payload = {
            "employee_id": "usr-88392-2026",
            "full_name": "John Smith",
            "department": "Security Operations",
            "os_platform": "Windows11",
            "corporate_email": "john.smith@enterprise.com"
        }
        response = client.post("/webhook/onboard", json=win11_payload)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        data = response.json()
        assert data["status"] == "PROVISIONED", f"Expected PROVISIONED, got {data['status']}"
        assert data["telemetry_registration"]["mdm_platform"] == "Microsoft Intune / Windows Autopilot", "Expected Intune MDM"
        assert data["telemetry_registration"]["assigned_hardware_serial"] == f"TL-SN-{win11_payload['employee_id'][-5:].upper()}-2026", "Incorrect serial mapping"
        print("[+] Onboarding Windows11 webhook PASSED.")

        # 4. Onboarding Webhook Tests (Unsupported Platform)
        print("[*] Testing onboarding webhook with unsupported platform (Linux)...")
        invalid_payload = macos_payload.copy()
        invalid_payload["os_platform"] = "Linux"
        response = client.post("/webhook/onboard", json=invalid_payload)
        assert response.status_code == 400, f"Expected 400, got {response.status_code}"
        print("[+] Onboarding unsupported platform error handling PASSED.")

        # 5. ML Telemetry Predictor (Healthy Device)
        print("[*] Testing ML refresh predictor with nominal (healthy) device vitals...")
        healthy_telemetry = {
            "device_serial": "TL-SN-1102-2026",
            "battery_cycle_count": 120,
            "average_cpu_temp_c": 55.2,
            "disk_read_error_rate": 0.001,
            "device_age_months": 6
        }
        response = client.post("/predict/refresh", json=healthy_telemetry)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        data = response.json()
        assert data["lifecycle_assessment_prediction"] == 0, f"Expected 0, got {data['lifecycle_assessment_prediction']}"
        assert data["recommended_action"] == "RETAIN_IN_PRODUCTION", f"Expected RETAIN_IN_PRODUCTION, got {data['recommended_action']}"
        print("[+] ML predictor healthy device check PASSED.")

        # 6. ML Telemetry Predictor (Degraded Device)
        print("[*] Testing ML refresh predictor with degraded (critical) device vitals...")
        degraded_telemetry = {
            "device_serial": "TL-SN-9482-2026",
            "battery_cycle_count": 780,
            "average_cpu_temp_c": 92.5,
            "disk_read_error_rate": 0.05,
            "device_age_months": 38
        }
        response = client.post("/predict/refresh", json=degraded_telemetry)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        data = response.json()
        assert data["lifecycle_assessment_prediction"] == 1, f"Expected 1, got {data['lifecycle_assessment_prediction']}"
        assert data["recommended_action"] == "FLAGGED_FOR_IMMEDIATE_REFRESH", f"Expected FLAGGED_FOR_IMMEDIATE_REFRESH, got {data['recommended_action']}"
        print("[+] ML predictor degraded device check PASSED.")

        print("\n[+] SUCCESS: All integration validation checks passed successfully!")

if __name__ == "__main__":
    run_validation()
