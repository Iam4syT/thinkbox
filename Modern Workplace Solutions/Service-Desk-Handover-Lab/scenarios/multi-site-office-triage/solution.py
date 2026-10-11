"""Synthetic offline policy exercise. No remote access or repair."""
import json, argparse
from collections import Counter
def analyse(rows):
    if not isinstance(rows, list) or not rows: raise ValueError('Expected non-empty list')
    seen=set();out=[]
    for r in rows:
        if not isinstance(r,dict): raise ValueError('Expected object')
        for k in ['id','site','category','summary','owner']:
            if not isinstance(r.get(k),str) or not r[k].strip(): raise ValueError('Missing '+k)
        if r['id'] in seen: raise ValueError('Duplicate id')
        seen.add(r['id'])
        if r['category'] not in ['access','mail','printing']: raise ValueError('Unknown category')
        if type(r.get('users')) is not int or r['users']<1: raise ValueError('Invalid users')
        for k in ['critical','workaround','security_concern']:
            if type(r.get(k)) is not bool: raise ValueError('Invalid '+k)
        if r['security_concern']: priority='P1';route='Security review; preserve evidence, do not change settings'
        elif r['critical'] and not r['workaround']: priority='P1';route='Specialist escalation with confirmed impact'
        elif r['users']>=5: priority='P2';route='Service desk investigation and user update'
        else: priority='P3';route='Service desk investigation and user update'
        checks={'access':'Confirm identity and approved access; record sign-in error; do not ask for passwords',
          'mail':'Record scope and error; test permitted web access; escalate beyond authority',
          'printing':'Check power/cable/selected queue and harmless test page on authorised device'}
        out.append(dict(id=r['id'],priority=priority,owner=r['owner'],site=r['site'],category=r['category'],
          next_action=route,diagnostic_check=checks[r['category']],user_update='Explain next check and agree next update',state='open'))
    out.sort(key=lambda r:(r['priority'],r['id']))
    return dict(tickets=out,repeat_categories={k:v for k,v in sorted(Counter(r['category'] for r in rows).items()) if v>1},
      policy='Illustrative only; not an employer SLA',mode='offline_advisory')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');a=p.parse_args()
    try: result=analyse(json.load(open(a.input)))
    except (ValueError,OSError) as e:p.exit(2,str(e)+'\n')
    with open(a.output,'w') as f:json.dump(result,f,indent=2);f.write('\n')
