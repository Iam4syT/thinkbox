"""Offline package contract checker. Never executes install commands or calls a tenant."""
import json
from pathlib import Path

def check(plan):
    required = {'app','version','architecture','pilot','install','uninstall','detection'}
    if not required.issubset(plan): raise ValueError('Missing package contract field')
    if not all(isinstance(plan[k],str) and plan[k].strip() for k in required - {'pilot'}): raise ValueError('Empty contract field')
    if plan['architecture'] not in {'x64','arm64'}: raise ValueError('Unsupported test architecture')
    pilot=plan['pilot']
    if not isinstance(pilot,list) or not 1 <= len(pilot) <= 2: raise ValueError('Pilot must contain one or two test devices')
    if any(not isinstance(x,str) or not x.startswith('LAB-') for x in pilot) or len(set(pilot))!=len(pilot): raise ValueError('Invalid or duplicate lab device')
    return {'app':plan['app'],'version':plan['version'],'pilot':pilot,'mode':'offline contract only','native_validated':False}

def detect(expected, observed):
    return observed == expected

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('plan');args=p.parse_args()
    print(json.dumps(check(json.loads(Path(args.plan).read_text(encoding="utf-8-sig"))),indent=2))
