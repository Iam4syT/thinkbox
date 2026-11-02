import argparse,json,math,hashlib
from pathlib import Path
def number(v):
    if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v):raise ValueError('finite number required')
    return float(v)
def evaluate(rows,split=10):
    if not isinstance(rows,list) or len(rows)<6 or not isinstance(split,int) or not 2<=split<=len(rows)-4:raise ValueError('split needs training and at least four holdout rows')
    last=-1
    for r in rows:
        if set(r)!={'time','x','y','group'}:raise ValueError('schema')
        t=number(r['time']);number(r['x']);number(r['y'])
        if t<=last:raise ValueError('time must strictly increase')
        if r['group'] not in ['a','b']:raise ValueError('synthetic group a or b required')
        last=t
    train,test=rows[:split],rows[split:]
    xm=sum(r['x'] for r in train)/len(train);ym=sum(r['y'] for r in train)/len(train)
    den=sum((r['x']-xm)**2 for r in train)
    if den==0:raise ValueError('constant training feature')
    slope=sum((r['x']-xm)*(r['y']-ym) for r in train)/den;intercept=ym-slope*xm
    errors=[abs(r['y']-(slope*r['x']+intercept)) for r in test]
    model=sum(errors)/len(test);baseline=sum(abs(r['y']-ym) for r in test)/len(test)
    groups={g:[e for r,e in zip(test,errors) if r['group']==g] for g in ['a','b']}
    if any(len(v)<2 for v in groups.values()):raise ValueError('need two holdout rows per group')
    gm={g:sum(v)/len(v) for g,v in groups.items()};gap=abs(gm['a']-gm['b'])
    reasons=[]
    if model>=baseline:reasons.append('does_not_beat_baseline')
    if model>5:reasons.append('overall_error')
    if gap>5:reasons.append('group_error_gap')
    return dict(scope='synthetic_local_only',train_n=len(train),test_n=len(test),slope=slope,intercept=intercept,model_mae=model,baseline_mae=baseline,group_mae=gm,group_gap=gap,reasons=reasons,decision='hold' if reasons else 'review',input_sha256=hashlib.sha256(json.dumps(rows,sort_keys=True,allow_nan=False).encode()).hexdigest())
def fixture(shift=0):return [dict(time=i,x=i,y=2*i+10+(shift if i>=10 and i%2 else 0),group='b' if i%2 else 'a') for i in range(16)]
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--group-shift',type=float,default=0);a.add_argument('--output',type=Path);args=a.parse_args();result=evaluate(fixture(args.group_shift))
    text=json.dumps(result,indent=2,allow_nan=False);print(text)
    if args.output:args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(text+'\n')
