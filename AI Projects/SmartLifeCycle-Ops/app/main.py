"""Local endpoint lifecycle simulation. No directory, MDM or hardware changes."""
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from pathlib import Path
import sys
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, EmailStr, Field
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app.models.train_model import execute_model_training, FEATURES, rule_baseline

@asynccontextmanager
async def lifespan(app):
    # Rebuild from local synthetic source; never load an untrusted committed pickle.
    app.state.model, app.state.evaluation = execute_model_training()
    yield

app = FastAPI(title="SmartLifeCycle Ops — synthetic lab", version="1.1.0", lifespan=lifespan)

class EmployeeOnboardPayload(BaseModel):
    employee_id: str = Field(min_length=1, max_length=100)
    full_name: str = Field(min_length=1, max_length=200)
    department: str = Field(min_length=1, max_length=200)
    os_platform: str
    corporate_email: EmailStr

class TelemetryPayload(BaseModel):
    model_config = ConfigDict(allow_inf_nan=False)
    device_serial: str = Field(min_length=1, max_length=100)
    battery_cycle_count: int = Field(ge=0, le=10000)
    average_cpu_temp_c: float = Field(ge=0, le=150)
    disk_read_error_rate: float = Field(ge=0, le=1)
    device_age_months: int = Field(ge=0, le=360)

@app.get("/")
def read_root():
    return {"system_status": "ONLINE", "mode": "simulation", "documentation": "/docs"}

@app.post("/webhook/onboard", status_code=201)
def process_onboarding_webhook(payload: EmployeeOnboardPayload):
    platform = payload.os_platform.strip().lower()
    if platform in {"macos", "apple"}: mdm = "JAMF Pro"
    elif platform in {"windows11", "windows", "win11"}: mdm = "Intune / Windows Autopilot"
    else: raise HTTPException(400, "Use macOS or Windows11")
    return {"status": "SIMULATION_ONLY", "employee_id": payload.employee_id,
            "proposed_plan": {"mdm_platform": mdm, "actions": ["Confirm identity and group scope", "Review MFA requirements", "Enrol a permitted test device", "Verify baseline compliance"]},
            "performed_actions": [], "external_systems_changed": False}

@app.post("/predict/refresh")
def predict_device_lifecycle(payload: TelemetryPayload):
    model = getattr(app.state, "model", None)
    if model is None: raise HTTPException(503, "Synthetic model is not initialised")
    frame = pd.DataFrame([{key: getattr(payload, key) for key in FEATURES}])
    predicted = int(model.predict(frame)[0])
    positive_index = list(model.classes_).index(1)
    score = float(model.predict_proba(frame)[0][positive_index])
    return {"mode": "simulation", "device_serial": payload.device_serial, "synthetic_rule_class": predicted,
            "synthetic_class_probability": round(score, 4), "rule_baseline_class": int(rule_baseline(frame).iloc[0]),
            "proposed_action": "REVIEW_DEVICE" if predicted else "NO_REFRESH_FLAG_IN_THIS_MODEL",
            "performed_actions": [], "limitation": "Model agreement with synthetic rules, not a real failure-risk estimate",
            "evaluated_at": datetime.now(timezone.utc).isoformat()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
