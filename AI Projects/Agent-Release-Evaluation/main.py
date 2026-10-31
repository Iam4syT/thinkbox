"""Validate synthetic agent traces against an explicit release policy; no LLM call."""
import json,argparse,math
ALLOWED={"search","lookup"}
FIELDS={"id","tools","citations","allowed_sources","human_review","tokens_in","tokens_out","latency_ms","quality"}
def evaluate(row):
    if not isinstance(row,dict) or set(row)!=FIELDS: raise ValueError("Exact trace fields required")
    if not isinstance(row["id"],str) or not row["id"]: raise ValueError("Trace id required")
    for k in ["tools","citations","allowed_sources"]:
        if not isinstance(row[k],list) or any(not isinstance(v,str) for v in row[k]): raise ValueError("List of strings required: "+k)
    if type(row["human_review"]) is not bool: raise ValueError("Boolean review required")
    for k in ["tokens_in","tokens_out","latency_ms"]:
        if type(row[k]) is not int or row[k]<0: raise ValueError("Nonnegative integer required: "+k)
    if type(row["quality"]) not in [int,float] or not math.isfinite(row["quality"]) or not 0<=row["quality"]<=1: raise ValueError("Quality range 0..1 required")
    failed=[]
    if not set(row["tools"])<=ALLOWED: failed.append("tool_allowlist")
    if not row["citations"] or not set(row["citations"])<=set(row["allowed_sources"]): failed.append("citation_scope")
    if not row["human_review"]: failed.append("human_review")
    if row["quality"]<.8: failed.append("quality")
    if row["latency_ms"]>2000: failed.append("latency_budget")
    if row["tokens_in"]+row["tokens_out"]>1000: failed.append("token_budget")
    # Illustrative tariff only: NOT a provider price or real usage measurement.
    cost=(row["tokens_in"]*1+row["tokens_out"]*4)/1000000
    return dict(id=row["id"],status="HOLD" if failed else "READY_FOR_REVIEW",failed=failed,illustrative_cost_units=cost)
def batch(rows):
    if not isinstance(rows,list) or not rows: raise ValueError("Nonempty trace list required")
    ids=[r.get("id") for r in rows if isinstance(r,dict)]
    if len(ids)!=len(set(ids)): raise ValueError("Duplicate trace id")
    return [evaluate(r) for r in rows]
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--data",default="data/traces.json");a=p.parse_args()
    try: print(json.dumps(batch(json.load(open(a.data))),indent=2))
    except (ValueError,OSError) as e: raise SystemExit("INVALID INPUT: "+str(e))
