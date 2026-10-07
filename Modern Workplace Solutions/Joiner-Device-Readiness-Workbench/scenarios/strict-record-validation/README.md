# Device Readiness
Independent offline support learning demo. Assistant-built, synthetic only; Windows/physical device and M365 tenant steps remain unrun. No employer deployment or measured service improvement.

The recurring problem is knowing which device-readiness checks remain unresolved.
The baseline is a manual checklist. Deterministic validation is sufficient; no model/API is required.

## Run
Python 3, standard library only, no installation, cloud cost or credentials.
From this project folder:
```
python3 scripts/check_readiness.py templates/ready.json
python3 -m unittest discover -s tests -v
```
Expected: READY for the complete fixture. Failed or missing input must never be mistaken for success.

## Scope and contribution
Codex authored the local tool, fixtures, tests and guide from the user's support-learning request. These outputs do not demonstrate the learner's independent competence. Human review checks observation accuracy; the tool checks only the record shape and stated values. No network calls, live changes or data collection.
See [LAB](LAB.md), [evaluation](EVALUATION.md), [demo](DEMO%20SCRIPT.md), [architecture](docs/architecture.md) and [contributions](CONTRIBUTIONS.md). Licence: MIT, original code; technical guidance attributed in LAB.
