"""Synthetic one-feature least-squares training and chronological holdout gate."""
import argparse,json,math
DATA=[{'day':i,'feature':i,'target':2*i+3} for i in range(1,13)]
def train(rows):
 if len(rows)<2:raise ValueError('Need at least two training rows')
 if any(not math.isfinite(float(r[k])) for r in rows for k in ('feature','target')):raise ValueError('Non-finite value')
 x=[r['feature'] for r in rows];y=[r['target'] for r in rows];xm=sum(x)/len(x);ym=sum(y)/len(y);den=sum((v-xm)**2 for v in x)
 if den==0:raise ValueError('No feature variation')
 slope=sum((a-xm)*(b-ym) for a,b in zip(x,y))/den
 return slope,ym-slope*xm
def rmse(actual,predicted):
 if not actual or len(actual)!=len(predicted):raise ValueError('Invalid prediction length')
 if any(not math.isfinite(float(v)) for v in actual+predicted):raise ValueError('Non-finite prediction')
 return math.sqrt(sum((a-p)**2 for a,p in zip(actual,predicted))/len(actual))
def run(rows=DATA,cut=8,drift=0):
 if not 2<=cut<len(rows):raise ValueError('Invalid split')
 if any(a['day']>=b['day'] for a,b in zip(rows,rows[1:])):raise ValueError('Days must strictly increase')
 train_rows,test=rows[:cut],rows[cut:];slope,intercept=train(train_rows)
 actual=[r['target']+drift for r in test];pred=[slope*r['feature']+intercept for r in test]
 baseline=[train_rows[-1]['target']]*len(test)
 model_error=rmse(actual,pred);baseline_error=rmse(actual,baseline)
 return {'train_n':len(train_rows),'holdout_n':len(test),'slope':slope,'intercept':intercept,'model_rmse':model_error,'baseline_rmse':baseline_error,'release':'pass' if model_error<baseline_error and model_error<=2 else 'hold','threshold':2,'limits':'Deterministic synthetic linear fixture. No real forecast performance, cloud deployment or operational monitoring established.'}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--drift',type=float,default=0);args=p.parse_args();print(json.dumps(run(drift=args.drift),indent=2))
