# Energy forecast checks

## Outcome

Produce a repeatable local check with explicit expected outputs and failure recovery. Status: assistant-built and locally tested; Bunamin’s independent run remains pending.

## Company context

Independent learning scenario using synthetic data. It is not commissioned client work.

## Requirement and gap mapping

Exercises data analysis, AI evaluation, continuous learning and the design-test-review part of the engineering lifecycle. Strengthens academic modelling into reproducible software checks. It does not establish industrial energy forecasting, production AI or plant-operation experience.

## Repeated use and value

A proposed energy analyst could rerun the checks for each permitted data refresh. Intended value is catching invalid data and weak forecasts before a planning review. Measure forecast error on representative unseen data and the number of rejected bad inputs. Actual employer demand and cost savings are unknown.

## Architecture and technology

Operator -> validated local CSV -> first eight rows for training -> next four rows for testing -> previous-observation baseline and fitted straight-line forecast -> local metrics.json -> human review. The baseline uses the last observed value available before each forecast. The fitted model uses training rows only. No identity provider or service account is needed.

## Prerequisites and cost

Python 3.10 or newer, terminal and text editor; 0 GBP incremental service cost on an existing computer. Standard library only, no installation of packages, credentials, tenant or device access. Allow about two to four hours per lab for a first personal run; this is an estimate, not measured time.

## Granular lab

### Step 1 Open an isolated project folder

Starting state: A downloaded copy of this package is available.

Action: Open a terminal. Use cd followed by a space, drag this project folder into the terminal and press Enter. Run pwd on macOS or Get-Location in PowerShell.

Expected result: The current folder contains main.py, src, data and tests.

Verification: Run python3 -c "from pathlib import Path; print(Path('main.py').exists())". Expect True. Windows may use py instead of python3.

Recovery: If False, navigate into the project folder, not its parent. Do not run inside an employer system.

### Step 2 Check Python and create the environment

Starting state: The terminal is inside the project folder.

Action: Run python3 --version. Use Python 3.10 or newer. Run python3 -m venv .venv. On macOS run source .venv/bin/activate. On Windows use .venv\Scripts\python.exe for each python command if activation is blocked.

Expected result: An isolated local Python environment exists. No cloud account, API key or paid licence is needed.

Verification: Run python -c "import sys; print(sys.prefix != sys.base_prefix)". Expect True.

Recovery: If Python is missing, install a supported Python release from python.org and reopen the terminal. Do not lower organisation security settings to activate an environment.

### Step 3 Review the implementation and its limits

Starting state: Python is ready and source files are present.

Action: Open src/engine.py and data in a text editor. Read CONTRIBUTIONS.md and docs/architecture.md. Confirm that only local fixture files are read and outputs are written locally.

Expected result: The operator understands the input fields, outputs and teaching boundaries.

Verification: Search the source for network requests, passwords and device commands. None are required. Explain the input and output in your own words.

Recovery: Stop if downloaded files differ from the described scope. Use a fresh verified copy; never add real customer, tenant or equipment data.

### Step 4 Inspect the fixture

Starting state: data/demand.csv is unchanged.

Action: Open the CSV. Confirm the header hour,demand_kw and twelve rows, from hour 0 with 100 kW to hour 11 with 155 kW.

Expected result: A deliberately simple rising-demand sequence is available.

Verification: Count twelve records, check strictly increasing hours, and confirm that all values are finite and non-negative.

Recovery: Restore the original CSV if the header or values differ. These are synthetic hourly values, not real sensor measurements.

### Step 5 Run the baseline and model

Starting state: The original fixture is present.

Action: Run python main.py. Open outputs/metrics.json.

Expected result: Eight training rows, four testing rows, persistence_mae_kw 5.0 and trend_mae_kw 0.0.

Verification: Check train_end_hour 7.0, slope 5.0 and intercept 100.0. MAE means the average absolute forecast error, measured here in kW.

Recovery: If outputs differ, check the input file and Python version. Rerun from a fresh copy. Zero toy error does not establish real-world accuracy.

