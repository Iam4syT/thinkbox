"""Offline synthetic record validator; no network, credentials or remediation."""
import json
MODE = 'readiness'
FIELDS = ['os', 'account', 'network', 'software', 'peripheral']
EXTRA = set()
import sys
from pathlib import Path

def inspect_record(data):
    if not isinstance(data, dict):
        raise ValueError("Record must be an object")
    fields = FIELDS
    allowed = set(fields) | EXTRA
    if set(data) - allowed:
        raise ValueError("Unexpected fields are not permitted")
    if MODE == "readiness":
        if set(data) != set(fields):
            raise ValueError("All five readiness fields are required")
        if any(not isinstance(v,str) or v not in {"pass","fail","pending"} for v in data.values()):
            raise ValueError("Use pass, fail or pending")
        return {"status": "READY" if all(v == "pass" for v in data.values()) else "REVIEW", "review": [k for k in fields if data[k] != "pass"]}
    if type(data.get("security_incident")) is not bool:
        raise ValueError("security_incident must be an explicit boolean")
    if any(k in data and not isinstance(data[k],str) for k in fields):
        raise ValueError("Ticket fields must be text")
    missing = [k for k in fields if not data.get(k, "").strip()]
    return {"status": "INCOMPLETE" if missing else "COMPLETE", "missing": missing, "route": "SECURITY ESCALATION" if data["security_incident"] else "ROUTINE REVIEW"}

def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError("Supply one synthetic JSON record path")
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        print(json.dumps(inspect_record(data), indent=2))
        return 0
    except (ValueError, OSError) as exc:
        print("Invalid record: " + str(exc), file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
