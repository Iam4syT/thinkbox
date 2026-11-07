# Approval workflow with safe integration failures
Status: locally evaluated synthetic baseline; Microsoft/AI extension unrun.
Maintained by Bunamin Adams. This is independent portfolio work, not an employer deployment.

## Problem and use
Repeated staff requests need review and clear handling of duplicate events and failed integrations.
The smallest useful implementation is a rules-based baseline. AI and tenant integration are separate experiments.

## Run
From this scenario directory, run `python3 -m unittest discover -s tests -v`, then the command in [LAB.md](LAB.md). Python 3.11+; standard library only; no secrets or API charges.

## Evidence and limits
See [EVALUATION.md](EVALUATION.md), [test output](evidence/tests.txt) and [architecture](docs/architecture.md). Local tests do not prove live permissions, production scale, model quality or personal independent operation. Personal reproduction remains a separate evidence step.
The initial implementation was prepared with AI coding assistance. No personal authorship or independent operation is inferred from file ownership.

## Reuse
[Lab](LAB.md) · [Demo](DEMO%20SCRIPT.md) · [Change record](CHANGELOG.md). Licensing follows the parent repository; no third-party dataset is bundled.
