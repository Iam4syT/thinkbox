"""Offline readiness checks. No network calls or account/device changes."""
import argparse,json
from pathlib import Path
ALLOWED_GROUPS={'staff','design','production-office'}
def assess(records):
    seen=set(); result=[]
    for r in records:
        issues=[]
        uid=r.get('id')
        if not uid or uid in seen: issues.append('missing-or-duplicate-id')
        seen.add(uid)
        if r.get('approval') is not True: issues.append('approval-missing')
        if r.get('action') not in ('join','leave'): issues.append('invalid-action')
        if r.get('action')=='join':
            if not r.get('licence'): issues.append('licence-missing')
            if not r.get('mfa_registered'): issues.append('mfa-not-registered')
            if not r.get('asset_id'): issues.append('asset-missing')
            if r.get('mdm_state')!='managed': issues.append('mdm-not-confirmed')
            if not set(r.get('groups',[])).issubset(ALLOWED_GROUPS): issues.append('unexpected-group')
        if r.get('action')=='leave':
            if not r.get('retention_review'): issues.append('retention-review-missing')
            if not r.get('asset_returned'): issues.append('asset-not-returned')
        result.append({'id':uid,'status':'review' if issues else 'ready-for-human-review','issues':issues})
    return result
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);args=p.parse_args()
    data=json.loads(Path(args.input).read_text())
    if not isinstance(data,list):raise ValueError('Input must be a list')
    output=assess(data);Path(args.output).parent.mkdir(parents=True,exist_ok=True);Path(args.output).write_text(json.dumps(output,indent=2)+'\n');print(json.dumps(output,indent=2))
