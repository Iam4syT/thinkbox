import argparse, json, os, tempfile
from pathlib import Path

FIELDS = ['link_ok', 'dns_ok', 'tcp445_ok', 'authorised_user_ok', 'unauthorised_denied']

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
    if row["unauthorised_denied"] is False:
        state = "access_exposure_review"
    elif row["link_ok"] is False:
        state = "check_link"
    elif row["dns_ok"] is False:
        state = "check_dns"
    elif row["tcp445_ok"] is False:
        state = "check_service_path"
    elif row["authorised_user_ok"] is False:
        state = "check_identity_permissions"
    elif missing:
        state = "collect_evidence"
    else:
        state = "ready_for_human_review"
    return {"id": row["id"], "state": state, "failed": failed, "missing": missing,
            "root_cause_confirmed": False, "changed": False}


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
