"""Demonstration eligibility from synthetic metadata, not live permission enforcement."""
import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from core_engine.policy import assess_record

def review(d):
    if not isinstance(d,dict) or not isinstance(d.get('records'),list) or not d['records']:
        raise ValueError('records must be a non-empty list')
    rows=[]
    for record in d['records']:
        if not isinstance(record,dict) or not isinstance(record.get('id'),str) or not record['id']:
            raise ValueError('each record needs a non-empty string id')
        rows.append({'id':record['id'],**assess_record(record)})
    if len({r['id'] for r in rows})!=len(rows): raise ValueError('duplicate ids')
    checks=d.get('checks',{})
    names=('owner_approved','licence_checked','baseline_defined')
    if not isinstance(checks,dict): raise ValueError('checks must be an object')
    if any(k in checks and type(checks[k]) is not bool for k in names): raise ValueError('check values must be boolean')
    ready=all(r['decision']=='allowed' for r in rows) and all(checks.get(k) is True for k in names)
    return {'status':'bounded_demo_candidate' if ready else 'review_before_demo','records':rows,
      'limits':'Metadata policy only. No real identities, retrieval, AI generation, tenant integration or automatic access changes.',
      'next_step':'Owner reviews actual access and baseline; run a permitted pilot and measure quality before any value claim.'}
if __name__=='__main__':
    try:
        with open(sys.argv[1],encoding='utf-8') as f: data=json.load(f)
        print(json.dumps(review(data),indent=2))
    except (ValueError,KeyError,IndexError,OSError,TypeError) as e:
        print('Input error: '+str(e),file=sys.stderr);sys.exit(2)
