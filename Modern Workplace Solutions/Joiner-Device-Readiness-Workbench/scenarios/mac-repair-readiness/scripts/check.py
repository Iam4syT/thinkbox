"""Offline checklist review; no device, room or cloud access."""
import json, sys
CHECKS = ['identity_confirmed', 'asset_matched', 'enrolment_reviewed', 'encryption_checked', 'handover_tested']
IDENTIFIER = 'asset_id'
def review(data):
    if not isinstance(data, dict): raise ValueError('Expected one object')
    for key in (IDENTIFIER, 'owner'):
        if not isinstance(data.get(key),str) or not data[key].strip(): raise ValueError('Missing '+key)
    checks=data.get('checks')
    if not isinstance(checks,dict) or set(checks)!=set(CHECKS): raise ValueError('Missing or unexpected checks')
    if any(type(v) is not str or v not in ('pass','fail','unknown') for v in checks.values()):
        raise ValueError('Checks must be pass, fail or unknown')
    issues=[k for k in CHECKS if checks[k]!='pass']
    status='hold' if 'fail' in checks.values() else ('review' if issues else 'ready_for_human_review')
    return {'id':data[IDENTIFIER], 'status':status, 'issues':issues,
      'limits':'Supplied observations only. No automated diagnosis, live verification or approval.'}
if __name__=='__main__':
    try:
        with open(sys.argv[1],encoding='utf-8') as f: d=json.load(f)
        print(json.dumps(review(d),indent=2))
    except (ValueError,TypeError,IndexError,OSError) as e:
        print('Input error: '+str(e),file=sys.stderr);sys.exit(2)
