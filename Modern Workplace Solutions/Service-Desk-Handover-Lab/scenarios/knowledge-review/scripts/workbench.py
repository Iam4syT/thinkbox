import json,sys
from pathlib import Path
from datetime import date

def evaluate(rows,today):
    today=date.fromisoformat(today)
    if not isinstance(rows,list):raise ValueError("Expected a list")
    out=[];seen=set()
    for r in rows:
        ident=r.get("id")
        if not isinstance(ident,str) or not ident.strip() or ident in seen:raise ValueError("Missing or duplicate id")
        seen.add(ident)
        for k in ("owner","symptom","safe_steps","verification","escalation"):
            if not isinstance(r.get(k),str):raise ValueError("Invalid text "+k)
        if type(r.get("reviewed")) is not bool:raise ValueError("Invalid reviewed")
        due=date.fromisoformat(r["review_due"])
        missing=[k for k in ("owner","symptom","safe_steps","verification","escalation") if not r[k].strip()]
        reasons=missing+([] if r["reviewed"] else ["approval"])+(["overdue"] if due<today else [])
        out.append({"id":ident,"status":"hold" if reasons else "ready","reasons":reasons})
    return out
if __name__=="__main__":
    try:print(json.dumps(evaluate(json.loads(Path(sys.argv[1]).read_text()),sys.argv[2]),indent=2))
    except (ValueError,KeyError,IndexError,TypeError,OSError) as e:print("Input error: "+str(e),file=sys.stderr);sys.exit(2)
