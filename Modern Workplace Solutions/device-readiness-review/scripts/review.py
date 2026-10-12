import json, sys
from pathlib import Path
def review(data):
    seen=set(); output=[]
    for row in data:
        serial=row.get('serial')
        if not serial or serial in seen: raise ValueError('missing or duplicate serial')
        seen.add(serial)
        if row.get('os') not in {'macOS','iOS','Windows'}: raise ValueError('unsupported OS')
        for key in ['managed','encrypted','patched']:
            if type(row.get(key)) is not bool: raise ValueError(key+' must be boolean')
        issues=[]
        if not row.get('owner'): issues.append('owner-unrecorded')
        for key in ['managed','encrypted','patched']:
            if not row[key]: issues.append(key+'-check-required')
        output.append({'serial':serial,'os':row['os'],'status':'review' if issues else 'ready-for-human-check','issues':issues,'ticket_required':bool(issues)})
    return output
if __name__=='__main__': print(json.dumps(review(json.loads(Path(sys.argv[1]).read_text())),indent=2))
