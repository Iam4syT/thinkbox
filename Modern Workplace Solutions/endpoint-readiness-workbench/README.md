# Endpoint readiness and diagnostic evidence

Status: offline synthetic slice built and evaluated; tenant validation remains pending. Maintainer: Bunamin Adams. Scaffold authored/tested by an assistant; learner independent operation is pending. See [contribution and provenance](CONTRIBUTIONS.md).

## Problem and useful outcome

Support engineers need fresh, scoped endpoint evidence before recommending a change. This workbench reports enrolment, configuration, compliance, application and authentication/connectivity failures without turning stale data or a log hint into a confirmed root cause.

This is an independent learning project. No customer/employer system or confidential data was used; no measured workplace benefit is claimed.

## What works today

| Capability | State | Evidence |
|---|---|---|
| Local synthetic input-to-output workflow | Implemented | [Source](scripts/readiness.py) |
| Expected states and safety/failure cases | Evaluated | [Evaluation](EVALUATION.md), 10 tests |
| Intune/Windows and any service integration | Unrun guide | [Full lab](LAB.md) |
| Production outcomes/candidate proficiency | Unestablished | [Contribution limits](CONTRIBUTIONS.md) |

## Run a small example

Python 3.11+; no external dependencies, credentials, cloud account or installation required. From this project root:

```sh
python3 scripts/readiness.py --output outputs/result.json
python3 -m unittest discover -s tests -v
```

On Windows replace `python3` with `py -3`. Expected: 5 records, no mutation and the classifications recorded in [evidence/evaluation.json](evidence/evaluation.json). Read the [granular lab](LAB.md) for the manual baseline, observed outputs, failure recovery, optional tenant prerequisites/licences and cleanup.

## Design and trade-offs

Freshness and unknown evidence stay separate from an observed fixture failure. Log text is inert and no recommendation changes the device. Rules are the baseline; AI adds no needed function to these checks. [Architecture and handover](docs/architecture.md).

## Results and next step

5 synthetic records and 10 passing tests; malformed CLI rejected without a new report. [Evidence and limits](EVALUATION.md). This is a narrow synthetic evaluation, not production validation. The learner should reproduce it, explain a failure, then run a scoped isolated tenant path if access/approval exists.

## Reuse

[Demo script](DEMO%20SCRIPT.md), [change record](CHANGELOG.md), [MIT licence](LICENSE). Microsoft documentation is linked in the lab. Preserve attribution and keep real diagnostic logs/private application records outside this package.
