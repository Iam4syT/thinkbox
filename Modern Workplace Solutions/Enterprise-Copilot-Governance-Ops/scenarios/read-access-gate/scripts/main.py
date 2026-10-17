"""Offline read-only assistant access boundary. No network or model calls."""
import argparse, json
from pathlib import Path

def retrieve(request, documents):
    if request.get('operation') != 'read':
        return {'allowed': False, 'reason': 'operation_denied', 'document_ids': []}
    subject=request.get('subject')
    if not isinstance(subject,str) or not subject:
        return {'allowed': False, 'reason': 'missing_identity', 'document_ids': []}
    if request.get('consent') is not True:
        return {'allowed': False, 'reason': 'consent_required', 'document_ids': []}
    allowed=[]
    for doc in documents:
        if (doc.get('classification') == 'internal' and
            isinstance(doc.get('readers'),list) and subject in doc['readers']):
            allowed.append({'id':doc['id'],'text':doc['text']})
    return {'allowed':bool(allowed),'reason':'authorised_documents' if allowed else 'no_access',
            'document_ids':[d['id'] for d in allowed], 'documents':allowed}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--input',default='templates/request.json');args=parser.parse_args()
    req=json.loads(Path(args.input).read_text());docs=json.loads(Path('templates/documents.json').read_text())
    result=retrieve(req,docs)
    Path('evidence').mkdir(exist_ok=True)
    # Audit excludes content; demo stdout is synthetic only.
    audit={k:v for k,v in result.items() if k!='documents'}
    Path('evidence/audit.json').write_text(json.dumps(audit,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
