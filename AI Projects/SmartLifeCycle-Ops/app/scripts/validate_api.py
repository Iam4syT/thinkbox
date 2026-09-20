"""Local API contract checks; no external service calls."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from fastapi.testclient import TestClient
from app.main import app

def run_validation():
    person = {"employee_id": "demo-1", "full_name": "Example User", "department": "Lab", "corporate_email": "example@example.com", "os_platform": "macOS"}
    device = {"device_serial": "synthetic-1", "battery_cycle_count": 100, "average_cpu_temp_c": 55, "disk_read_error_rate": .001, "device_age_months": 6}
    with TestClient(app) as client:
        assert client.get("/").json()["mode"] == "simulation"
        for platform, expected in [("macOS", "JAMF"), ("Windows11", "Intune")]:
            response = client.post("/webhook/onboard", json={**person, "os_platform": platform})
            assert response.status_code == 201
            result = response.json()
            assert result["status"] == "SIMULATION_ONLY" and not result["external_systems_changed"]
            assert not result["performed_actions"] and expected in result["proposed_plan"]["mdm_platform"]
        assert client.post("/webhook/onboard", json={**person, "os_platform": "Linux"}).status_code == 400
        for cycles, temperature, expected in [(100, 55, 0), (900, 95, 1)]:
            response = client.post("/predict/refresh", json={**device, "battery_cycle_count": cycles, "average_cpu_temp_c": temperature})
            assert response.status_code == 200
            assert response.json()["synthetic_rule_class"] == expected
            assert response.json()["performed_actions"] == []
        for key, value in [("battery_cycle_count", -1), ("disk_read_error_rate", 1.1), ("average_cpu_temp_c", 151), ("device_age_months", -1)]:
            assert client.post("/predict/refresh", json={**device, key: value}).status_code == 422
    print("PASS: simulation contracts, two platform plans, healthy/degraded fixtures and invalid telemetry")

if __name__ == "__main__": run_validation()
