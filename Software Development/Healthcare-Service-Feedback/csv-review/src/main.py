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

FIELDS=["id","category","impact","evidence","owner","status"]
def review(rows):
    seen=set(); cases=[]; counts={}
    for row in rows:
        if set(row)!=set(FIELDS) or any(v is None for v in row.values()):
            raise ValueError("Malformed case row")
        if not row["id"] or row["id"] in seen: raise ValueError("Missing or duplicate case id")
        seen.add(row["id"])
        if row["category"] not in {"access","report","workflow"}: raise ValueError("Unknown category")
        if row["impact"] not in {"single","multiple","safety"}: raise ValueError("Unknown impact")
        if row["status"] not in {"open","closed"}: raise ValueError("Unknown status")
        notes=[]
        if row["impact"]=="safety": notes.append("escalate immediately under local safety procedure")
        if not row["evidence"].strip(): notes.append("request reproduction evidence")
        if not row["owner"].strip(): notes.append("assign a responsible reviewer")
        if row["status"]=="closed" and not row["evidence"].strip(): notes.append("closure unsupported")
        counts[row["category"]]=counts.get(row["category"],0)+1
        cases.append({"id":row["id"],"category":row["category"],"review":notes or ["ready for human investigation"]})
    return {"case_count":len(cases),"category_counts":counts,"cases":cases,"automatic_resolution":False}


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
