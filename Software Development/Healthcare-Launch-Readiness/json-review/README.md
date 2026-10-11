# Healthcare launch evidence review

Status: locally built and evaluated, 11 October 2026. Independent Codex-assisted learning demo for Bunamin Adams; personal reproduction pending. Not commissioned by a healthcare provider or vendor.

## Problem and contribution
Each software launch needs training, support ownership, testing and a way to undo a change. TPP’s vacancy includes product launches. Its 3 September 2026 South Brent case study describes checks and prompts in a referral workflow. This lab practises administrative evidence review; its checklist is a chosen teaching model, not TPP’s release procedure. Codex wrote and tested this small standard-library package. See [contribution boundaries](CONTRIBUTIONS.md).

## Quick start
Python 3.10+; no pip installation. From this project folder:

```sh
python3 -m unittest discover -s scripts -p "test_*.py" -v
python3 scripts/check_launch.py --input templates/sample.json --output output/result.json
```

## Actual result and limits
A complete synthetic checklist returned ready-for-human-review; removing rollback evidence returned hold and named rollback. Neither output grants go-live permission. Eight behavioural tests passed. No measured time saving, real patient data, vendor connection or production deployment. Explicit rules are the simpler baseline; no AI is required.

[Complete lab](LAB.md) · [Evaluation](EVALUATION.md) · [Demo](DEMO%20SCRIPT.md) · [Architecture](docs/architecture.md) · [Test output](evidence/tests.txt) · [Change history](CHANGELOG.md)
