# Incident lifecycle practice
Independent synthetic practice tool. Local behaviour evaluated29 October 2026; no live service connection or workplace outcome measured.

Practise impact/urgency decisions, safe escalation and follow-up before closure. Repeated daily queue checks are a plausible support need, not a measured employer defect.

## Run
Python 3.11 or 3.12; no packages, account or licence. From this folder run `python3 scripts/workbench.py templates/sample.json` then `python3 -B -m unittest discover -s tests -v`.

## Design
Analyst → synthetic ticket file → local rules → suggested priority/action → human review. No real ticket changes or notifications. Rules are deliberately small and explainable. AI is omitted: no evidence that a language model improves these structured decisions. An optional future comparison would measure missed urgent cases or unsupported article advice before adoption.

## Evidence and limits
[Lab](LAB.md), [evaluation](EVALUATION.md), [demo](DEMO%20SCRIPT.md), [architecture](docs/architecture.md), [test output](evidence/test-output.txt), [source](scripts/workbench.py), [changes](CHANGELOG.md).
Source and test implementation were prepared with automated assistance. Maintainer review and an independent rebuild remain separate milestones. No personal mastery, ITIL certification, commercial deployment or company commission is claimed.
