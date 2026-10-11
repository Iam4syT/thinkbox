"""Local declared-readiness exercise. Never grants or revokes access."""
import json, argparse
def analyse(rows):
    if not isinstance(rows,list) or not rows: raise ValueError('Expected non-empty list')
    seen=set();out=[]
    for r in rows:
        if not isinstance(r,dict): raise ValueError('Expected object')
        for k in ['id','user','asset','group','reviewer']:
            if not isinstance(r.get(k),str) or not r[k].strip(): raise ValueError('Missing '+k)
        if r['id'] in seen: raise ValueError('Duplicate id')
        seen.add(r['id'])
        for k in ['approved','enabled','privileged','sign_in_test','app_test','peripheral_test']:
            if type(r.get(k)) is not bool: raise ValueError('Invalid '+k)
        findings=[]
        if not r['approved']:findings.append('Missing approval')
        if not r['enabled']:findings.append('Account disabled; verify reason before action')
        if r['privileged']:findings.append('Privilege request needs separate specialist approval')
        for k in ['sign_in_test','app_test','peripheral_test']:
            if not r[k]:findings.append('Unverified '+k)
        out.append(dict(id=r['id'],asset=r['asset'],user=r['user'],reviewer=r['reviewer'],findings=findings,
          status='hold' if findings else 'review_ready',mode='dry_run',
          next_action='Human must compare declared checks with permitted real evidence'))
    return out
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');a=p.parse_args()
    try: result=analyse(json.load(open(a.input)))
    except (ValueError,OSError) as e:p.exit(2,str(e)+'\n')
    with open(a.output,'w') as f:json.dump(result,f,indent=2);f.write('\n')
