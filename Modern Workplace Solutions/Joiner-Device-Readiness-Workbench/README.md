# Joiner and device readiness

Independent manufacturing-workplace learning workbench. Codex-assisted source and local evaluation; not commissioned by an employer. The learner must reproduce and explain the work before claiming personal proficiency.

## What works

Offline JSON checking/routing is implemented. Six synthetic records and seven behavioural tests were executed locally on 1 October 2026. Tenant, device, factory and AI steps are unrun.

## Quick start

Python 3.10+ standard library. No new packages required. Run from this project root:

```sh
python3 scripts/readiness.py --input templates/sample.json --output output/result.json
python3 -m unittest discover -s scripts -p "test_*.py" -v
```

## Business relevance and trade-offs

The intended user is a workplace support engineer repeating readiness or handover checks. The baseline is a manual checklist/template. Deterministic checks make reasons explicit; they never approve changes. No time-saving claim or production integration. AI is unnecessary for readiness and planned/unrun for triage summaries.

See [LAB.md](LAB.md), [evaluation](EVALUATION.md), [demo](DEMO%20SCRIPT.md), [architecture](docs/architecture.md) and [test evidence](evidence/test-output.txt).

Read [contribution details](CONTRIBUTIONS.md) and [machine-readable evaluation](evidence/evaluation.json). Source commit is recorded in Git history.

## Additional strict record-validation scenario
See [strict-record-validation](scenarios/strict-record-validation/README.md) for an isolated synthetic schema/checklist exercise with explicit invalid-input handling. Existing workflow remains unchanged.
