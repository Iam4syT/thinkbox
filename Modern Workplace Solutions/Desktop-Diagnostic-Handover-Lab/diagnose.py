"""Read synthetic desktop observations and prepare an escalation handover."""
import argparse,json
from pathlib import Path

def diagnose(s):
    if not isinstance(s,dict): raise ValueError('snapshot must be object')
    if not isinstance(s.get('asset_alias'),str) or not s['asset_alias']: raise ValueError('asset alias required')
    for k in ['adapter_up','dns_ok','tcp_443_ok','app_ok']:
        if s.get(k) is not None and type(s[k]) is not bool: raise ValueError(k+' must be boolean or null')
    free=s.get('disk_free_percent')
    if free is not None and (type(free) not in [int,float] or not 0<=free<=100): raise ValueError('invalid disk percentage')
    missing=[k for k in ['adapter_up','dns_ok','tcp_443_ok','app_ok','disk_free_percent'] if s.get(k) is None]
    checks=[]
    if s.get('adapter_up') is False: checks.append('Check cable or Wi-Fi using approved local procedure')
    if s.get('dns_ok') is False: checks.append('Record DNS failure; compare approved endpoint; escalate to network team')
    if s.get('tcp_443_ok') is False: checks.append('Record failed TCP test; inspect approved service status; no firewall change')
    if free is not None and free<10: checks.append('Low free space; request approved cleanup; do not delete user files')
    if s.get('app_ok') is False: checks.append('Record application symptom and escalate with reproduction steps')
    if missing: checks.append('Collect missing observations: '+', '.join(missing))
    if not checks: checks.append('No issue detected by these checks; confirm user task before closure')
    return {'asset_alias':s['asset_alias'],'observations':s,'checks':checks,'missing':missing,
            'state':'needs_review' if checks[0]!='No issue detected by these checks; confirm user task before closure' else 'checks_clear',
            'limitations':'Observations are not a root-cause diagnosis. No auto-remediation or clinical judgement.'}

def main():
    p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');a=p.parse_args()
    records=[diagnose(x) for x in json.loads(Path(a.input).read_text())]
    out=Path(a.output);tmp=out.with_suffix(out.suffix+'.tmp');tmp.write_text(json.dumps(records,indent=2)+'\n');tmp.replace(out)
    print(json.dumps(records,indent=2))
if __name__=='__main__':main()
