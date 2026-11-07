# Customer ticket handover
An independent offline learning scenario maintained by Bunamin Adams. Read-only synthetic evidence checks for an analyst; not commissioned client work.
## What works
Strict input review and a JSON handover are implemented locally. Ten local regression tests and a command-line example were run on 7 November 2026; see [EVALUATION.md](EVALUATION.md) and [raw evidence](evidence/run.txt). Native Windows/physical/tenant work and learner completion are unrun.
## Quick start
Python 3.10+; no external packages, API keys, paid services or live changes.
From this scenario folder, run `python3 -m unittest -v`, then `python3 review.py sample.json north-demo`. On Windows replace python3 with py. The complete novice workflow and cleanup are in [LAB.md](LAB.md).
## Design and limits
Local JSON → validation → deterministic review → human decision. No AI is needed for this small structured checklist. It has no authentication or production integration. [Architecture](docs/architecture.md), [demo](DEMO%20SCRIPT.md), [changes](CHANGELOG.md). No learner capability or commercial result follows from automated fixture checks.
