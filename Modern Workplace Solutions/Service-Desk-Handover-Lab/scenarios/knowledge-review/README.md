# Knowledge article review
Independent synthetic practice tool. Local behaviour evaluated29 October 2026; no live service connection or workplace outcome measured.

Check draft knowledge articles for an owner, verification, escalation, approval and review date. The intended reader is a service desk author/reviewer, returning whenever a ticket becomes reusable guidance.

## Run
Python 3.11 or 3.12; no packages, account or licence. From this folder run `python3 scripts/workbench.py templates/sample.json 2026-10-29` then `python3 -B -m unittest discover -s tests -v`.

## Design
Author → synthetic article metadata → local validation → ready/hold report → reviewer. Ready means metadata checks passed, not that repair steps are safe or technically correct. Rules are deliberately small and explainable. AI is omitted: no evidence that a language model improves these structured decisions. An optional future comparison would measure missed urgent cases or unsupported article advice before adoption.

## Evidence and limits
[Lab](LAB.md), [evaluation](EVALUATION.md), [demo](DEMO%20SCRIPT.md), [architecture](docs/architecture.md), [test output](evidence/test-output.txt), [source](scripts/workbench.py), [changes](CHANGELOG.md).
Source and test implementation were prepared with automated assistance. Maintainer review and an independent rebuild remain separate milestones. No personal mastery, ITIL certification, commercial deployment or company commission is claimed.
