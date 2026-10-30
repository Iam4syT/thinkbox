import argparse, json, sys
from pathlib import Path
CHECKS = ['functional_test', 'access_test', 'rollback_test', 'reviewer_approved']

def evaluate(rows):
    if not isinstance(rows, list) or not rows:
        raise ValueError('Expected a non-empty list of records')
    seen=set(); output=[]
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get('id'), str) or not row['id'].strip():
            raise ValueError('Every record needs a non-empty string id')
        if row['id'] in seen:
            raise ValueError('Duplicate record id: '+row['id'])
        seen.add(row['id'])
        unexpected=set(row)-set(CHECKS)-{'id'}
        if unexpected:
            raise ValueError('Unexpected fields: '+','.join(sorted(unexpected)))
        for key in CHECKS:
            if row.get(key) is not None and type(row[key]) is not bool:
                raise ValueError('Checks must be JSON true, false or null: '+key)
        unknown=[k for k in CHECKS if row.get(k) is None]
        failed=[k for k in CHECKS if row.get(k) is False]
        status='HOLD' if failed else 'REVIEW' if unknown else 'READY_FOR_HUMAN_REVIEW'
        output.append(dict(id=row['id'],status=status,failed=failed,unknown=unknown))
    return output

if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Offline synthetic checklist; never authorises live changes')
    parser.add_argument('input'); parser.add_argument('--out')
    args=parser.parse_args()
    try:
        path=Path(args.input)
        if path.stat().st_size > 1_000_000: raise ValueError('Input exceeds 1 MB limit')
        result=evaluate(json.loads(path.read_text()))
        text=json.dumps(result,indent=2)+'\n'
        if args.out: Path(args.out).write_text(text)
        else: print(text,end='')
    except (ValueError,OSError) as error:
        print('INVALID INPUT: '+str(error),file=sys.stderr);sys.exit(2)
