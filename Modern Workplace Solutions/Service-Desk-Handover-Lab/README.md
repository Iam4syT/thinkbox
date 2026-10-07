# Service desk handover lab

A synthetic offline learning tool for support analysts. No live ITSM, patient data or tenant access. Python 3.10 or later, standard library only. Run `python3 -m unittest -v`, then `python3 triage.py triage sample.json output.json`.

See [LAB.md](LAB.md) for steps, [EVALUATION.md](EVALUATION.md) for actual fixture results and [CONTRIBUTIONS.md](CONTRIBUTIONS.md) for authorship. A human confirms impact, authority and every remediation.

## Additional strict record-validation scenario
See [strict-record-validation](scenarios/strict-record-validation/README.md) for an isolated synthetic schema/checklist exercise with explicit invalid-input handling. Existing workflow remains unchanged.
