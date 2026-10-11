"""Evidence completeness aid; never authorises a clinical launch."""
import argparse,json
from pathlib import Path
REQUIRED=("training","support_owner","rollback","test_evidence")
def check(data):
    if not isinstance(data,dict) or not isinstance(data.get("launch_id"),str) or not data["launch_id"].strip(): raise ValueError("Named launch object required")
    checks=data.get("checks")
    if not isinstance(checks,dict): raise ValueError("Checks object required")
    missing=[]
    for name in REQUIRED:
        value=checks.get(name)
        if not isinstance(value,dict) or value.get("status") not in ("passed","pending","failed"): raise ValueError("Every required check needs a valid status")
        if value["status"]!="passed" or not isinstance(value.get("evidence"),str) or not value["evidence"].strip(): missing.append(name)
    return {"launch_id":data["launch_id"],"decision":"ready-for-human-review" if not missing else "hold","missing_or_failed":missing,"boundary":"References are not authenticated; authorised humans verify evidence and decide go-live"}
def main():
    p=argparse.ArgumentParser();p.add_argument("--input",required=True);p.add_argument("--output",required=True);a=p.parse_args()
    try: result=check(json.loads(Path(a.input).read_text()))
    except (ValueError,OSError) as exc:p.exit(2,"Input rejected: "+str(exc)+"\n")
    out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n");print(json.dumps(result,indent=2))
if __name__=="__main__":main()
