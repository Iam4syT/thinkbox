# Forecast release gate

## Purpose and source
Train a small regression model and stop release when held-out error or data checks fail.

This is an independent synthetic learning scenario. The selected employer advert requires tested AI/ML components, evaluation and client delivery; no employer-specific incident, data or commissioned work is claimed. Public problem basis: https://www.talan.com/uk/en/careers/offers/detail/744000135541189 (checked 18 October 2026). The repeated need is a hypothesis for consulting teams, not a confirmed Talan internal process.

## Requirements and gaps
R1, R4–R6 and desirable MLOps: data preparation, training, held-out evaluation and a repeatable release decision. This local check is not cloud deployment or a complete MLOps platform.

This strengthens Practised/Project Python and evaluation, plus Developing delivery checks. It cannot establish professional AI experience or the learner’s independent authorship.

## Repeat use and value
A model engineer could run this gate on each model/data change. It helps catch invalid data and degraded held-out results before review. Measure error and the unsafe-release rate on independent cases; no real business saving is established.

## Architecture and technology
Twelve synthetic dated rows enter validation; eight train a one-feature least-squares model, four remain held out. A frozen last-observation baseline is compared with model RMSE, the typical prediction error size. A decision is pass only when error beats baseline and is at most 2 target units. This prints a decision; it never deploys anything.

A learned numerical model is compared with a simpler forecast; generative AI adds no value to this release decision and is deliberately absent. Use a language model only for an optional human-reviewed explanation, never to change the gate.

## Environment cost and time
Python 3.10+ with its standard library, a text editor and local terminal. No package installation, identity account, administrator permission or cloud tenant needed. Check the Python version before use. Allow 60–90 minutes for the basic walkthrough and a further 1–2 hours for your own code change and explanation; these are planning estimates, not measured completion times. No licences beyond the included MIT code licence.

## Step by step lab

### Step 1 Prepare the workspace
Start with the supplied project folder and Python 3.10 or later. Open a terminal, type python3 --version, then cd into this public folder. Run ls and check main.py, requirements.txt and tests are present. Expected: a Python version and those names. If Python is unavailable, install it from python.org; if files are absent, check the folder before continuing.

### Step 2 Read the starting data
Open main.py in a text editor. Find DATA: days 1–12 use target = 2 × feature + 3. Find cut=8. Expected: ordered days and an eight/four split. Check held-out target values are not passed into train(). If split/data differ, restore the original before comparing results.

### Step 3 Run the ordinary path
From the folder, run python3 -B main.py. Expected: train_n 8, holdout_n 4, model_rmse 0.0, baseline_rmse about 5.4772 and release pass. Check each field, not just successful exit. If main.py is missing, return to the project directory; if values differ, inspect source/data changes and do not overwrite the recorded evidence.

### Step 4 Check the simpler baseline
Read baseline_rmse and compare it with model_rmse. Expected: the trained model beats the frozen last-training-target baseline. The baseline never looks at future targets. If the baseline accidentally uses held-out targets, repair it and rerun; do not call leaked evaluation an improvement.

### Step 5 Exercise a real failure
Run python3 -B main.py --drift 10. Expected: model_rmse 10.0 and release hold. This simulates a changed target pattern, not live monitoring. Check the gate is hold even when code runs successfully. If it still passes, inspect the absolute threshold and restore the original check.

### Step 6 Run behavioural checks
Run python3 -B -m unittest discover -s tests -v. Expected: 6 tests and OK. Check the ordinary path, shifted targets, reversed dates, constant features, non-finite values and invalid split/lengths. If a test fails, read its traceback, reproduce that case and fix the cause; do not delete the assertion to obtain a pass.

### Step 7 Break and restore the check
Copy main.py to main.backup. Temporarily reverse DATA with DATA = list(reversed(DATA)) beneath its definition, then run main.py; expect Days must strictly increase. Restore the file and rerun normal/drift paths and all tests. Keep the traceback and recovery output. The tests cover this fault; the manual edit/recovery exercise remains for the learner.

### Step 8 Capture your own evidence
After a successful run, create a new folder named learner-evidence and save commands, date, Python version, outputs and one decision you made. Expected: a traceable record of your own work. Compare source hashes with evidence/source-receipt.json and explain deliberate changes. If no personal run occurred, keep personal execution marked unobserved. A provided test log is not proof that you ran it.

### Step 9 Hand over and clean up
Explain the normal path and one failure to a peer, using the source and results. No account, tenant, API key, subscription or paid resource is needed; recurring cloud cost is £0 for this local exercise. After saving evidence, delete only your temporary main.backup and disposable learner copies if unwanted. Keep source and original evidence. No cloud resources exist to remove; never use broad deletion commands.

## Acceptance and actual evaluation
Six behavioural tests pass. Eight training and four held-out rows give slope 2, intercept 3, model RMSE 0 versus baseline 5.4772 target units; gate pass. Adding a target shift of 10 produces model RMSE 10 and gate hold. Perfect fit follows the deliberately linear synthetic data; it predicts no real forecasting accuracy.
The observed run is assistant-executed on 18 October 2026, Python 3.13.13. Source hashes and exact outputs are under evidence/. The manual fault edit, personal rebuild, unseen-case evaluation and any cloud/API extension remain unrun. An initial test invocation from the workspace root failed because the test path was wrong; the correct project-local invocations passed and are the recorded results.

## Artefacts and interview story
Keep main.py, tests, README, LAB, EVALUATION, CHANGELOG, source receipt and output logs together. Make a short screen recording of your own run only after it happens. Architecture is described in docs/architecture.md. Interview story: explain the repeated problem, the baseline, the access/data boundary, one failure, the verification and what production would require. Do not describe generated source as sole personal authorship or the synthetic numbers as customer results.

## Conditional wording after personal completion
Use only after your own run/change/check is evidenced: “Implemented and evaluated a local forecast release gate using synthetic data, documented a baseline comparison and checked a failure path.” Adjust “implemented” to “reviewed and modified an AI-assisted implementation” where that describes your contribution. LinkedIn wording follows the same boundary; no post is authorised by this guide.

## Next extension
Add a real permitted dataset with a locked chronological holdout, training-only preprocessing and an independent baseline. Use scikit-learn pipelines and model/version tracking after pinning versions. Add scheduled batch checks and reviewed rollback; Azure deployment needs a separate approved sandbox and budget, and is unrun.

## Technical references
https://docs.python.org/3/library/unittest.html — test discovery and assertions, checked 18 October 2026.
https://scikit-learn.org/stable/modules/model_evaluation.html — evaluation metrics and baseline comparison, checked 18 October 2026. This package implements its own tiny standard-library example; it does not claim scikit-learn runtime use.
