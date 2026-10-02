"""Offline evidence classification. Does not connect, execute logs or change devices."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

STATES = {"enrolled": "enrolment", "configured": "configuration", "compliant": "compliance", "app_installed": "application", "m365_access": "authentication/connectivity"}
KNOWN_CODES = {"SCOPE_MISMATCH": "Check test user enrolment scope and licence with an authorised administrator.", "CONFIG_CONFLICT": "Compare assigned policies and setting-level conflict evidence.", "DETECTION_FAILED": "Compare detection rule with observed app version and IME logs.", "DNS_FAILURE": "Check name resolution and scope before changing network settings."}

def instant(value):
    point = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if point.tzinfo is None:
        raise ValueError("timestamps must include a timezone")
    return point

def assess(payload, now):
    if not isinstance(payload, dict) or not isinstance(payload.get("devices"), list) or not isinstance(payload.get("logs"), list):
        raise ValueError("input must contain devices and logs lists")
    for entry in payload["logs"]:
        if not isinstance(entry, dict) or not isinstance(entry.get("device_id"), str) or not isinstance(entry.get("code"), str):
            raise ValueError("each log requires string device_id and code fields")
    seen, results = set(), []
    for device in payload["devices"]:
        if not isinstance(device, dict):
            raise ValueError("device must be an object")
        identifier = device.get("id")
        if not isinstance(identifier, str) or not identifier.startswith("LAB-") or identifier in seen:
            raise ValueError("unique synthetic LAB- device IDs are required")
        seen.add(identifier)
        if any(key not in device or (device[key] is not None and type(device[key]) is not bool) for key in STATES):
            raise ValueError("state fields must be true, false or null")
        try:
            hours = (now - instant(device["last_sync"])).total_seconds() / 3600
        except (KeyError, TypeError, AttributeError) as exc:
            raise ValueError("last_sync must be an ISO timestamp") from exc
        if hours < 0:
            raise ValueError("last_sync cannot be in the future")
        evidence = [entry for entry in payload["logs"] if isinstance(entry, dict) and entry.get("device_id") == identifier]
        if any(not isinstance(entry.get("code"), str) for entry in evidence):
            raise ValueError("correlated log entries require a code")
        failed = [scope for key, scope in STATES.items() if device[key] is False]
        unknown = [scope for key, scope in STATES.items() if device[key] is None]
        stale = hours > 24
        if stale:
            unknown.append("current endpoint state: sync older than 24 hours")
        status = "investigate" if failed else "needs_evidence" if unknown else "ready_in_fixture"
        next_steps = [KNOWN_CODES.get(entry["code"], "Unknown synthetic code: collect supporting evidence; do not infer a root cause.") for entry in evidence]
        if not evidence and failed:
            next_steps.append("No correlated log supplied: collect diagnostics and record scope before recommending a change.")
        if stale:
            next_steps.insert(0, "Request fresh test-device check-in before relying on the snapshot.")
        results.append({"id": identifier, "status": status, "failed_scopes": failed, "unknown_scopes": unknown, "evidence_codes": [entry["code"] for entry in evidence], "next_steps": next_steps, "mutation": "none", "cause": "hypothesis only; verify independently" if failed else "not established"})
    if any(entry["device_id"] not in seen for entry in payload["logs"]):
        raise ValueError("log references a device absent from the snapshot")
    return {"mode": "offline_synthetic", "device_count": len(results), "results": results, "no_data": not results, "live_readiness_established": False}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="templates/readiness.json")
    parser.add_argument("--now", default="2026-09-30T09:00:00Z")
    parser.add_argument("--output", default="outputs/readiness.json")
    args = parser.parse_args()
    try:
        result = assess(json.loads(Path(args.input).read_text()), instant(args.now))
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        parser.exit(2, "Input rejected: " + str(exc) + "\n")
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"device_count": result["device_count"], "statuses": {r["id"]: r["status"] for r in result["results"]}, "output": str(out), "mutation": "none"}, sort_keys=True))

if __name__ == "__main__":
    main()
