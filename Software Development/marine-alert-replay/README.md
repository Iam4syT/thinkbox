# Marine alert replay

Independent local learning example. Read [the lab](LAB.md), [evaluation](EVALUATION.md) and [contributions](CONTRIBUTIONS.md).

Run from this folder with Python 3.10+: `python3 main.py` and `python3 -m unittest discover -s tests -v`. No external packages or API keys. Inputs are synthetic. Outputs are local.

Operator -> local synthetic scenario JSON -> numeric/age validation -> deterministic teaching rules -> replay.json with recommendation and reason -> human review. Every record includes actuation false. There is no hardware, network, device driver, cloud identity or equipment command.

A proposed software test engineer could replay these checks after each change. Intended value is finding regressions and making missing or stale information visible. Measure missed expected HOLDs and unexplained output changes. Actual marine safety performance is unestablished.
