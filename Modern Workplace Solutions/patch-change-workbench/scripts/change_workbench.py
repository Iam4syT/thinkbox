"""Offline approval-aware queue. Produces proposals/messages; never applies a patch."""
import argparse
import json
import re
from pathlib import Path

SEVERITIES = {"critical":0,"high":1,"medium":2,"low":3}

def version(value):
    if not isinstance(value, str) or not re.fullmatch(r"[0-9]+(?:\.[0-9]+){1,3}", value):
        raise ValueError("versions must be numeric dotted strings")
    return tuple(int(x) for x in value.split(".")) + (0,) * (4-len(value.split(".")))

def plan(payload):
    if not isinstance(payload, dict) or not isinstance(payload.get("findings"), list):
        raise ValueError("findings list required")
    seen, rows = set(), []
    for item in payload["findings"]:
        identifier = item.get("id")
        if not isinstance(identifier, str) or not identifier.startswith("LAB-VULN-") or identifier in seen:
            raise ValueError("unique synthetic finding IDs required")
        seen.add(identifier)
        if item.get("severity") not in SEVERITIES or item.get("exposure") not in {"external", "internal", "unknown"}:
            raise ValueError("explicit severity and exposure required")
        for key in ["patch_available", "approved", "installed", "app_smoke_pass", "reboot_pending", "security_recheck_pass"]:
            if key not in item or (item[key] is not None and type(item[key]) is not bool):
                raise ValueError(key + " must be true, false or null")
        target = version(item.get("target_version"))
        observed = version(item["observed_version"]) if item.get("observed_version") is not None else None
        reasons = []
        if item["installed"] is True and item["app_smoke_pass"] is False:
            state = "rollback_review"
            reasons.append("Application smoke test failed: stop expansion and ask the change owner to review recovery.")
        elif item["patch_available"] is not True or item["exposure"] == "unknown":
            state = "risk_escalation"
            reasons.append("Patch availability or exposure needs security-owner review; do not silently defer risk.")
        elif item["approved"] is not True:
            state = "needs_approval"
            reasons.append("Named change approval not recorded; no deployment proposal is authorised.")
        elif item["installed"] is not True:
            state = "ready_for_pilot"
            reasons.append("Approved test change only: agree pilot users, maintenance window and recovery first.")
        elif observed is None or observed < target or item["app_smoke_pass"] is not True or item["reboot_pending"] is not False or item["security_recheck_pass"] is not True:
            state = "verify_again"
            reasons.append("Do not close: version, restart, app health or security recheck is missing/unsatisfactory.")
        else:
            state = "closed_verified_in_fixture"
            reasons.append("All required synthetic verification fields pass; no live remediation established.")
        messages = {
            "needs_approval": "A software update is being reviewed. No installation time has been agreed yet. We will confirm any impact before the change.",
            "ready_for_pilot": "Your test device is included in an approved pilot. Please save your work before the agreed window. We will confirm whether a restart is needed and check the application afterwards.",
            "verify_again": "The test update needs further checks before we can confirm it is complete. Please keep your work saved and tell the support team about any application problem.",
            "risk_escalation": "The security and change owners are reviewing this finding. A safe next action has not yet been agreed.",
            "rollback_review": "The pilot found an application problem. We have stopped wider rollout and are reviewing a safe recovery with the change owner.",
            "closed_verified_in_fixture": "The synthetic test update passed the recorded checks. This is a lab result, so it does not confirm the health of a real device."
        }
        rows.append({"id":identifier,"severity":item["severity"],"state":state,"reasons":reasons,"user_message":messages[state],"mutation":"none","priority_key":[SEVERITIES[item["severity"]],0 if item["exposure"]=="external" else 1]})
    rows.sort(key=lambda row:(row["priority_key"],row["id"]))
    return {"mode":"offline_synthetic","finding_count":len(rows),"results":rows,"no_data":not rows,"live_remediation_established":False}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",default="templates/findings.json")
    parser.add_argument("--output",default="outputs/change-plan.json")
    args = parser.parse_args()
    try: result = plan(json.loads(Path(args.input).read_text()))
    except (ValueError, OSError, json.JSONDecodeError, AttributeError) as exc: parser.exit(2,"Input rejected: " + str(exc) + "\n")
    output = Path(args.output)
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"finding_count":result["finding_count"],"states":{r["id"]:r["state"] for r in result["results"]},"output":str(output),"mutation":"none"},sort_keys=True))

if __name__ == "__main__": main()
