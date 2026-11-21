import json
import sys
from pathlib import Path

def decide(row):
    metadata = ('purpose', 'users', 'logic', 'benefit', 'support', 'owner')
    if row['data'] != 'approved' or any(not str(row.get(k, '')).strip() for k in metadata):
        return 'GOVERNANCE REVIEW'
    if not row['needed']:
        return 'RETIRE REVIEW'
    if not row['tested']:
        return 'IMPROVE'
    return 'HANDOVER REVIEW'

def main():
    if len(sys.argv) != 2:
        sys.exit('Usage: python3 scripts/review.py templates/sample.json')
    try:
        rows = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
        if not isinstance(rows, list) or not rows:
            raise ValueError('Provide a non-empty list.')
        seen = set()
        results = []
        for row in rows:
            if not isinstance(row, dict) or not isinstance(row.get('id'), str) or not row['id'].strip():
                raise ValueError('Every row needs a text ID.')
            if row['id'] in seen:
                raise ValueError('Duplicate ID: ' + row['id'])
            seen.add(row['id'])
            if any(type(row[k]) is not bool for k in ['tested', 'needed']):
                raise ValueError('Check flags must be true or false.')
            if any(not isinstance(row.get(k), str) for k in ['id', 'purpose', 'users', 'logic', 'benefit', 'support', 'owner', 'data']):
                raise ValueError('Each required text field must be a string.')
            results.append(row['id'] + ': ' + decide(row))
        print('\n'.join(results))
    except (OSError, TypeError, KeyError, ValueError) as err:
        sys.exit('Invalid input: ' + str(err))
if __name__ == '__main__':
    main()
