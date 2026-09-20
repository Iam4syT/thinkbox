"""Deterministic synthetic telemetry with known injected labels."""
from datetime import datetime, timedelta, timezone
from pathlib import Path
import random
import pandas as pd
DATA = Path(__file__).resolve().parent / "data"

def generate_mock_telemetry(num_records=1000, seed=42, output_dir=None):
    if isinstance(num_records, bool) or not isinstance(num_records, int) or num_records < 20:
        raise ValueError("Use at least 20 synthetic records")
    rng = random.Random(seed)
    start = datetime(2026, 1, 1, tzinfo=timezone.utc)
    rows = []
    for i in range(num_records):
        category = rng.choice(["Authentication", "VirtualMachines", "FinOps_Cost", "Intune_Enrollment"])
        anomalous = i % 50 == 0
        rows.append({"Timestamp": (start + timedelta(minutes=i)).isoformat(), "Category": category,
                     "MetricValue": round(rng.uniform(500, 1500) if anomalous else rng.uniform(5, 50), 2),
                     "KnownAnomaly": int(anomalous), "Source": "synthetic"})
    frame = pd.DataFrame(rows)
    out = Path(output_dir or DATA); out.mkdir(parents=True, exist_ok=True)
    frame.to_csv(out / "azure_telemetry_raw.csv", index=False)
    return frame

if __name__ == "__main__":
    print("Synthetic rows generated:", len(generate_mock_telemetry()))
