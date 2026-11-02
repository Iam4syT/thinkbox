"""Synthetic discovery checks; no automatic architecture approval."""
import json
import sys
from pathlib import Path

def assess(data):
    if not isinstance(data, dict) or not isinstance(data.get('requirements'), list):
        raise ValueError('requirements must be a list')
    issues = []
    seen = set()
    for item in data['requirements']:
        if not isinstance(item, dict):
            raise ValueError('each requirement must be an object')
        rid = item.get('id')
        if not isinstance(rid, str) or not rid or rid in seen:
            raise ValueError('requirement IDs must be nonempty and unique')
        seen.add(rid)
        for key in ('owner', 'need', 'acceptance'):
            if not isinstance(item.get(key), str) or not item[key].strip():
                issues.append(f'{rid}: missing {key}')
    if not seen:
        issues.append('No requirements recorded')
    for key in ('data_classification', 'retention_days', 'availability_target', 'dependency_owner'):
        if data.get(key) in (None, ''):
            issues.append(f'Unresolved {key}')
    days = data.get('retention_days')
    if days is not None and (type(days) is not int or days < 1):
        issues.append('retention_days must be a positive integer')
    return issues

def report(data):
    issues = assess(data)
    lines = ['# Discovery review', '', 'Status: needs review' if issues else 'Status: checklist complete; human approval still required', '', '# Traceability']
    for r in data['requirements']:
        lines.append(f"- {r['id']} | {r.get('owner', '?')} | {r.get('need', '?')} | Check: {r.get('acceptance', '?')}")
    lines += ['', '# Open questions'] + ['- ' + x for x in issues]
    lines += ['', '# Proposed design decision', 'Begin with a single service and relational storage for this small synthetic workload. Compare a spreadsheet for lower-volume manual use. A separate microservice is a future option only if ownership, deployment or scaling needs justify it.', '', '# Approval', 'A checklist is not security assurance. A service owner and architect must review assumptions, cost, failure behaviour and data handling.']
    return '\n'.join(lines) + '\n'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python3 main.py data/brief.json')
    try:
        print(report(json.loads(Path(sys.argv[1]).read_text())), end='')
    except (OSError, ValueError, KeyError) as exc:
        raise SystemExit(str(exc))
