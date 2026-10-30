# Business application release test and rollback gate
Offline synthetic support exercise. Hold a software change until tests, rollback and independent approval are recorded.
Status: local checker evaluated29 October 2026; Windows/tenant operations unrun. No live changes or production integration.
Problem: a support colleague needs explicit failed/unknown checks at each handover/change.
Contribution: scenario/rules, implementation and local validation prepared with AI assistance; independent learner execution is still required. No client use claimed.
Quick start: Python 3.11+, no packages; run python3 -B main.py sample.json, then python3 -B -m unittest -v test_behaviour. On Windows use py -3.
Results:3 synthetic records match expected labels;9behavioural tests plus malformed CLI exit2. See [evaluation](EVALUATION.md). No time or service improvement measured.
[Full lab](LAB.md) · [Demo](DEMO%20SCRIPT.md) · [Architecture](docs/architecture.md) · [Changelog](CHANGELOG.md).
Next: independent rerun and controlled Windows exercise. Rules used instead of AI for decisions; model summaries are only an optional future comparison.
