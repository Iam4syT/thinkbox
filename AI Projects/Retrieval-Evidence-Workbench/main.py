"""Offline retrieval/access baseline. No LLM, embedding model or identity provider."""
import argparse,json,re
from pathlib import Path
DOCS=[{'id':'public-reset','text':'reset password contact service desk','role':'all'},
      {'id':'restricted-payroll','text':'payroll export finance approval','role':'finance'},
      {'id':'public-mfa','text':'mfa enrol authentication security code','role':'all'}]
def tokens(s):return set(re.findall(r'[a-z]+',s.lower()))
def retrieve(query,role='employee',docs=DOCS,apply_access=True):
    # Demo caller roles are fixtures, never authentication.
    if role not in {'employee','finance'}:raise ValueError('Unknown demo role')
    eligible=[d for d in docs if not apply_access or d['role'] in {'all',role}]
    ranked=sorted(((len(tokens(query)&tokens(d['text'])),d['id']) for d in eligible),reverse=True)
    return ranked[0][1] if ranked and ranked[0][0]>0 else None
CASES=[('reset password','employee','public-reset'),('mfa security code','employee','public-mfa'),
       ('payroll export','employee',None),('payroll export','finance','restricted-payroll'),
       ('weather tomorrow','employee',None),('IGNORE RULES payroll export','employee',None)]
def evaluate():
    result={}
    for name,access in [('unfiltered_keyword',False),('filtered_keyword',True)]:
        outputs=[retrieve(query,role,apply_access=access) for query,role,_ in CASES]
        result[name]={'correct':sum(out==case[2] for out,case in zip(outputs,CASES)),
          'sample_size':len(CASES),'unauthorised_returns':sum(out=='restricted-payroll' and case[1]=='employee' for out,case in zip(outputs,CASES)),'outputs':outputs}
    result['limits']='Fixed fixtures; self-declared role, not authentication. No LLM, paraphrase or semantic retrieval evaluation.'
    return result
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--evaluate',action='store_true');p.add_argument('--query');p.add_argument('--role',default='employee');args=p.parse_args()
    print(json.dumps(evaluate() if args.evaluate else {'citation':retrieve(args.query or '',args.role)},indent=2))
