"""Offline synthetic feedback report. Does not decide clinical priority."""
import argparse, json
from collections import Counter
from pathlib import Path

def analyse(rows):
    if not isinstance(rows,list): raise ValueError("Input must be a list")
    seen=set(); themes=Counter(); overdue=[]; review=[]
    for row in rows:
        if not isinstance(row,dict): raise ValueError("Each ticket must be an object")
        tid=row.get("id")
        if not isinstance(tid,str) or not tid.strip() or tid in seen: raise ValueError("Missing or duplicate ticket id")
        seen.add(tid)
        theme=row.get("theme")
        if theme not in {"access","report","referral","unknown"}: raise ValueError("Unsupported theme")
        for key in ("age_hours","target_hours"):
            value=row.get(key)
            if type(value) not in (int,float) or value<0: raise ValueError("Hours must be non-negative numbers")
        if row["target_hours"]==0: raise ValueError("Target must be greater than zero")
        if type(row.get("safety_concern")) is not bool: raise ValueError("Safety concern must be boolean")
        themes[theme]+=1
        if row["age_hours"]>row["target_hours"]: overdue.append(tid)
        if row["safety_concern"] or theme=="unknown": review.append(tid)
    return {"ticket_count":len(rows),"themes":dict(sorted(themes.items())),"overdue_ids":sorted(overdue),"human_review_ids":sorted(review),"boundary":"Human reviews all recommendations; local targets are illustrative, not vendor SLAs"}

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--input",required=True);parser.add_argument("--output",required=True);args=parser.parse_args()
    try: result=analyse(json.loads(Path(args.input).read_text()))
    except (ValueError,OSError) as exc: parser.exit(2,"Input rejected: "+str(exc)+"\n")
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n");print(json.dumps(result,indent=2))
if __name__=="__main__": main()
