"""
SmartLifecycle-Ops: Enterprise Core OpenAPI Gateway Execution Module
"""

import os
import pickle
import datetime
import uvicorn
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, EmailStr

app = FastAPI(
    title="SmartLifecycle-Ops Core Engine",
    description="Automated IT Asset Modern Workplace Lifecycle & Telemetry Gateway API Pipeline",
    version="1.0.0"
)

# Global variables for ML model storage
MODEL_PATH = os.path.join(os.getcwd(), 'data', 'predictive_refresh_model.pkl')
hardware_model = None

# --- PYDANTIC SCHEMAS ---
class EmployeeOnboardPayload(BaseModel):
    employee_id: str = Field(..., example="usr-94827-2026", description="Unique alphanumeric identifier.")
    full_name: str = Field(..., example="Jane Doe")
    department: str = Field(..., example="Workplace Technology")
    os_platform: str = Field(..., example="macOS", description="Must resolve to either macOS or Windows11")
    corporate_email: EmailStr = Field(..., example="jane.doe@enterprise.com")

class TelemetryPayload(BaseModel):
    device_serial: str = Field(..., example="TL-SN-9482-2026")
    battery_cycle_count: int = Field(..., example=680, ge=0)
    average_cpu_temp_c: float = Field(..., example=89.4, ge=0.0)
    disk_read_error_rate: float = Field(..., example=0.012, ge=0.0)
    device_age_months: int = Field(..., example=24, ge=0)

# --- STARTUP EVENT ---
@app.on_event("startup")
def load_assets():
    global hardware_model
    if not os.path.exists(MODEL_PATH):
        raise RuntimeError(f"Serialized model not found at {MODEL_PATH}. Run training script first.")
    with open(MODEL_PATH, 'rb') as f:
        hardware_model = pickle.load(f)
    print("[+] API Engine Startup Hook: Predictive ML Classifier loaded into active memory successfully.")

# --- ROUTE OVERVIEWS ---
@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return {
        "system_status": "ONLINE",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "documentation": "/docs"
    }

@app.post("/webhook/onboard", status_code=status.HTTP_201_CREATED)
def process_onboarding_webhook(payload: EmployeeOnboardPayload):
    """
    Simulates automated zero-touch enterprise onboarding architecture across Intune & JAMF platforms.
    """
    platform = payload.os_platform.strip().lower()
    serial_derived = f"TL-SN-{payload.employee_id[-5:].upper()}-2026"
    
    response_payload = {
        "orchestration_timestamp": datetime.datetime.utcnow().isoformat(),
        "employee_id": payload.employee_id,
        "active_directory_synced": True,
        "mfa_enforced": True,
        "assigned_hardware_serial": serial_derived
    }
    
    if platform in ["macos", "apple", "ios"]:
        response_payload["mdm_platform"] = "JAMF Pro Automation Engine"
        response_payload["assigned_configuration_payload"] = "Apple_Security_Baseline_ISO27001"
        response_payload["bootstrap_token_escrowed"] = True
    elif platform in ["windows11", "windows", "win11"]:
        response_payload["mdm_platform"] = "Microsoft Intune / Windows Autopilot"
        response_payload["assigned_configuration_payload"] = "Win11_Corporate_Secure_Baseline"
        response_payload["azure_ad_joined"] = True
    else:
        raise HTTPException(
            status_code=400, 
            detail=f"Unsupported OS platform designation: {payload.os_platform}. Use 'macOS' or 'Windows11'."
        )
        
    return {
        "status": "PROVISIONED",
        "telemetry_registration": response_payload
    }

@app.post("/predict/refresh", status_code=status.HTTP_200_OK)
def predict_device_lifecycle(payload: TelemetryPayload):
    """
    Consumes live hardware monitoring metrics and passes vectors directly to the internal model.
    """
    if hardware_model is None:
        raise HTTPException(status_code=500, detail="Predictive model engine context is not initialized.")
        
    # Build array structured identical to the model training configuration layout
    input_vector = [[
        payload.battery_cycle_count,
        payload.average_cpu_temp_c,
        payload.disk_read_error_rate,
        payload.device_age_months
    ]]
    
    # Predict class (0 = Healthy, 1 = Immediate Replacement Required)
    prediction = int(hardware_model.predict(input_vector)[0])
    probabilities = hardware_model.predict_proba(input_vector)[0]
    failure_probability = float(probabilities[1])
    
    action_recommendation = (
        "FLAGGED_FOR_IMMEDIATE_REFRESH" if prediction == 1 
        else "RETAIN_IN_PRODUCTION"
    )
    
    return {
        "device_serial": payload.device_serial,
        "failure_risk_probability": round(failure_probability, 4),
        "lifecycle_assessment_prediction": prediction,
        "recommended_action": action_recommendation,
        "evaluation_timestamp": datetime.datetime.utcnow().isoformat()
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)