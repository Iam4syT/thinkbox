"""Offline identity plan with explicit approval, no live adapter."""
import argparse,json
from pathlib import Path
ALLOWED={'research','operations'}
def plan(people, accounts, approved=False):
    ids=[p.get('id') for p in people]
    if len(ids)!=len(set(ids)) or any(not isinstance(x,str) or not x for x in ids):raise ValueError('duplicate_or_missing_people_id')
    changes=[]
    # Only source-present people are considered; missing source records never imply termination.
    for person in people:
        uid=person['id'];state=person.get('state');team=person.get('team')
        if state not in {'active','left'}:raise ValueError('unknown_state')
        if state=='active' and team not in ALLOWED:raise ValueError('unknown_team')
        old=accounts.get(uid)
        desired=[] if state=='left' else [team]
        if old is None and state=='left':continue
        if old is None:changes.append(dict(id=uid,action='create',groups=desired))
        elif state=='left' and (old.get('enabled') or old.get('groups')):changes.append(dict(id=uid,action='disable',groups=[]))
        elif state=='active' and (not old.get('enabled') or sorted(old.get('groups',[]))!=desired):changes.append(dict(id=uid,action='reconcile',groups=desired))
    return dict(approved=approved is True, mode='local_simulation', changes=changes)
def apply_local(plan_data,accounts):
    if plan_data.get('approved') is not True:raise PermissionError('approval_required')
    updated=json.loads(json.dumps(accounts))
    for change in plan_data['changes']:
        updated[change['id']]=dict(enabled=change['action']!='disable',groups=change['groups'])
    return updated
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--approve-local',action='store_true');args=parser.parse_args()
    people=json.loads(Path('templates/people.json').read_text());accounts=json.loads(Path('templates/accounts.json').read_text())
    result=plan(people,accounts,args.approve_local);Path('evidence').mkdir(exist_ok=True)
    Path('evidence/plan.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
    if args.approve_local:Path('evidence/simulated-accounts.json').write_text(json.dumps(apply_local(result,accounts),indent=2)+'\n')
if __name__=='__main__':main()
