"""Synthetic service desk triage and handover. No live ITSM connection."""
import argparse, json
from pathlib import Path

def classify(t):
    if not isinstance(t, dict): raise ValueError('ticket must be an object')
    if not isinstance(t.get('id'),str) or not t['id']: raise ValueError('id required')
    for k in ['critical_service', 'workaround']:
        if type(t.get(k)) is not bool: raise ValueError(k+' must be boolean')
    if type(t.get('users')) is not int or t['users']<1: raise ValueError('users must be positive integer')
    if t.get('channel') not in ['phone','portal','in-person']: raise ValueError('channel invalid')
    if not isinstance(t.get('summary'),str) or not t['summary'].strip(): raise ValueError('summary required')
    # Demonstration policy only, not an NHS clinical priority rule.
    priority='P1' if t['critical_service'] and not t['workaround'] else ('P2' if t['users']>=5 else 'P3')
    return {**t,'priority':priority,'state':'new','owner':None,'history':[],
            'next_action':'Human confirms service impact, approved priority and escalation route'}

def transition(t,state,note,owner=None,verified=False):
    allowed={'new':['assigned'],'assigned':['escalated','resolved'],'escalated':['resolved'],'resolved':['closed'],'closed':[]}
    if state not in allowed[t['state']]: raise ValueError('invalid lifecycle transition')
    if not note.strip(): raise ValueError('note required')
    if state=='assigned' and not owner: raise ValueError('owner required')
    if state in ['resolved','closed'] and not verified: raise ValueError('explicit user verification required')
    result={**t,'state':state,'history':t['history']+[{'state':state,'note':note,'verified':verified}]}
    if owner: result['owner']=owner
    return result

def main():
    ap=argparse.ArgumentParser(); subs=ap.add_subparsers(dest='cmd',required=True)
    p=subs.add_parser('triage');p.add_argument('input');p.add_argument('output')
    p=subs.add_parser('update');p.add_argument('file');p.add_argument('id');p.add_argument('state');p.add_argument('--note',required=True);p.add_argument('--owner');p.add_argument('--verified',action='store_true')
    a=ap.parse_args()
    if a.cmd=='triage':
        raw=json.loads(Path(a.input).read_text()); records=[classify(x) for x in raw]
        if len({x['id'] for x in records}) != len(records): raise ValueError('duplicate id')
        records.sort(key=lambda x:(x['priority'],x['id']));out=Path(a.output)
    else:
        out=Path(a.file); records=json.loads(out.read_text()); matches=[x for x in records if x['id']==a.id]
        if len(matches)!=1: raise ValueError('id must match exactly one record')
        records=[transition(x,a.state,a.note,a.owner,a.verified) if x['id']==a.id else x for x in records]
    tmp=out.with_suffix(out.suffix+'.tmp');tmp.write_text(json.dumps(records,indent=2)+'\n');tmp.replace(out)
    print(json.dumps(records,indent=2))
if __name__=='__main__': main()
