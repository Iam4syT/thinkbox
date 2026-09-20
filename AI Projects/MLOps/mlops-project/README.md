# Customer-satisfaction local pipeline

Run the supported local benchmark from this directory with `python demo.py`. Install requirements.txt first. It reads the existing attributed dataset, splits by order, fits preprocessing on the training set, and compares a mean predictor with Ridge regression. Results go to evidence/evaluation.json; no external API or persisted model is required.

The retained model/, steps/, pipelines/ and materializer/ folders contain the earlier ZenML learning project. Their full orchestration/deployment has not been validated in this repair. Historical setup is in [UPSTREAM README.md](UPSTREAM%20README.md); do not treat its old commands as the supported quick start. Read [MIGRATION.md](MIGRATION.md) and [data provenance](data/README.md).
