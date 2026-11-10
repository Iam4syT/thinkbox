"""Evaluate synthetic change evidence for a human decision."""
import argparse
import json
from pathlib import Path

REQUIRED = ('baseline', 'allowed_access', 'denied_access', 'sharing', 'sync', 'rollback', 'handover')
VALID = {"pass", "fail", "unknown"}


def review(observations):
    if not isinstance(observations, dict):
        raise ValueError("Expected a JSON object")
    if set(observations) - set(REQUIRED):
        raise ValueError("Unexpected check name")
    if any(not isinstance(value, str) or value not in VALID for value in observations.values()):
        raise ValueError("Use pass, fail or unknown")
    checks = {name: observations.get(name, "unknown") for name in REQUIRED}
    return {
        "decision": "READY_FOR_REVIEW" if all(value == "pass" for value in checks.values()) else "HOLD",
        "checks": checks,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("evidence", type=Path)
    args = parser.parse_args()
    try:
        result = review(json.loads(args.evidence.read_text(encoding="utf-8")))
    except (OSError, ValueError) as error:
        parser.exit(2, f"Input error: {error}\n")
    print(json.dumps(result, indent=2))
