"""Read-only synthetic identity reconciliation. Never performs directory matching."""
import json,sys
from pathlib import Path
def evaluate(data):
    if not isinstance(data,dict) or set(data)!={'onprem','cloud'}: raise ValueError('Expected onprem and cloud lists')
    for name in ['onprem','cloud']:
        rows=data[name]
        if not isinstance(rows,list): raise ValueError(name+' must be a list')
        seen=set()
        for row in rows:
            if not isinstance(row,dict) or not {'id','smtp','enabled'}<=set(row): raise ValueError('Missing identity fields')
            if not all(isinstance(row[k],str) and row[k].strip() for k in ['id','smtp']): raise ValueError('Empty identity')
            if row['id'] in seen: raise ValueError('Duplicate object id')
            seen.add(row['id'])
            if type(row['enabled']) is not bool: raise ValueError('enabled must be boolean')
            if name=='cloud' and type(row.get('synced')) is not bool: raise ValueError('synced must be boolean')
    findings=[]
    for row in data['onprem']:
        key=row['smtp'].strip().casefold()
        local=[r for r in data['onprem'] if r['smtp'].strip().casefold()==key]
        cloud=[r for r in data['cloud'] if r['smtp'].strip().casefold()==key]
        if len(local)>1 or len(cloud)>1: result='AMBIGUOUS'
        elif not cloud: result='MISSING'
        elif not row['enabled'] or not cloud[0]['enabled']: result='DISABLED_REVIEW'
        elif not cloud[0]['synced']: result='UNSYNCED'
        else: result='CHECKS_PASS'
        findings.append({'id':row['id'],'result':result})
    if not findings: raise ValueError('No onprem identities to check')
    return {'status':'CHECKS_PASS' if all(r['result']=='CHECKS_PASS' for r in findings) else 'REVIEW','findings':findings,'writes_performed':0}
def main():
    if len(sys.argv)!=2: print('Usage: python3 scripts/check.py templates/sample.json',file=sys.stderr);return 2
    try: report=evaluate(json.loads(Path(sys.argv[1]).read_text()))
    except (OSError,ValueError,TypeError) as e: print(json.dumps({'status':'INVALID','error':str(e)}));return 2
    print(json.dumps(report,indent=2));return 0 if report['status']=='CHECKS_PASS' else 1
if __name__=='__main__':sys.exit(main())
