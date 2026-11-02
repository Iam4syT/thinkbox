# Network KPI forecast lab

## A Purpose and outcome
Build a small Python model that estimates a synthetic network latency measure and compare it with a simple baseline. The output is evidence for a reviewer, never a command to a network.

## B Sourced need and scenario limits
The selected public advert describes graduate support for AI, network-related improvement, testing and cloud/data work. A daily latency-review workflow is a reasoned telecom scenario, not an observed problem at the unnamed client. Client mission, three dated developments, systems and data remain unknown; no operator-specific facts are borrowed. Public sector context and responsibility basis: https://www.techrecruitmentspecialists.uk/job/13/detail/ checked 2 November 2026.

## C Requirement mapping
Practise R01 model development, R04 data projects, R05 network-related analysis, R07 testing and R08 technical notes. Exercise Python, analytical reasoning and a repeatable method. This does not establish telecom integration, real network optimisation or cloud deployment.

## D Evidence gap and ownership
Existing MSc modelling is academic; automated tests, operations and network context need more evidence. This package provides assisted synthetic practice. The supplied local run is assistant-executed. Bunamin must record an own change, reasoning and unseen failure before claiming personal completion. No candidate capability rating changes.

## E Repeated use and baseline
A network analyst could repeat a forecast check on each approved data/model change. Whether this exact workflow is valuable to the client is unverified. Measure error and caught failures before discussing value. Use the last training latency as a frozen baseline; do not use future target values. A learned linear model is the smallest useful ML comparison. A language model adds no value to this numerical decision.

## F Architecture and trust boundaries
Synthetic ordered rows -> strict schema/finite-value validation -> first 16 rows train slope and intercept -> final 8 rows evaluate -> JSON report. Only training targets fit the model. Each test-row load is assumed available at prediction time; the target latency is not. This is a contemporaneous feature-to-latency estimate, not a proven multi-step forecast. There are no identities, external services, network devices or automatic changes. Local filesystem permissions are the only access boundary.

## G Environment and costs
Python 3.10 or newer, a terminal and text editor. Standard library only; no pip install, account, trial, API key, tenant or paid service. Local runtime energy is not measured; no cloud charges are incurred by this path. Allow 60–90 minutes for the walkthrough and 1–2 hours for your own modification; these are estimates. Save the project in a folder you control. Never use customer traffic, identifiers or employer telemetry here.

## H Step by step implementation
### Step 1 Open the correct folder
Starting state: the supplied public scenario is downloaded. In a terminal, change into the folder containing this LAB.md and main.py. Run python3 --version. Expected Python 3.10 or newer. Run ls and check main.py, tests and docs. If a command is missing, fix the runtime or working folder before continuing. Do not install random packages to resolve a path error.

### Step 2 Inspect the data contract
Open main.py. Find DATA with time, load and latency_ms. There are 24 ordered records and latency is deliberately 2 times load plus 10. Confirm no names, IP addresses or subscriber identifiers appear. Expected no personal information and strictly increasing time. If another file contains real data, do not use it for this lab.

### Step 3 Follow the split
Find cut=16 and the train/test assignments. Write down which rows train and which evaluate. Expected 16 training rows and 8 held-out rows. Follow the slope/intercept calculation and confirm it reads train only. A held-out set is data kept out of model fitting so a test can challenge it. If test targets enter fitting, restore separation before evaluating.

### Step 4 Run the normal path
Run python3 -B main.py. Expected slope 2, intercept 10, model_mae_ms 0, baseline_mae_ms 9 and review eligible_for_review. MAE means average absolute error in milliseconds. Check all fields and scope synthetic_local_only. A perfect fit is a consequence of the simple made-up data; it says nothing about accuracy on real networks. If output differs, inspect source changes and preserve the unexpected result.

### Step 5 Compare with the simpler choice
Explain why the frozen last-training observation has error 9 on this increasing sequence. Check the model is required to beat the baseline and stay within an absolute 3 ms threshold. These thresholds are lab design choices, not telecom service promises. If a baseline wins on a future dataset, retain it and investigate instead of forcing an AI recommendation.

### Step 6 Inject changed behaviour
Run python3 -B main.py --drift 20. Expected model_mae_ms 20 and review hold. The added offset affects held-out targets only; this imitates a shift in behaviour. Check slope/intercept remain 2 and 10. If they change, investigate leakage. This is a repeatable fault simulation, not a live drift detector.

### Step 7 Run meaningful tests
Run python3 -B -m unittest discover -s tests -v. Expected 9 test methods and OK. Tests challenge time ordering, non-finite/negative input, unexpected fields, constant features, invalid splits, changed targets and baseline behaviour. Some methods contain several cases. On failure, read the traceback and reproduce the failed input. Fix the cause; do not remove assertions.

### Step 8 Make and recover one fault
Copy main.py to a temporary main.backup. In DATA, make the second time equal to the first; run the program and expect time must strictly increase. Restore main.py from the backup, rerun normal and drift commands and all tests. Check the original evidence stays unchanged. This manual exercise is for the learner and is not counted as already performed.

### Step 9 Record an own design change
Create learner-evidence. Choose one justified change, such as adding a median baseline for a noisy series. Explain why before editing, add one unseen failure fixture and run the suite. Save date, Python version, changed source hash and actual output. Expected a personal decision plus reproducible evidence. Existing supplied logs are not your own execution.

### Step 10 Document handover and clean up
Write a short architecture note explaining data ownership, known-at-prediction inputs, baseline, error limit, rollback to the baseline and the person who would review it. Keep originals and your results. Remove only your temporary backup when no longer needed. No cloud resources exist to delete. Do not run broad directory removal commands.

## I Break and fix checklist
Duplicate/out-of-order time -> reject before fitting -> restore order -> all tests pass. NaN or an extra customer field -> reject the schema/value -> replace with approved synthetic records -> rerun. Target shift -> hold -> diagnose data/model change, never lower the threshold merely to pass. Constant training load -> reject -> provide a meaningful training set or keep the baseline.

## J Acceptance and evaluation
Normal output matches the documented split and coefficients. Drift holds; data contract failures are rejected. All 9 behavioural test methods pass in the supplied automated run. The sample is 24 artificial rows, 16 train and 8 test; there is no external validation, latency benchmark or measured business gain. Native cloud and learner execution remain unrun.

## K Artefacts
Keep main.py, tests, LAB, README, evaluation, source receipt and normal/failure output together. Record your own short demo only after completing it. Use docs/architecture.md to explain the trust boundary. Never publish raw customer data or private application records.

## L Interview story
Explain the repeated decision, small synthetic scope, chronological separation, simpler baseline, deliberate failure and evidence. State that actual network integration needs domain review, permitted data, observability and authorised deployment. Describe your own change accurately; do not claim sole authorship of assisted code.

## M Conditional wording
Use only after personal completion is evidenced: Reviewed and modified an AI-assisted Python KPI model, compared a held-out result with a simple baseline and demonstrated rejection of invalid data. Do not use production, telecom deployment or savings wording. The new scenario is excluded from the current CV.

## N Next extension
With permitted data, lock a chronological holdout, choose a baseline suited to operational cycles and evaluate across realistic shifts. Only then consider a reviewed cloud batch job with monitoring and rollback. Azure is an optional learning choice, not an advertised vendor requirement. No tenant creation or paid resource is authorised by this guide.

## Technical sources
Python unittest official documentation https://docs.python.org/3/library/unittest.html checked 2 November 2026. The numerical example is original standard-library code; it does not claim TensorFlow or scikit-learn use.
