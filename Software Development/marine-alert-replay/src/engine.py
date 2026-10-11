import json, math
from pathlib import Path

def assess(row):
    # Teaching thresholds only. Return advice; never operate equipment.
    values=[]
    for key in ["age_seconds","temperature_c","speed_knots"]:
        value=row.get(key)
        if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or value<0:
            return {"recommendation":"HOLD","reason":"invalid input","actuation":False}
        values.append(value)
    age,temp,speed=values
    if age>5:return {"recommendation":"HOLD","reason":"stale input","actuation":False}
    if temp>80 or speed>12:return {"recommendation":"HOLD","reason":"teaching limit exceeded","actuation":False}
    return {"recommendation":"REVIEW","reason":"within teaching limits","actuation":False}

def main():
    import argparse
    a=argparse.ArgumentParser();a.add_argument("--input",default="data/scenarios.json");args=a.parse_args()
    rows=json.loads(Path(args.input).read_text())
    if not isinstance(rows,list) or not all(isinstance(x,dict) for x in rows):raise ValueError("Expected a list of records")
    out=[]
    for row in rows:
        result=assess(row);result["id"]=row.get("id");result["matches_expected"]=result["recommendation"]==row.get("expected");out.append(result)
    Path("outputs").mkdir(exist_ok=True);Path("outputs/replay.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))
if __name__ == "__main__":main()
