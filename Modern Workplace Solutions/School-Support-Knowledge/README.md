# Recurring issue and knowledge review
A desk lead needs to find repeat software issues and check whether approved guidance exists. This lab groups resolved dummy tickets by service and symptom, then lists matching approved, unexpired article IDs. It asks for review when there is no usable article. It does not generate fixes or prove a root cause.
Independent learning demo for education software support. Built and fixture-tested with Codex; personal reproduction pending. No commissioned client work or live integration.
## Quick start
From this folder, with Python 3.11+:
```sh
python3 -m unittest discover -s tests -v
python3 src/knowledge_check.py data/history.json evidence/result.json --as-of 2026-10-08
```
Read [LAB.md](LAB.md) for setup, expected values, failure recovery and cleanup. [Evaluation](EVALUATION.md) records actual tests. [Contributions](CONTRIBUTIONS.md) states who did what. [Architecture](docs/ARCHITECTURE.md) describes the boundary.
## Baseline and intended value
A manual spreadsheet using the same rules is the baseline. The target is correct fixture decisions and safe rejection of malformed inputs. No time or hiring benefit is measured. No AI service is necessary for this scope.
