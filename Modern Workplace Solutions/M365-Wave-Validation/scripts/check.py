RULES = ['identity_verified', 'licensing_verified', 'content_verified', 'access_verified', 'mailflow_verified', 'support_owner_verified']
"""Offline evidence checks. No network, tenant changes or automated cutover."""
import json,sys
from pathlib import Path

def evaluate(data):
    if not isinstance(data,dict): raise ValueError("Input must be an object")
    checks=RULES
    missing=[k for k in checks if k not in data]
    if missing: return {"status":"REVIEW", "failed":[], "unknown":missing}
    if any(type(data[k]) is not bool for k in checks):
        raise ValueError("Evidence fields must be JSON true/false, never strings")
    failed=[k for k in checks if not data[k]]
    return {"status":"HOLD" if failed else "CHECKS_PASS", "failed":failed,"unknown":[]}

def main():
    if len(sys.argv)!=2: print("Usage: python3 scripts/check.py templates/sample.json",file=sys.stderr);return 2
    try:
        report=evaluate(json.loads(Path(sys.argv[1]).read_text()))
    except (ValueError,OSError) as exc:
        print(json.dumps({"status":"INVALID","error":str(exc)}));return 2
    print(json.dumps(report,indent=2))
    return 0 if report["status"]=="CHECKS_PASS" else 1
if __name__=="__main__": sys.exit(main())
