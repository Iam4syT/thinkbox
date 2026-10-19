"""Synthetic service-desk routing; no ITSM or tenant connection."""
import csv,json,sys
from pathlib import Path
FIELDS={"id","service","impact","urgency","age_minutes"}
def evaluate(rows):
    output=[];seen=set()
    for r in rows:
        if set(r)!=FIELDS: raise ValueError("columns must match fixture schema")
        if not r["id"] or r["id"] in seen: raise ValueError("empty or duplicate id")
        seen.add(r["id"])
        if r["service"] not in {"m365","identity","device","unknown"}: raise ValueError("unknown service")
        if r["impact"] not in {"one","many"} or r["urgency"] not in {"normal","high"}: raise ValueError("invalid impact or urgency")
        age=int(r["age_minutes"])
        if age<0: raise ValueError("negative ticket age")
        priority="P1" if r["impact"]=="many" and r["urgency"]=="high" else "P2" if r["urgency"]=="high" else "P3"
        # Teaching thresholds only, never claimed as an employer SLA.
        limit={"P1":15,"P2":60,"P3":240}[priority]
        route={"m365":"M365 support","identity":"Access team","device":"Device team","unknown":"Human triage"}[r["service"]]
        output.append({"id":r["id"],"priority":priority,"route":route,"review_due":age>=limit,"action":"Human review; no automatic remediation"})
    return output
if __name__=="__main__":
    try:
        with Path(sys.argv[1]).open(newline="",encoding="utf-8") as f: result=evaluate(list(csv.DictReader(f)))
        print(json.dumps(result,indent=2))
    except (ValueError,OSError,IndexError) as e:
        print("Input rejected: "+str(e),file=sys.stderr);sys.exit(2)
