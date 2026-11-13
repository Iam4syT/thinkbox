import json
import sys
from pathlib import Path


def evaluate(path, limit_ms=250):
    checks = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(checks, list) or not checks:
        raise ValueError("expected a nonempty list of checks")
    failures = []
    for index, check in enumerate(checks, start=1):
        if not isinstance(check, dict):
            raise ValueError(f"invalid check at row {index}")
        status, latency = check.get("status"), check.get("latency_ms")
        if type(status) is not int or type(latency) is not int or latency < 0:
            raise ValueError(f"invalid status or latency at row {index}")
        if status != 200 or latency > limit_ms:
            failures.append(index)
    return failures


def main():
    try:
        failures = evaluate(sys.argv[1])
    except (IndexError, OSError, ValueError) as exc:
        print(f"Invalid health data: {exc}", file=sys.stderr)
        return 2
    if failures:
        print(f"Hold release. Failed rows: {failures}")
        return 1
    print("Release checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
