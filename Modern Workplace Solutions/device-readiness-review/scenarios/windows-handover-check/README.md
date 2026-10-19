# Endpoint handover check

Status: locally evaluated synthetic prototype. No live integration.

## Problem and approach
Every device handover/change needs repeatable evidence. Missing approval or unknown encryption must stop a checklist from being called complete. Device state is synthetic input, not telemetry.

Device setup assistance, patch support, access approval and documented user checks. Input CSV → validated rules → JSON findings → human review. No external dependency, credentials or account changes. A deterministic baseline is sufficient; no AI needed for these rules.

## Run
Use Python3.11 or later. From this folder: `python3 -B scripts/check.py templates/sample.csv`; Windows: `py -3 -B scripts/check.py templates/sample.csv`. Then run `python3 -B -m unittest discover -s tests -v`. Four input records and five behavioural tests; [results](EVALUATION.md) include one rejected CLI fixture. See [complete lab](LAB.md), [demo](DEMO%20SCRIPT.md), [architecture](docs/architecture.md) and [change record](CHANGELOG.md).

## Contribution and limits
A small support-learning tool with explicit rules, fixtures and error handling. Local checks do not prove live M365/AD/Intune support or physical-device ability. No real incidents, names or employer data included. Human judgement and approved evidence remain required; production security and Windows device execution are untested. Intended operational benefit has not been measured. Learner rebuild is the next evidence step. Code licensing follows the destination repository's root licence; all included fixtures are invented for this example.
