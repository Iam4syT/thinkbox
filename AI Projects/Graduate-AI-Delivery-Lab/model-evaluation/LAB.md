# Repeatable model evaluation and group-error review

## A Outcome
Compare a small predictor against a simple baseline, then hold it for review when overall or group errors are too high.
## B Research basis
The selected public graduate role includes data/model work and trustworthy systems. Actual client product is unknown. A team's recurring need to review model changes is a reasoned scenario, not an observed client process. No proprietary system is reproduced.
## C Requirements exercised
Model preparation/training/evaluation, software testing, responsible AI and maintainable Python (E2–E5, R1,R2,R6–R8). This basic regression is an ML teaching model; it is not an LLM or TensorFlow performance demonstration.
## D Gap addressed
Build practice in repeatable tests and group-level error inspection. Existing academic modelling remains separate; this guide does not upgrade personal capability or satisfy strong fairness expertise by itself.
## E Recurring value
A developer repeats evaluation for every change. A stable baseline and an explicit hold prevent a promising average from hiding a bad subgroup. No real time saving, adoption or fairness benefit is measured.
## F Architecture and baseline
Synthetic rows -> schema/time checks -> first 10 training rows -> fitted linear predictor -> last 6 held-out rows -> overall/group errors -> review or hold plus fingerprint. Groups a/b are arbitrary synthetic cohorts, not demographic attributes. Training-mean predictor is the simpler baseline. The fitted line must beat it; if it does not, retain the simpler model. No system authorises deployment.
## G Environment
Status: locally implemented learning demo. Guides and implementation prepared with AI assistance; the private evidence record separates implementation tests from Bunamin's own execution and explanation. No client work, live system or production outcome. Python 3.11 standard library only; no cloud account, paid API, licence purchase or external dataset. Budget £0 excluding existing device/internet; estimated learner time one focused weekend per lab, not a measured duration. Use only synthetic data. Do not enter personal/client information. Intended for individual learning on an isolated machine.

## H Implementation and walkthrough
Step 1 Starting state: terminal open, downloaded model-evaluation folder. Run `python3 --version`, then change into the folder containing demo.py and tests. Run `ls`. Expected Python 3.11 and those files. If missing, correct folder/runtime; no packages need installing. Windows may use `py -3.11` instead of python3. Record the command used.

Step 2 Open demo.py in an editor. Read fixture:16 invented rows, x0–15, y=2x+10; groups alternate a/b. Time increases. Check that the first 10 train and last 6 test are separate. Expected training target mean 19. If your input differs, preserve it separately and check schema before comparing outputs.

Step 3 Run `python3 -B demo.py --output evidence/normal.json`. Expected slope 2, intercept 10, train_n 10, test_n 6, model_mae 0, baseline_mae 16, group_gap 0 and decision review. MAE means average absolute prediction error in made-up units. Open the saved JSON and verify every value. A perfect score is caused by simple synthetic data, not evidence of commercial performance. If it differs, check uncommitted data/code changes and keep the unexpected output.

Step 4 Read evaluate. Mean and coefficients use training rows only. Test data supplies errors, never fitted parameters. Write a short explanation of why fitting on all 16 rows would leak the answer into the test. Expected explanation names a future observation influencing training; if unclear, draw the split before proceeding.

Step 5 Run `python3 -B demo.py --group-shift 20 --output evidence/group-shift.json`. Expected overall MAE10, group a MAE0, group b MAE20, gap20 and hold. Check slope/intercept remain2/10. This is an imposed shift, not an automatic real-world drift detector. The different errors flag investigation; they do not prove illegal discrimination or a valid fairness definition.

Step 6 Run `python3 -B -m unittest discover -s tests -v`. Expected 10 test methods and OK. Read test names: chronological ordering, target leakage, non-finite/bool input, constant feature, insufficient groups, unexpected fields, split and fingerprint changes. On failure, reproduce the exact input and repair the cause. Do not weaken a check to pass.

Step 7 In a separate copy, remove a group's test rows and call evaluate on that input in a Python shell, or use test_missing_group. Expected ValueError. Restore the input. Check that an under-sampled group is not presented as a reliable zero-error score. Two rows per group is only a toy minimum, not a statistical assurance standard.

Step 8 Record a model card: intended use synthetic illustration; prohibited use live decisions; row counts; split; baseline; group definition; error thresholds; source fingerprint; failure cases; limits. Threshold5 is a chosen teaching rule, not a client tolerance or universal fairness threshold. Ask who would set an appropriate threshold in a real product.

Step 9 Review normal and shifted outputs together. Expected review versus hold. No deploy action exists. Explain why a human should inspect error reasons, data provenance and affected users before a release. If only the average looks good, check every group before deciding.

Step 10 Save your own code diff, rerun output, environment and explanation. Ask a reviewer to give an unseen group-shift fixture. Expected correct prediction that coefficients stay fixed while held-out errors change. Personal completion requires this execution; supplied assistant output alone is insufficient.
## I Break/fix
Duplicate a timestamp: reject ordering; restore strict time order and rerun. Set a feature to NaN: reject non-finite data; restore a number. Make all training features constant: reject zero variance; restore varying data. Shift group b: hold; investigate data/label relationship rather than dropping b. Retain before/after outputs.
## J Acceptance
Normal numbers and hold case match; all 10 tests pass; no train/test target leakage; missing group/data error rejected; own explanation records tiny-sample and fairness limits. This supports local numerical behaviour only. No latency, carbon, monetary saving or business fairness gain measured.
## K Artefacts and cleanup
Keep source, tests, model card, normal/shift JSON, your diff and short demo. Delete only scratch copies and generated evidence after preserving wanted outputs. No tenant resources or subscriptions exist. Restore edited fixtures before the final rerun.
## L Interview story
Problem repeated evaluation; constraint tiny synthetic dataset; design simpler baseline and holdout; build explicit checks; failure subgroup shift; verification normal plus failure tests; intended value clearer review; next step permitted realistic data and domain-approved error rules. Describe your actual contribution and what you personally ran.
## M Conditional CV/LinkedIn wording
Use only after completion and personal evidence: Built and tested a synthetic Python evaluation workflow comparing a linear model with a mean baseline and checking group-level prediction errors. Do not claim deployment, business impact or a fairness certificate.
## N Extension
Replace the toy line with a scikit-learn or TensorFlow model only after justifying complexity, pinning dependencies, preserving temporal separation and evaluating a permitted larger sample. Add confidence intervals and domain-defined group checks. Not built or tested here.
## Sources
Public selected advert informs private mapping only; no client commission. Python 3.11 unittest documentation: https://docs.python.org/3.11/library/unittest.html, checked2 November 2026. Numerical method is original standard-library code.
