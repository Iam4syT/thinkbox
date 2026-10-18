# Hybrid identity reconciliation

An independent, read-only Python lab for identity support teams. It uses synthetic JSON and never connects to a tenant. It is not a commissioned client deployment.

From this project folder, run `python3 scripts/check.py templates/sample.json`, then `python3 -m unittest discover -s scripts -p "test_*.py" -v`. Python 3.10+; no dependencies or paid service.

The deterministic baseline makes each finding inspectable. A language model would add cost and uncertainty to exact identity/time comparisons, so no AI model is used at runtime. No measured workplace savings are claimed.

See [LAB.md](LAB.md), [evaluation](EVALUATION.md), [demo](DEMO%20SCRIPT.md), [architecture](docs/architecture.md), [contribution scope](CONTRIBUTIONS.md) and [change log](CHANGELOG.md). Live Microsoft validation remains unrun. Licence follows the repository root licence.
