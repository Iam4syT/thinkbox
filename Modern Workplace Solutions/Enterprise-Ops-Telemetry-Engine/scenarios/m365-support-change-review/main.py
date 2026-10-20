"""Synthetic ticket trends and change acceptance. No live ticket or tenant integration."""
import argparse,json
from collections import Counter
from pathlib import Path

def analyse(data):
    rows=data["tickets"]; ids=[r["id"] for r in rows]
    if len(ids)!=len(set(ids)): raise ValueError("Duplicate ticket ID")
    groups=Counter()
    for row in rows:
        if row["service"] not in {"Teams","Exchange","SharePoint","Copilot"} or not isinstance(row["symptom"],str) or not row["symptom"].strip(): raise ValueError("Invalid ticket")
        groups[(row["service"],row["symptom"])]+=1
    c=data["change"]
    for key in ("approved","positive_test","negative_test","rollback_test"):
        if c[key] not in {"pass","fail","unknown"}: raise ValueError("Invalid change evidence")
    missing=[key for key in ("approved","positive_test","negative_test","rollback_test") if c[key]!="pass"]
    return {"recurring":[{"service":s,"symptom":t,"count":n} for (s,t),n in sorted(groups.items()) if n>=2],"change_status":"ready_for_human_review" if not missing else "hold", "unresolved":missing,"deployment_authorised":False}

if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("--input",default="fixtures.json"); p.add_argument("--output",default="report.json"); a=p.parse_args()
    try: result=analyse(json.loads(Path(a.input).read_text())); Path(a.output).write_text(json.dumps(result,indent=2)+"\n")
    except (ValueError,KeyError,TypeError,OSError) as e: p.exit(2,str(e)+"\n")
