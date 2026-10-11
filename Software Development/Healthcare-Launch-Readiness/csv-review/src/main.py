import argparse, csv, json
from pathlib import Path

def load(path, fields):
    with Path(path).open(newline="", encoding="utf-8") as f:
        reader=csv.DictReader(f)
        if not reader.fieldnames or set(reader.fieldnames) != set(fields):
            raise ValueError("CSV columns do not match the documented schema")
        rows=list(reader)
    if not rows:
        raise ValueError("CSV contains no records")
    return rows

FIELDS=["check","status","evidence","owner","rollback"]
REQUIRED={"access","workflow","reporting","communications"}
def review(rows):
    seen=set(); blockers=[]
    for row in rows:
        if set(row)!=set(FIELDS) or any(v is None for v in row.values()): raise ValueError("Malformed launch row")
        name=row["check"]
        if name not in REQUIRED or name in seen: raise ValueError("Unknown or duplicate check")
        seen.add(name)
        if row["status"] not in {"pass","fail","unrun"}: raise ValueError("Unknown status")
        if row["status"]!="pass": blockers.append(name+": "+row["status"])
        for field in ["evidence","owner","rollback"]:
            if not row[field].strip(): blockers.append(name+": missing "+field)
    for name in sorted(REQUIRED-seen): blockers.append(name+": missing check")
    return {"decision":"HOLD" if blockers else "READY FOR HUMAN REVIEW","blockers":blockers,"check_count":len(rows),"deployment_performed":False}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--input", default="data/sample.csv")
    parser.add_argument("--output", default="output/report.json")
    args=parser.parse_args()
    result=review(load(args.input, FIELDS))
    out=Path(args.output); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2))

if __name__ == "__main__": main()
