"""Synthetic endpoint handover review; no live-device changes."""
import csv,json,sys
from pathlib import Path
FIELDS={"asset","approved","encrypted","patched","m365_test","owner_recorded"}
def evaluate(rows):
    result=[];seen=set()
    for r in rows:
        if set(r)!=FIELDS: raise ValueError("columns must match fixture schema")
        if not r["asset"] or r["asset"] in seen: raise ValueError("empty or duplicate asset")
        seen.add(r["asset"])
        if any(r[k] not in {"yes","no","unknown"} for k in FIELDS-{"asset"}): raise ValueError("expected yes/no/unknown")
        missing=sorted(k for k in FIELDS-{"asset"} if r[k]!="yes")
        result.append({"asset":r["asset"],"status":"REVIEW" if missing else "CHECKLIST_COMPLETE", "missing":missing,"action":"Human confirms evidence before handover; no automatic changes"})
    return result
if __name__=="__main__":
    try:
        with Path(sys.argv[1]).open(newline="",encoding="utf-8") as f: result=evaluate(list(csv.DictReader(f)))
        print(json.dumps(result,indent=2))
    except (ValueError,OSError,IndexError) as e:
        print("Input rejected: "+str(e),file=sys.stderr);sys.exit(2)
