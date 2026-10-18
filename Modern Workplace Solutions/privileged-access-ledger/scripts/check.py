"""Offline evidence ledger; does not grant, revoke or enforce Entra permissions."""
import json,sys
from pathlib import Path
from datetime import datetime
def stamp(s):
    if not isinstance(s,str): raise ValueError('Timestamp must be text')
    d=datetime.fromisoformat(s.replace('Z','+00:00'))
    if d.utcoffset() is None: raise ValueError('Timestamp needs timezone')
    return d
def evaluate(d):
    if not isinstance(d,dict) or not isinstance(d.get('requests'),list) or not d['requests']: raise ValueError('Nonempty requests list required')
    now=stamp(d['now']);findings=[];seen=set()
    for r in d['requests']:
        if not isinstance(r,dict):raise ValueError('Request must be object')
        for k in ['id','role','requester','approver']:
            if not isinstance(r.get(k),str) or not r[k].strip():raise ValueError('Missing '+k)
        if r['id'] in seen:raise ValueError('Duplicate request id')
        seen.add(r['id'])
        for k in ['eligible','approved','mfa']:
            if type(r.get(k)) is not bool:raise ValueError(k+' must be boolean')
        start,end=stamp(r['start']),stamp(r['end'])
        if end<=start:raise ValueError('End must follow start')
        if r['role']!='User Administrator':result='ROLE_REVIEW'
        elif not r['eligible'] or not r['approved'] or not r['mfa'] or r['requester']==r['approver']:result='DENY'
        elif (end-start).total_seconds()>3600:result='DURATION_REVIEW'
        elif now<start:result='NOT_STARTED'
        elif now>=end:result='EXPIRED'
        else:result='EVIDENCE_PASS'
        findings.append({'id':r['id'],'result':result})
    return {'status':'EVIDENCE_PASS' if all(r['result']=='EVIDENCE_PASS' for r in findings) else 'REVIEW','findings':findings,'tenant_enforcement':False}
def main():
    if len(sys.argv)!=2:print('Usage: python3 scripts/check.py templates/sample.json',file=sys.stderr);return 2
    try:report=evaluate(json.loads(Path(sys.argv[1]).read_text()))
    except (OSError,ValueError,TypeError,KeyError) as e:print(json.dumps({'status':'INVALID','error':str(e)}));return 2
    print(json.dumps(report,indent=2));return 0 if report['status']=='EVIDENCE_PASS' else 1
if __name__=='__main__':sys.exit(main())
