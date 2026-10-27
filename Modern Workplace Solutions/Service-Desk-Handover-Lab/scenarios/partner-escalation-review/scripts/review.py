"""Check a synthetic partner handover without granting access or closing cases."""
import json, sys
REQUIRED=["impact","history","configuration","checks","next_action","owner"]
def review(rows):
    if not isinstance(rows,list) or not rows:raise ValueError("Expected a nonempty list")
    seen=set();out=[]
    for row in rows:
        if not isinstance(row,dict):raise ValueError("Expected record")
        for key in ["id","tenant","evidence_tenant"]:
            if not isinstance(row.get(key),str) or not row[key].strip():raise ValueError("Missing "+key)
        if row["id"] in seen:raise ValueError("Duplicate case ID")
        seen.add(row["id"])
        missing=[key for key in REQUIRED if not isinstance(row.get(key),str) or not row[key].strip()]
        reasons=[]
        if row["tenant"]!=row["evidence_tenant"]:reasons.append("Evidence belongs to another tenant")
        if row.get("access_authorised") is not True:reasons.append("Access authorisation unconfirmed")
        if row.get("sanitised") is not True:reasons.append("Sanitisation unconfirmed")
        reasons += ["Missing "+key for key in missing]
        out.append({"id":row["id"],"review_state":"hold" if reasons else "human_review", "reasons":reasons,"owner":row.get("owner"),"case_closed":False,"access_granted":False})
    return out
if __name__=="__main__":
    try:
        if len(sys.argv)!=2:raise ValueError("Usage: python3 scripts/review.py fixtures/sample.json")
        print(json.dumps(review(json.load(open(sys.argv[1],encoding="utf-8"))),indent=2))
    except (OSError,ValueError,TypeError) as exc:
        print("Input rejected: "+str(exc),file=sys.stderr);sys.exit(2)
