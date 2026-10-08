"""Offline queue exercise. Rules are invented for this lab, not an employer SLA."""
import csv, json, os, tempfile, argparse
from pathlib import Path
FIELDS={'id','service','impact','urgency','age_minutes'}
def analyse(rows):
    seen=set(); result=[]
    for row in rows:
        if set(row)!=FIELDS or any(v is None for v in row.values()):
            raise ValueError('Expected exactly id,service,impact,urgency,age_minutes')
        ident=row['id'].strip(); service=row['service'].strip()
        if not ident or ident in seen or not service:
            raise ValueError('Missing or duplicate id, or missing service')
        seen.add(ident)
        if row['impact'] not in {'single','group','school'} or row['urgency'] not in {'normal','urgent'}:
            raise ValueError('Unknown impact or urgency')
        age=int(row['age_minutes'])
        if age<0: raise ValueError('Negative age')
        major=row['impact']=='school' and row['urgency']=='urgent'
        priority=1 if major else 2 if row['impact'] in {'group','school'} or row['urgency']=='urgent' else 3
        target={1:30,2:120,3:480}[priority]
        result.append(dict(id=ident,service=service,priority=priority,age_minutes=age,
            target_minutes=target,overdue=age>=target,major_review=major))
    return sorted(result,key=lambda r:(r['priority'],-r['age_minutes'],r['id']))
def write_atomic(path,data):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    fd,tmp=tempfile.mkstemp(dir=path.parent,prefix='.queue-')
    try:
        with os.fdopen(fd,'w') as f: json.dump(data,f,indent=2); f.write('\n')
        os.replace(tmp,path)
    finally:
        if os.path.exists(tmp): os.unlink(tmp)
def main():
    p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');a=p.parse_args()
    if Path(a.input).resolve()==Path(a.output).resolve(): p.error('Output must differ from input')
    try:
        with open(a.input,newline='') as f: result=analyse(list(csv.DictReader(f)))
        write_atomic(a.output,result)
    except (ValueError,OSError) as e: p.exit(2,str(e)+'\n')
    print(f'Wrote {len(result)} requests; review every flag before taking action.')
if __name__=='__main__': main()
