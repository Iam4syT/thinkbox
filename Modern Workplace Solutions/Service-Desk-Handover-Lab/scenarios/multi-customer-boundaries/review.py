"""Read-only synthetic ticket review. No service desk or tenant connection."""
import json, sys
REQUIRED={"id","tenant","service","impact","urgent","security","owner","next_update"}
def review(rows, tenant):
    if not isinstance(tenant,str) or not tenant.strip(): raise ValueError("tenant is required")
    if not isinstance(rows,list): raise ValueError("tickets must be a list")
    seen=set(); result=[]
    for row in rows:
        if not isinstance(row,dict) or set(row)!=REQUIRED: raise ValueError("invalid ticket schema")
        if any(not isinstance(row[k],str) or not row[k].strip() for k in ["id","tenant","service"]): raise ValueError("invalid text identity")
        if (row["tenant"],row["id"]) in seen: raise ValueError("duplicate ticket")
        seen.add((row["tenant"],row["id"]))
        if type(row["impact"]) is not int or not 1<=row["impact"]<=3: raise ValueError("impact must be 1..3")
        if any(type(row[k]) is not bool for k in ["urgent","security"]): raise ValueError("boolean flags required")
        if any(not isinstance(row[k],str) for k in ["owner","next_update"]): raise ValueError("invalid handover text")
        if row["tenant"]!=tenant: continue
        missing=[k for k in ["owner","next_update"] if not row[k].strip()]
        priority="P1" if row["security"] or (row["impact"]==3 and row["urgent"]) else "P2" if row["impact"]>=2 or row["urgent"] else "P3"
        action="security escalation" if row["security"] else "review missing handover" if missing else "analyst review"
        result.append({"id":row["id"],"tenant":tenant,"service":row["service"],"priority":priority,"missing":missing,"action":action,"human_review":True})
    return sorted(result,key=lambda r:(r["priority"],r["id"]))
if __name__=="__main__":
    try:
        rows=json.load(open(sys.argv[1],encoding="utf-8"));print(json.dumps(review(rows,sys.argv[2]),indent=2))
    except (ValueError,OSError,IndexError) as e:print(str(e),file=sys.stderr);sys.exit(2)
