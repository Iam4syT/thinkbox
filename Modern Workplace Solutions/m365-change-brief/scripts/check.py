"""Build a review queue from synthetic change records. Never publishes."""
import csv,json,sys
from datetime import date
def analyse(rows,today):
    today=date.fromisoformat(today);seen=set();out=[]
    for r in rows:
        required=['id','service','summary','due','impact','owner','status']
        if any(not r.get(k,'').strip() for k in required):raise ValueError('Required field missing')
        if r['id'] in seen:raise ValueError('Duplicate change ID')
        seen.add(r['id'])
        if r['impact'] not in ['high','low'] or r['status'] not in ['draft','approved']:raise ValueError('Unknown impact or status')
        due=date.fromisoformat(r['due']);days=(due-today).days
        urgency='overdue' if days<0 else 'due soon' if days<=7 else 'scheduled'
        out.append(dict(id=r['id'],service=r['service'],summary=r['summary'],due=due.isoformat(),owner=r['owner'],impact=r['impact'],urgency=urgency,review='owner approval needed' if r['status']=='draft' else 'approval recorded; recheck source and audience before manual communication'))
    if not out:raise ValueError('No records')
    return {'mode':'synthetic offline','as_of':today.isoformat(),'queue':sorted(out,key=lambda r:(r['due'],r['id'])),'limit':'Recorded approval is fixture data; no email, tenant change or real approval occurs'}
if __name__=='__main__':
    try:
        with open(sys.argv[1],newline='',encoding='utf-8') as f:rows=list(csv.DictReader(f))
        print(json.dumps(analyse(rows,sys.argv[2]),indent=2))
    except (ValueError,KeyError,IndexError,OSError) as exc:
        print('Input rejected: '+str(exc),file=sys.stderr);sys.exit(2)
