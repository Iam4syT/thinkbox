"""Compare an Isolation Forest with a simple threshold on synthetic held-out rows."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score
DATA = Path(__file__).resolve().parent / "data"

def measures(truth, predicted):
    tn, fp, fn, tp = confusion_matrix(truth, predicted, labels=[0, 1]).ravel()
    return {"true_positive": int(tp), "false_positive": int(fp), "false_negative": int(fn), "true_negative": int(tn),
            "precision": float(precision_score(truth, predicted, zero_division=0)), "recall": float(recall_score(truth, predicted, zero_division=0)),
            "f1": float(f1_score(truth, predicted, zero_division=0))}

def detect_systemic_anomalies(raw_log_path=None, output_dir=None):
    frame = pd.read_csv(raw_log_path or DATA / "azure_telemetry_raw.csv")
    required = {"MetricValue", "KnownAnomaly"}
    if not required.issubset(frame) or len(frame) < 20: raise ValueError("Labelled synthetic fixture with at least 20 rows required")
    if not np.isfinite(frame["MetricValue"]).all() or not frame.KnownAnomaly.isin([0, 1]).all(): raise ValueError("Invalid metrics or labels")
    if frame.KnownAnomaly.value_counts().min() < 2 or frame.KnownAnomaly.nunique() != 2: raise ValueError("Both labels need at least two samples")
    train, test = train_test_split(frame, test_size=.4, random_state=42, stratify=frame.KnownAnomaly)
    model = IsolationForest(contamination=.05, random_state=42)
    model.fit(train[["MetricValue"]])
    test = test.copy()
    test["ModelAnomaly"] = (model.predict(test[["MetricValue"]]) == -1).astype(int)
    test["ThresholdAnomaly"] = (test.MetricValue > 100).astype(int)
    report = {"dataset": "Deterministic synthetic fixture; 2% injected high-metric anomalies", "seed": 42,
              "train_size": len(train), "test_size": len(test), "isolation_forest": measures(test.KnownAnomaly, test.ModelAnomaly),
              "threshold_baseline": measures(test.KnownAnomaly, test.ThresholdAnomaly),
              "limitations": "Threshold exploits the known fixture gap. No live Azure ingestion, self-healing, incident reduction or business savings measured."}
    out = Path(output_dir or DATA); out.mkdir(parents=True, exist_ok=True)
    test.to_csv(out / "telemetry_anomaly_insights.csv", index=False)
    evidence = Path(__file__).resolve().parents[2] / "evidence" if output_dir is None else out
    evidence.mkdir(exist_ok=True)
    (evidence / "evaluation.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return report

if __name__ == "__main__": detect_systemic_anomalies()
