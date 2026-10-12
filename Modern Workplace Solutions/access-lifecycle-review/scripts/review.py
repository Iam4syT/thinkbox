import json, sys
from pathlib import Path
def review(data):
    seen=set(); output=[]
    for row in data:
        uid=row.get('id'); groups=row.get('groups',[])
        if not uid or uid in seen: raise ValueError('missing or duplicate identity')
        seen.add(uid)
        if type(row.get('active')) is not bool: raise ValueError('active must be boolean')
        if not isinstance(groups,list) or any(not isinstance(g,str) for g in groups): raise ValueError('groups must be strings')
        if row['active'] and row.get('department') not in {'IT','Support'}: raise ValueError('unknown department')
        expected=[] if not row['active'] else ['all-staff','it-tools' if row['department']=='IT' else 'support-tools']
        add=sorted(set(expected)-set(groups)); remove=sorted(set(groups)-set(expected))
        output.append({'id':uid,'add':add,'remove':remove,'action':'review' if add or remove else 'no-change','requires_approval':True})
    return output
if __name__=='__main__': print(json.dumps(review(json.loads(Path(sys.argv[1]).read_text())),indent=2))
