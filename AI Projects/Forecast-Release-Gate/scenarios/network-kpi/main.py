"""Synthetic ordered network KPI regression, never a network controller."""
import argparse, json, math
from statistics import mean
DATA=[{'time':i,'load':float(i),'latency_ms':2.0*i+10.0} for i in range(1,25)]
def validate(rows,cut):
    if not isinstance(cut,int) or cut<3 or cut>=len(rows):raise ValueError('invalid temporal split')
    for r in rows:
        if set(r)!={'time','load','latency_ms'}:raise ValueError('schema mismatch')
        if any(type(r[k]) not in (int,float) or not math.isfinite(r[k]) for k in r):raise ValueError('finite numeric data required')
        if r['load']<0 or r['latency_ms']<0:raise ValueError('negative KPI')
    if any(b['time']<=a['time'] for a,b in zip(rows,rows[1:])):raise ValueError('time must strictly increase')
def evaluate(rows=DATA,cut=16):
    validate(rows,cut);train=rows[:cut];test=rows[cut:]
    x=mean(r['load'] for r in train);y=mean(r['latency_ms'] for r in train)
    den=sum((r['load']-x)**2 for r in train)
    if den==0:raise ValueError('constant training feature')
    slope=sum((r['load']-x)*(r['latency_ms']-y) for r in train)/den
    intercept=y-slope*x
    model=mean(abs(slope*r['load']+intercept-r['latency_ms']) for r in test)
    baseline=mean(abs(train[-1]['latency_ms']-r['latency_ms']) for r in test)
    if not all(math.isfinite(v) for v in (slope,intercept,model,baseline)):raise ValueError('numeric overflow')
    return {'schema_version':1,'model_id':'synthetic-kpi-v1','train_n':len(train),'test_n':len(test),'slope':slope,'intercept':intercept,'model_mae_ms':model,'baseline_mae_ms':baseline,'review':'eligible_for_review' if model<baseline and model<=3 else 'hold','scope':'synthetic_local_only'}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--drift',type=float,default=0);a=p.parse_args()
    rows=[dict(r) for r in DATA]
    for row in rows[16:]:row['latency_ms']+=a.drift
    print(json.dumps(evaluate(rows),indent=2,allow_nan=False))
