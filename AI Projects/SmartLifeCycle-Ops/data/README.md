# Data provenance

The committed devices.csv is a historical synthetic fixture, not customer/device telemetry. The current trainer generates its own deterministic 2,500-row fixture using NumPy default_rng seed 42. Labels are the documented refresh rule, not real failures. The API rebuilds a small model from this source on startup. No committed pickle is loaded or required. Run `python app/models/train_model.py` for holdout and rule-baseline metrics in evidence/evaluation.json.
