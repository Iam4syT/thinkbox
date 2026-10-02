"""Deterministic, read-only evaluation of synthetic M365 review snapshots."""
import argparse
import json
import math
from datetime import datetime, timezone
from pathlib import Path

EXPECTED = {"Exchange Online", "SharePoint Online", "Microsoft Teams", "OneDrive for Business"}
NORMAL = {"ServiceOperational", "ServiceRestored", "PostIncidentReviewPublished"}
REVIEW = {"Investigating", "ServiceDegradation", "ServiceInterruption", "RestoringService",
          "ExtendedRecovery", "VerifyingService", "InvestigationSuspended"}


def timestamp(value):
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("timestamps must include UTC offset")
    return result


def number(value, field):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
        raise ValueError(f"{field}: expected finite non-negative number")
    return value


def evaluate(snapshot, as_of):
    """Evaluate declared data only; never connect to a tenant or change state."""
    if snapshot.get("schema_version") != 1:
        raise ValueError("unsupported schema_version")
    now = timestamp(as_of)
    captured = timestamp(snapshot["captured_at"])
    age_hours = (now - captured).total_seconds() / 3600
    if age_hours < 0:
        raise ValueError("capture timestamp is in the future")
    findings = []
    incomplete = False

    def add(code, subject, detail, unknown=False):
        nonlocal incomplete
        incomplete = incomplete or unknown
        findings.append({"code": code, "subject": subject, "detail": detail})

    if age_hours > 48:
        add("STALE_SNAPSHOT", "snapshot", "Refresh before making a current-health statement.", True)
    services = snapshot["services"]
    names = [x["name"] for x in services]
    if len(set(names)) != len(names):
        raise ValueError("duplicate service names")
    for name in sorted(EXPECTED - set(names)):
        add("MISSING_SERVICE", name, "Missing data is not healthy status.", True)
    for item in services:
        if item["status"] in REVIEW:
            add("SERVICE_REVIEW", item["name"], "Check current incident scope and the official update; do not infer a local root cause.")
        elif item["status"] not in NORMAL:
            add("UNKNOWN_STATUS", item["name"], "Map this provider value before interpreting it.", True)
    usage = snapshot["usage"]
    if not usage:
        add("MISSING_USAGE", "usage", "No activity records were provided.", True)
    for item in usage:
        active = number(item["active_users"], "active_users")
        total = number(item["licensed_users"], "licensed_users")
        if active > total:
            raise ValueError("active_users exceeds licensed_users")
        if total == 0:
            add("UNKNOWN_ADOPTION", item["service"], "No denominator; do not infer adoption.", True)
        elif active / total < 0.2:
            add("ADOPTION_REVIEW", item["service"], "Discuss the task and reporting window with the owner; activity is not productivity.")
    storage = snapshot["storage"]
    if not storage:
        add("MISSING_STORAGE", "storage", "No capacity records were provided.", True)
    for item in storage:
        used = number(item["used_bytes"], "used_bytes")
        allocated = number(item["allocated_bytes"], "allocated_bytes")
        if allocated == 0:
            add("UNKNOWN_CAPACITY", item["name"], "No allocation denominator was provided.", True)
        elif used / allocated >= 0.9:
            add("CAPACITY_REVIEW", item["name"], "At least 90% of declared allocation; confirm pool/manual mode and report age.")
        if not item.get("owner"):
            add("OWNER_REVIEW", item["name"], "Identify an accountable owner before changing storage or access.")
    audit = snapshot["audit_events"]
    if not isinstance(audit, list):
        raise ValueError("audit_events must be a list; unknown cannot be an empty clean result")
    if not snapshot.get("audit_complete", False):
        add("AUDIT_INCOMPLETE", "audit", "The synthetic collection does not establish a complete audit window.", True)
    for event in audit:
        if event["severity"] == "review":
            add("AUDIT_REVIEW", event["action"], "Ask the authorised security owner to validate context; no automated remediation.")
        elif event["severity"] != "informational":
            add("UNKNOWN_AUDIT_SEVERITY", event["action"], "Classify before concluding.", True)
    findings.sort(key=lambda x: (x["code"], x["subject"]))
    state = "INCOMPLETE" if incomplete else "REVIEW" if findings else "NO_RULE_FINDINGS"
    return {"scope": "synthetic-read-only", "as_of": as_of, "state": state,
            "service_count": len(services), "findings": findings,
            "interpretation": "No rule findings is not proof of tenant health or security."}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--as-of", required=True, help="ISO timestamp with offset; reproducible evaluation clock")
    args = parser.parse_args()
    try:
        report = evaluate(json.loads(args.input.read_text()), args.as_of)
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        print(json.dumps({"state": "INCOMPLETE", "error": str(error)}, indent=2))
        return 2
    print(json.dumps(report, indent=2, sort_keys=True))
    return {"NO_RULE_FINDINGS": 0, "REVIEW": 1, "INCOMPLETE": 2}[report["state"]]


if __name__ == "__main__":
    raise SystemExit(main())
