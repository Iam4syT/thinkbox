# Retrieval evidence workbench

Return an allowed source or a refusal for a recurring support question.

Status: locally evaluated synthetic baseline; no live LLM, tenant or production deployment.

## Run
Open this directory and run `python3 -B main.py --evaluate` followed by `python3 -B -m unittest discover -s tests -v`. Python 3.10+, no external dependencies or accounts.

## Results and limits
Five behavioural tests pass. Across six fixed cases, unfiltered keyword retrieval scores 4/6 with two unauthorised returns; filtered retrieval scores 6/6 with zero. This is a deterministic fixture result, not an independent generalisation or security assessment. There is no measured LLM improvement.

## Reproduce
[Complete lab](LAB.md), [evaluation](EVALUATION.md), [contributions](CONTRIBUTIONS.md), [architecture](docs/architecture.md), [demo](DEMO%20SCRIPT.md). Personal reproduction and real-use value remain to establish.
