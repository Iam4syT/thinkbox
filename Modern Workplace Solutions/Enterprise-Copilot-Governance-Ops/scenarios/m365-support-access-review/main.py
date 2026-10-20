"""Offline synthetic evidence review. No Microsoft service calls or access changes."""
import argparse, json
from pathlib import Path

def review(row):
    required = {"id", "licence", "service_health", "access", "label", "encrypted"}
    if not required.issubset(row):
        raise ValueError("Missing required evidence fields")
    if row["licence"] not in {"yes", "no", "unknown"} or row["service_health"] not in {"healthy", "incident", "unknown"} or row["access"] not in {"scoped", "broad", "unknown"} or row["label"] not in {"public", "confidential", "unknown"} or row["encrypted"] not in {True, False, "unknown"}:
        raise ValueError("Invalid evidence state")
    reasons = []
    if row["label"] == "confidential" and row["access"] == "broad": reasons.append("review_oversharing")
    if "unknown" in [row[k] for k in required - {"id"}]: reasons.append("collect_evidence")
    if row["licence"] == "no": reasons.append("check_licence")
    if row["service_health"] == "incident": reasons.append("check_service_incident")
    return {"id":row["id"], "status":"review_required" if reasons else "no_flag_in_model", "reasons":reasons, "label_is_not_enforcement":row["label"] == "confidential" and row["encrypted"] is False, "authorises_change":False}

def run(source, target):
    rows = json.loads(Path(source).read_text())
    ids = [r.get("id") for r in rows]
    if len(ids) != len(set(ids)): raise ValueError("Duplicate case ID")
    output = [review(row) for row in rows]
    Path(target).write_text(json.dumps(output,indent=2)+"\n")
    return output

if __name__ == "__main__":
    p=argparse.ArgumentParser(); p.add_argument("--input", default="fixtures.json"); p.add_argument("--output", default="report.json"); a=p.parse_args()
    try: run(a.input,a.output)
    except (ValueError, KeyError, TypeError, OSError) as e: p.exit(2,str(e)+"\n")
