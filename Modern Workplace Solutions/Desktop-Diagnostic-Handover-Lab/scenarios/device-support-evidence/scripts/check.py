import argparse, json, os, tempfile
from pathlib import Path

FIELDS = ['power_ok', 'peripheral_ok', 'os_ok', 'task_ok', 'user_confirmed']

def validate(data):
    if not isinstance(data, list) or not data:
        raise ValueError("Expected a non-empty list")
    seen = set()
    for row in data:
        if not isinstance(row, dict) or set(row) != set(FIELDS) | {"id"}:
            raise ValueError("Unexpected or missing fields")
        name = row["id"]
        if not isinstance(name, str) or not name or name in seen:
            raise ValueError("IDs must be non-empty unique strings")
        seen.add(name)
        for field in FIELDS:
            if row[field] is not None and type(row[field]) is not bool:
                raise ValueError("Observations must be true, false or null")
    return data

def evaluate(data):
    return [classify(row) for row in validate(data)]

def classify(row):
    failed = [f for f in FIELDS if row[f] is False]
    missing = [f for f in FIELDS if row[f] is None]
    state = "review_failure" if failed else "collect_evidence" if missing else "ready_for_human_closure"
    return {"id": row["id"], "state": state, "failed": failed, "missing": missing,
            "closed": False, "next": "Human reviews scope, original task and user confirmation; no repair is automated."}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("input", type=Path)
    p.add_argument("output", type=Path)
    args = p.parse_args()
    if args.input.resolve() == args.output.resolve():
        p.error("Input and output must differ")
    try:
        result = evaluate(json.loads(args.input.read_text()))
    except (ValueError, OSError) as e:
        p.error(str(e))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", dir=args.output.parent, delete=False) as f:
        json.dump(result, f, indent=2)
        temp = f.name
    os.replace(temp, args.output)

if __name__ == "__main__":
    main()
