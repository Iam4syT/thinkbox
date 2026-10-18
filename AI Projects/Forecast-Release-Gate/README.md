# Forecast release gate

Train a small regression model and stop release when held-out error or data checks fail.

Status: locally evaluated synthetic baseline; no live LLM, tenant or production deployment.

## Run
Open this directory and run `python3 -B main.py` followed by `python3 -B -m unittest discover -s tests -v`. Python 3.10+, no external dependencies or accounts.

## Results and limits
Six behavioural tests pass. Eight training and four held-out rows give slope 2, intercept 3, model RMSE 0 versus baseline 5.4772 target units; gate pass. Adding a target shift of 10 produces model RMSE 10 and gate hold. Perfect fit follows the deliberately linear synthetic data; it predicts no real forecasting accuracy.

## Reproduce
[Complete lab](LAB.md), [evaluation](EVALUATION.md), [contributions](CONTRIBUTIONS.md), [architecture](docs/architecture.md), [demo](DEMO%20SCRIPT.md). Personal reproduction and real-use value remain to establish.
