# Windows event triage

Group current lab events and keep unknown critical events visible for specialist handover.

Independent workplace learning scenario. Offline Python fixture workflow implemented and evaluated with AI assistance; native Windows/Intune operations and learner reproduction remain unrun. No employer system, personal data or commercial outcome.

## Run
Python 3.11 or later; standard library only. From this folder run `python3 scripts/triage.py templates/events.json --now 2026-01-01T10:00:00+00:00` and `python3 -m unittest discover -s tests -v`. On Windows use `py -3` instead of `python3`.

See [LAB.md](LAB.md) for granular setup, expected results, break/fix and cleanup; [EVALUATION.md](EVALUATION.md) for actual results; [CONTRIBUTIONS.md](CONTRIBUTIONS.md) for authorship; [DEMO SCRIPT.md](DEMO%20SCRIPT.md) for walkthrough.

Rules are the simple baseline. AI is unnecessary for this small deterministic task and cannot authorise a change. Native actions require a disposable personally controlledWindowsdevice and appropriate licences/authority. This tool does not prove production competency.
