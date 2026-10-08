"""Read-only search of synthetic structured tickets. No pupil or free-text input."""
import json, argparse, sys
from datetime import date
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
from atomic_json import write_atomic
def analyse(data,as_of):
    today=date.fromisoformat(as_of)
    if set(data)!={'tickets','articles'}: raise ValueError('Expected tickets and articles')
    groups={}; seen=set(); articles={}
    for a in data['articles']:
        if set(a)!={'id','service','symptom','approved','valid_until'} or type(a['approved']) is not bool:
            raise ValueError('Article fields invalid')
        if not all(isinstance(a[k],str) and a[k].strip() for k in ['id','service','symptom','valid_until']): raise ValueError('Article value missing')
        if a['id'] in seen: raise ValueError('Duplicate article')
        seen.add(a['id']); valid=date.fromisoformat(a['valid_until'])
        if a['approved'] and valid>=today:
            articles.setdefault((a['service'],a['symptom']),[]).append(a['id'])
    seen=set(); excluded=0
    for t in data['tickets']:
        if set(t)!={'id','service','symptom','status','sensitive'} or type(t['sensitive']) is not bool:
            raise ValueError('Ticket fields invalid; free text is not accepted')
        if not all(isinstance(t[k],str) and t[k].strip() for k in ['id','service','symptom','status']): raise ValueError('Ticket value missing')
        if t['id'] in seen or t['status'] not in {'open','resolved'}: raise ValueError('Duplicate or invalid ticket')
        seen.add(t['id'])
        if t['sensitive']: excluded+=1;continue
        if t['status']!='resolved': continue
        key=(t['service'],t['symptom']); groups[key]=groups.get(key,0)+1
    return dict(as_of=as_of,excluded_sensitive=excluded,groups=[dict(service=k[0],symptom=k[1],resolved_count=n,
        recurring=n>=2,article_ids=sorted(articles.get(k,[])),needs_review=not bool(articles.get(k))) for k,n in sorted(groups.items())])
def main():
    p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--as-of',required=True);a=p.parse_args()
    if Path(a.input).resolve()==Path(a.output).resolve(): p.error('Output must differ from input')
    try:
        result=analyse(json.loads(Path(a.input).read_text()),a.as_of); write_atomic(a.output,result)
    except (ValueError,TypeError,KeyError,OSError) as e: p.exit(2,str(e)+'\n')
    print(f"Wrote {len(result['groups'])} groups; no instructions or tickets were changed.")
if __name__=='__main__': main()
