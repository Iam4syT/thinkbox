import csv, json, math
from pathlib import Path
from statistics import linear_regression, mean

def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader=csv.DictReader(f)
        if reader.fieldnames != ["hour", "demand_kw"]:
            raise ValueError("Expected hour,demand_kw header")
        rows=[]
        for r in reader:
            x,y=float(r["hour"]),float(r["demand_kw"])
            if not all(math.isfinite(v) and v >= 0 for v in (x,y)):
                raise ValueError("Values must be finite and non-negative")
            rows.append((x,y))
    if len(rows)<6 or any(b[0]<=a[0] for a,b in zip(rows,rows[1:])):
        raise ValueError("At least six rows with strictly increasing hours required")
    return rows

def evaluate(rows):
    cut=len(rows)*2//3
    train,test=rows[:cut],rows[cut:]
    slope,intercept=linear_regression([r[0] for r in train],[r[1] for r in train])
    trend=[slope*x+intercept for x,_ in test]
    actual=[y for _,y in test]
    persistence=[rows[i-1][1] for i in range(cut,len(rows))]
    return {"train_rows":len(train),"test_rows":len(test),"train_end_hour":train[-1][0],
      "slope":slope,"intercept":intercept,
      "persistence_mae_kw":mean(abs(a-b) for a,b in zip(actual,persistence)),
      "trend_mae_kw":mean(abs(a-b) for a,b in zip(actual,trend)),
      "limits":"Synthetic straight-line fixture. No real-world forecasting or energy saving established."}

def main():
    import argparse
    a=argparse.ArgumentParser();a.add_argument("--input",default="data/demand.csv");args=a.parse_args()
    result=evaluate(load(args.input));Path("outputs").mkdir(exist_ok=True)
    Path("outputs/metrics.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
if __name__ == "__main__":main()
