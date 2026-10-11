# Healthcare support case review
Turn synthetic support cases into a review list and a recurring-category report, while keeping safety concerns and missing evidence visible.
Independent learning demonstration created with Codex assistance, not commissioned by TPP or used with live patient data. Python 3.11+, standard library only. Bunamin’s personal reproduction is pending.
## Run
From this folder: python3 -m unittest discover -s tests -v, then python3 src/main.py. See [LAB.md](LAB.md).
## Scope and evidence
Implemented local validation, rules and report. Synthetic service data; no SystmOne integration, AI service or deployment. See [evaluation](EVALUATION.md), [contributions](CONTRIBUTIONS.md), [architecture](docs/architecture.md) and [demo](DEMO%20SCRIPT.md).
## Next test
A human reviewer should independently mark ten new synthetic records before comparing results. No measured operational saving or personal independent competence inferred.