### Step 6 Verify separation of training and testing

Starting state: Baseline output is saved.

Action: Run python -m unittest discover -s tests -v. Read test_future_does_not_change_fit. It changes a future value to 900 and checks the fitted parameters stay the same.

Expected result: Eight test methods pass, including a check that future test data cannot change the trained model.

Verification: Confirm OK and eight tests. Keep terminal output as evidence.

Recovery: If a test fails, read the assertion and compare source/fixture versions. Fix the underlying split or input issue rather than changing the expected result.

### Step 7 Reject a faulty input

Starting state: The original fixture is preserved.

Action: Copy data/demand.csv to data/bad.csv. Change the first demand value to -1. Run python main.py --input data/bad.csv.

Expected result: The command fails with a clear finite/non-negative-value error.

Verification: Confirm that the invalid input did not produce a new valid forecast. A previous outputs/metrics.json may still exist and must not be treated as this failed run.

Recovery: Restore the value or remove data/bad.csv. Rerun the original fixture and confirm the normal metrics.

### Step 8 Test an unseen change honestly

Starting state: Original results are recorded.

Action: Make data/changed.csv as a copy. Change hour 11 demand to 900. Run python main.py --input data/changed.csv.

Expected result: The fitted slope and intercept stay 5 and 100 while forecast error rises.

Verification: Check train_end_hour stays 7; trend MAE becomes 186.25 kW. This shows the simple model can fail on a change outside its pattern.

Recovery: Check that only the final row changed. Record failure rather than claiming the linear model generalises. Restore the original run for a baseline comparison.

### Step 9 Write a short handover

Starting state: Happy path and both failure cases were run.

Action: Create evidence/my-run.md with your own date, Python version, commands, outputs, interpretation and one design decision. Explain why the test tail was kept out of training.

Expected result: A personal reproduction record distinguishes your work from assistant-supplied code.

Verification: Keep original data, changed fixture, test log and output together. Do not copy assistant results as your own run.

Recovery: If any step was not run, label it pending. Avoid time-saving, energy-saving or commercial-performance claims.

### Step 10 Clean up local outputs

Starting state: Your personal evidence is safely copied outside generated outputs.

Action: Exit the environment with deactivate if activated. Delete only this project’s .venv, outputs and deliberately changed fixture copies using the file manager. Preserve source, pristine fixtures and your evidence.

Expected result: Local disposable resources are removed. There are no cloud resources or subscriptions to cancel.

Verification: Check that source and original data remain. A later new environment and run should reproduce the original outputs.

Recovery: If useful evidence was deleted, rerun from the preserved source. Do not delete a parent repository or use a broad recursive cleanup command.

## Acceptance checks

Eight tests pass; original output has 8/4 chronological split and MAE 5/0; negative and non-finite values are rejected; the 900 kW change affects error, not fitted parameters; no live services or personal data are used.

## Evidence and interview story

Keep README, source, fixtures, tests, architecture, actual run output, break/fix notes and a short demo. Explain the problem, limits, design, personal changes, failed case, recovery and intended value. Assistant testing proves this supplied implementation only; Bunamin must reproduce and explain it before making a personal completion claim.

## Conditional career wording

After Bunamin reproduces and explains the work: Built and tested an independent Python forecast-evaluation exercise with a chronological holdout, persistence baseline and invalid-input checks on synthetic energy data. State the actual personal contribution and date; exclude toy accuracy as a commercial result.

## Optional extension

Replace the straight-line fixture with permitted representative data, add a held-out seasonal period and compare a justified ML model against persistence. Specify deployment monitoring and a human review threshold before considering any cloud service. Paid services and live systems are outside this lab.

## Technical references

Python csv, statistics.linear_regression, venv and unittest documentation, checked 11 October 2026. See https://docs.python.org/3.12/library/csv.html and https://docs.python.org/3.12/library/statistics.html and https://docs.python.org/3.12/library/venv.html and https://docs.python.org/3.12/library/unittest.html. No Rolls-Royce internal technology stack is inferred.
