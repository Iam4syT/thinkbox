# Customer-satisfaction pipeline learning

Compare a review-score predictor with a simple baseline while separating preprocessing and evaluation.

This is a portfolio learning project maintained by Bunamin Adams. Read [contribution and provenance](CONTRIBUTIONS.md), [the lab](LAB.md), [evaluation](EVALUATION.md) and [change record](CHANGELOG.md).

## What works and what it means

| Component | State | Evidence |
|---|---|---|
| Local group-split benchmark with training-only imputation, mean baseline and Ridge model | Implemented at the scope described here | [Source](mlops-project/demo.py); [Recorded evaluation](mlops-project/evidence/evaluation.json) |
| Live/business outcome | Unestablished unless explicitly recorded | One local holdout does not validate production serving, temporal performance, drift monitoring or causal business effects. Earlier ZenML code is retained as legacy study material. |

Starting point credits Ayush Singh. The duplicated inner directory was flattened; see mlops-project/MIGRATION.md and data provenance. Historical dependency pins are in requirements-legacy.txt.

## Reproduce a small example

Commands below assume a new clone; if already inside thinkbox, navigate directly to the quoted project path. Python examples use Python 3.11. On Windows activate the environment using its Scripts/Activate.ps1 instead.

```sh
git clone https://github.com/Iam4syT/thinkbox.git
cd "thinkbox/AI Projects/MLOps/mlops-project"
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python demo.py
```

Read [LAB.md](LAB.md) for expected results, troubleshooting and cleanup. Do not interpret an unrun live step as an integration test. Dependency downloads require internet access; offline fixtures do not need service credentials.

## Results, limits and next step

One local holdout does not validate production serving, temporal performance, drift monitoring or causal business effects. Earlier ZenML code is retained as legacy study material. [Recorded evaluation](mlops-project/evidence/evaluation.json) describes method and observed results; a small synthetic evaluation is not proof of workplace impact. Source revision/environment are recorded in the repository verification report.

Use [DEMO SCRIPT.md](DEMO%20SCRIPT.md) for a short walkthrough. The next useful step is the smallest evaluation that could change a decision, using permitted data and a justified baseline.

## Layout and reuse

Keep the established source folders in place. Repository CI lives at root `.github/workflows`, with project working directories. Code licensing follows [the root licence](../../LICENSE) and any project-specific notice; third-party datasets, papers and adapted code retain their own terms.

## Last local verification

20 September 2026, macOS arm64. See the [verification report](../../docs/VERIFICATION.md) for the exact runtime, command, result and untested boundaries. The evidence is local or mocked at the stated scope.
