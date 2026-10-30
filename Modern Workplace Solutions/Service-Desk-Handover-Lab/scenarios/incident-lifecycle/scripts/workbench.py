import json,sys
from pathlib import Path

def evaluate(rows):
    if not isinstance(rows,list):raise ValueError("Expected a list")
    out=[];seen=set()
    for r in rows:
        ident=r.get("id")
        if not isinstance(ident,str) or not ident.strip() or ident in seen:raise ValueError("Missing or duplicate id")
        seen.add(ident)
        if r.get("impact") not in ("single","team","organisation") or r.get("urgency") not in ("normal","high"):raise ValueError("Invalid impact or urgency")
        if type(r.get("age_hours")) not in (int,float) or not 0<=r["age_hours"]<=8760:raise ValueError("Invalid age_hours")
        if r.get("status") not in ("open","resolved"):raise ValueError("Invalid status")
        for k in ("outside_scope","user_confirmed","followup_done"):
            if type(r.get(k)) is not bool:raise ValueError("Invalid boolean "+k)
        priority="P1" if r["impact"]=="organisation" and r["urgency"]=="high" else "P2" if r["urgency"]=="high" or r["impact"]=="team" else "P3"
        if r["status"]=="resolved":action="close" if r["user_confirmed"] and r["followup_done"] else "follow_up"
        elif r["outside_scope"] or r["age_hours"]>=4:action="escalate"
        else:action="investigate"
        out.append({"id":ident,"priority":priority,"action":action})
    return out
if __name__=="__main__":
    try:print(json.dumps(evaluate(json.loads(Path(sys.argv[1]).read_text())),indent=2))
    except (ValueError,KeyError,IndexError,TypeError,OSError) as e:print("Input error: "+str(e),file=sys.stderr);sys.exit(2)
