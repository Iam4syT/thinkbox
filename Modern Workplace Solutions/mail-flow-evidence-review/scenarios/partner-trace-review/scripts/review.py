"""Review synthetic trace evidence without changing a tenant."""
import json, sys

def review(rows):
    if not isinstance(rows, list) or not rows:
        raise ValueError("Expected a nonempty list")
    seen=set(); result=[]
    actions={"Delivered":"Check recipient experience; delivered is not proof of inbox visibility", "Failed":"Inspect failure detail and authorised next diagnostic", "Deferred":"Inspect delay detail and recheck within agreed interval", "Unknown":"Request trace evidence; do not infer delivery"}
    for row in rows:
        if not isinstance(row,dict): raise ValueError("Expected record")
        for key in ["id","tenant","trace_status","impact","observed_at"]:
            if not isinstance(row.get(key),str) or not row[key].strip():raise ValueError("Missing " + key)
        if row["id"] in seen: raise ValueError("Duplicate case ID")
        seen.add(row["id"])
        if row["trace_status"] not in actions:raise ValueError("Unsupported status")
        if row.get("access_authorised") is not True:
            action="Stop tenant diagnostics; obtain approved access or administrator-provided evidence"
        else:action=actions[row["trace_status"]]
        result.append({"id":row["id"],"tenant":row["tenant"],"status":row["trace_status"],"next_action":action,"human_review_required":True,"setting_changed":False})
    return result

if __name__=="__main__":
    try:
        if len(sys.argv)!=2:raise ValueError("Usage: python3 scripts/review.py fixtures/sample.json")
        output=review(json.load(open(sys.argv[1],encoding="utf-8")))
        print(json.dumps(output,indent=2))
    except (OSError,ValueError,TypeError) as exc:
        print("Input rejected: "+str(exc),file=sys.stderr);sys.exit(2)
