# Energy forecast checks

Independent local learning example. Read [the lab](LAB.md), [evaluation](EVALUATION.md) and [contributions](CONTRIBUTIONS.md).

Run from this folder with Python 3.10+: `python3 main.py` and `python3 -m unittest discover -s tests -v`. No external packages or API keys. Inputs are synthetic. Outputs are local.

Operator -> validated local CSV -> first eight rows for training -> next four rows for testing -> previous-observation baseline and fitted straight-line forecast -> local metrics.json -> human review. The baseline uses the last observed value available before each forecast. The fitted model uses training rows only. No identity provider or service account is needed.

A proposed energy analyst could rerun the checks for each permitted data refresh. Intended value is catching invalid data and weak forecasts before a planning review. Measure forecast error on representative unseen data and the number of rejected bad inputs. Actual employer demand and cost savings are unknown.
