import json, sys
FIELDS = {"request_id", "approval", "account_signin", "mail", "sharepoint_access", "device_check", "app_check", "handover_review"}
def check(record):
    if not isinstance(record, dict) or set(record) != FIELDS:
        raise ValueError("exact schema required")
    if not isinstance(record["request_id"],str) or not record["request_id"].strip():
        raise ValueError("request_id must be nonempty text")
    checks=FIELDS-{"request_id"}
    if any(type(record[k]) is not bool for k in checks):
        raise ValueError("checks must be booleans")
    missing=sorted(k for k in checks if not record[k])
    return "BLOCKED: " + ", ".join(missing) if missing else "READY FOR HUMAN REVIEW"
if __name__ == "__main__":
    try:
        if len(sys.argv)!=2: raise ValueError("usage: check.py record.json")
        print(check(json.load(open(sys.argv[1],encoding="utf-8"))))
    except (ValueError,OSError) as error:
        print("INVALID:",error); sys.exit(2)
