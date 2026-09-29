# Approval-aware patch change and user communication

Status: offline synthetic slice built and evaluated; tenant validation remains pending. Maintainer: Bunamin Adams. Scaffold authored/tested by an assistant; learner independent operation is pending. See [contribution and provenance](CONTRIBUTIONS.md).

## Problem and useful outcome

Workplace and security teams need a reviewable path from vulnerability finding to change, employee communication and verified closure. This workbench keeps missing approval, unresolved risk and incomplete validation visible.

This is an independent learning project. No customer/employer system or confidential data was used; no measured workplace benefit is claimed.

## What works today

| Capability | State | Evidence |
|---|---|---|
| Local synthetic input-to-output workflow | Implemented | [Source](scripts/change_workbench.py) |
| Expected states and safety/failure cases | Evaluated | [Evaluation](EVALUATION.md), 10 tests |
| Intune/Windows and any service integration | Unrun guide | [Full lab](LAB.md) |
| Production outcomes/candidate proficiency | Unestablished | [Contribution limits](CONTRIBUTIONS.md) |

## Run a small example

Python 3.11+; no external dependencies, credentials, cloud account or installation required. From this project root:

```sh
python3 scripts/change_workbench.py --output outputs/result.json
python3 -m unittest discover -s tests -v
```

On Windows replace `python3` with `py -3`. Expected: 6 records, no mutation and the classifications recorded in [evidence/evaluation.json](evidence/evaluation.json). Read the [granular lab](LAB.md) for the manual baseline, observed outputs, failure recovery, optional tenant prerequisites/licences and cleanup.

## Design and trade-offs

Approval, version, reboot, app health and security recheck are separate gates. Rules are the implemented baseline. Optional AI wording comparison is a planned extension and cannot authorise or execute change. [Architecture and handover](docs/architecture.md).

## Results and next step

6 synthetic records and 10 passing tests; malformed CLI rejected without a new report. [Evidence and limits](EVALUATION.md). This is a narrow synthetic evaluation, not production validation. The learner should reproduce it, explain a failure, then run a scoped isolated tenant path if access/approval exists.

## Reuse

[Demo script](DEMO%20SCRIPT.md), [change record](CHANGELOG.md), [MIT licence](LICENSE). Microsoft documentation is linked in the lab. Preserve attribution and keep real diagnostic logs/private application records outside this package.
