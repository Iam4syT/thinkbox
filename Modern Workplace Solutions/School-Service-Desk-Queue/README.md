# Incident queue review
A desk agent needs to see which requests need attention first. This lab turns five dummy software requests into a sorted review list. It flags a possible major incident for a person to assess. It never declares an incident or contacts a user.
Independent learning demo for education software support. Built and fixture-tested with Codex; personal reproduction pending. No commissioned client work or live integration.
## Quick start
From this folder, with Python 3.11+:
```sh
python3 -m unittest discover -s tests -v
python3 src/queue_check.py data/requests.csv evidence/result.json
```
Read [LAB.md](LAB.md) for setup, expected values, failure recovery and cleanup. [Evaluation](EVALUATION.md) records actual tests. [Contributions](CONTRIBUTIONS.md) states who did what. [Architecture](docs/ARCHITECTURE.md) describes the boundary.
## Baseline and intended value
A manual spreadsheet using the same rules is the baseline. The target is correct fixture decisions and safe rejection of malformed inputs. No time or hiring benefit is measured. No AI service is necessary for this scope.
