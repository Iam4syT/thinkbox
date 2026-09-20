"""Labelled synthetic policy evaluation. Unknowns are counted separately."""
import json
from pathlib import Path
from core_engine.policy import assess_record

CASES = [
    ("private HR", "Highly Confidential", ["HR-Managers"], "allowed"),
    ("broad HR", "Highly Confidential", ["All-Employees"], "exposed"),
    ("broad confidential", "Confidential", ["All-Employees"], "exposed"),
    ("internal employees", "Internal Only", ["All-Employees"], "allowed"),
    ("internal anonymous", "Internal Only", ["Anonymous"], "exposed"),
    ("public catalogue", "Public", ["Anonymous"], "allowed"),
    ("unknown group", "Highly Confidential", ["Mystery"], "review"),
    ("missing class", None, ["All-Employees"], "review"),
    ("missing access", "Confidential", [], "review"),
    ("mixed groups", "Highly Confidential", ["HR-Managers", "All-Employees"], "exposed")
]

def evaluate():
    rows = [{"case": name, "expected": expected, "actual": assess_record({"classification": cls, "access_groups": groups})["decision"]} for name, cls, groups, expected in CASES]
    result = {"dataset": "10 hand-labelled synthetic cases, policy version 1; not real tenant data", "sample_size": len(rows),
              "false_positives": sum(r["actual"] == "exposed" and r["expected"] == "allowed" for r in rows),
              "false_negatives": sum(r["actual"] == "allowed" and r["expected"] == "exposed" for r in rows),
              "manual_review": sum(r["actual"] == "review" for r in rows),
              "policy_mismatches": sum(r["actual"] != r["expected"] for r in rows),
              "baseline": "Explicit non-AI metadata rules; no claim of AI uplift", "cases": rows}
    out = Path(__file__).resolve().parent / "evidence"
    out.mkdir(exist_ok=True)
    (out / "evaluation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if result["policy_mismatches"]: raise SystemExit(1)

if __name__ == "__main__": evaluate()
