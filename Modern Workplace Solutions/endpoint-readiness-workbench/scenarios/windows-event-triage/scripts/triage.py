"""Read synthetic events and propose handover; no device remediation."""
import json
from datetime import datetime,timezone
from pathlib import Path

def triage(events, now, max_age_minutes=60):
    now=datetime.fromisoformat(now)
    if now.tzinfo is None:raise ValueError('Reference time needs timezone')
    if max_age_minutes <= 0:raise ValueError('Invalid lookback')
    seen=set();groups={};excluded=0
    for e in events:
        if not {'record_id','host','provider','event_id','time','level'}.issubset(e):raise ValueError('Missing event field')
        if not isinstance(e['record_id'],int) or not isinstance(e['event_id'],int):raise ValueError('IDs must be integers')
        if e['level'] not in {'Information','Warning','Error','Critical'}:raise ValueError('Unknown severity')
        key=(e['host'],e['provider'],e['record_id'])
        if key in seen:raise ValueError('Duplicate event record')
        seen.add(key)
        if not e['host'].startswith('LAB-'):raise ValueError('Only synthetic lab hosts accepted')
        t=datetime.fromisoformat(e['time'])
        if t.tzinfo is None:raise ValueError('Event time needs timezone')
        age=(now-t).total_seconds()/60
        if age<0:raise ValueError('Future event')
        if age>max_age_minutes or e['level']=='Information':excluded+=1;continue
        k=(e['host'],e['provider'],e['event_id']);g=groups.setdefault(k,{'host':e['host'],'provider':e['provider'],'event_id':e['event_id'],'count':0,'owner':'service desk','action':'investigate within authority','urgent':False})
        g['count']+=1
        if e['provider']!='WorkplaceLab' or e['level']=='Critical':g.update(owner='specialist review',action='escalate with scope and evidence; no automatic fix')
        if e['level']=='Critical':g['urgent']=True
    return {'mode':'offline synthetic triage','groups':list(groups.values()),'excluded':excluded,'remediation_performed':False}

if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('events');p.add_argument('--now',required=True);a=p.parse_args()
 print(json.dumps(triage(json.loads(Path(a.events).read_text(encoding="utf-8-sig")),a.now),indent=2))
