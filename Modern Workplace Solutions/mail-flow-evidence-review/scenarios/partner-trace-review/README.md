# Partner mail evidence review
Independent offline learning scenario maintained by Bunamin Adams. Interpret four synthetic mail observations and keep diagnostics subject to approved access. No employer deployment, live integration or AI service.

## Run and inspect
Python3.10 or later, standard library only. From this scenario folder:
```
python3 -m unittest discover -s tests -v
python3 scripts/review.py fixtures/sample.json
```
See [LAB.md](LAB.md) for exact expectations, fault recovery and cleanup; [EVALUATION.md](EVALUATION.md) for actual results; [CONTRIBUTIONS.md](CONTRIBUTIONS.md) for scope; [architecture](docs/architecture.md) and [demo](DEMO%20SCRIPT.md). Input is synthetic, not a Microsoft export adapter. A passing checklist is not factual validation or authorisation. Independent learner completion and native tests remain pending. Rules give a simpler inspectable baseline than AI; no time or business improvement measured.
