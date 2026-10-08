# Joiner device readiness

A synthetic law-firm service-desk learning demo. Built and tested locally with Codex assistance on 8 October 2026. No live tenant, device or client integration. The learner has not independently reproduced this version.

Local CSV → Python rules → JSON explanation → human review. See [LAB.md](LAB.md), [architecture](docs/architecture.md), [evaluation](EVALUATION.md) and [contribution](CONTRIBUTIONS.md). No AI is needed for these fixed rules. This is not commissioned employer work.

Run Python 3.10 or later from this folder. `python3 scripts/check_readiness.py data/joiners.csv`

Run checks: `python3 -m unittest discover -s tests -v`. See the lab for exact outputs, failure practice, permission limits and cleanup.
