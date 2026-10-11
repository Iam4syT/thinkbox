# Marine alert replay

## Outcome

Produce a repeatable local check with explicit expected outputs and failure recovery. Status: assistant-built and locally tested; Bunamin’s independent run remains pending.

## Company context

Independent learning scenario using synthetic data. It is not commissioned client work.

## Requirement and gap mapping

Exercises software testing, data validation, fault diagnosis, clear evidence and safety-conscious judgement. Strengthens developing software integration and operational testing skills. It does not establish marine, mechanical, electrical or safety-critical engineering competence.

## Repeated use and value

A proposed software test engineer could replay these checks after each change. Intended value is finding regressions and making missing or stale information visible. Measure missed expected HOLDs and unexplained output changes. Actual marine safety performance is unestablished.

## Architecture and technology

Operator -> local synthetic scenario JSON -> numeric/age validation -> deterministic teaching rules -> replay.json with recommendation and reason -> human review. Every record includes actuation false. There is no hardware, network, device driver, cloud identity or equipment command.

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

### Step 4 Read the scenario fields

Starting state: data/scenarios.json is unchanged.

Action: Open the file. Review five cases: normal, stale, hot, fast and missing. The age is seconds, temperature is degrees C and speed is knots.

Expected result: One normal record expects REVIEW and four fault records expect HOLD.

Verification: Check each expected value. These thresholds are invented teaching values and require domain review before any real use.

Recovery: Restore the fixture if a case is missing. Never reuse these limits for real equipment.

### Step 5 Replay the cases

Starting state: Five unchanged scenarios are present.

Action: Run python main.py. Open outputs/replay.json.

Expected result: Five results include matches_expected true and actuation false.

Verification: Count one REVIEW and four HOLD results; read each reason, not just the summary flag.

Recovery: If outputs differ, compare the source and fixture. Review every false match before proceeding.

### Step 6 Check boundaries and unsafe inputs

Starting state: Normal replay has been saved.

Action: Run python -m unittest discover -s tests -v. Read the boundary, invalid and no-actuation tests.

Expected result: Eight test methods pass. Exact limits 5 seconds, 80 C and 12 knots yield REVIEW; exceeding a limit yields HOLD.

Verification: Confirm OK. Invalid subcases include missing, negative, Boolean, text, NaN and infinite values.

Recovery: If a limit test fails, inspect greater-than versus greater-than-or-equal behaviour. Do not loosen a safety check to silence a failure.

### Step 7 Break the fixture deliberately

Starting state: Original fixture is preserved.

Action: Copy scenarios.json to data/changed.json. In the normal case change age_seconds to 6 but leave expected as REVIEW. Run python main.py --input data/changed.json.

Expected result: The changed case gives HOLD with reason stale input, and matches_expected false.

Verification: Confirm the disagreement is visible and actuation remains false. The application reports the disagreement; the separate tests remain the release gate.

Recovery: Decide whether the input or expected outcome is wrong. Do not automatically change the expected value to make the replay green.

### Step 8 Recover and prove the repair

Starting state: The altered fixture has a documented discrepancy.

Action: Change age_seconds back to 1 in changed.json. Rerun with --input data/changed.json and rerun all tests.

Expected result: All five replay expectations agree and eight tests pass.

Verification: Record before/after output and explain why the restored value matches the stated rule.

Recovery: If the case still fails, compare field spelling and types; restore the pristine fixture and isolate one change at a time.

### Step 9 Document the authority boundary

Starting state: Happy path, fault and recovery were run.

Action: Create evidence/my-run.md. Record the commands, your own outputs and why REVIEW is advice for a person rather than permission to operate a device.

Expected result: A personal explanation and traceable failure/recovery record exist.

Verification: Verify no record says equipment was stopped or controlled. Both outputs and source keep actuation false.

Recovery: Remove any real vessel, operator or employer details. Label unfinished checks pending rather than claiming a safety result.

### Step 10 Clean up local outputs

Starting state: Your personal evidence is safely copied outside generated outputs.

Action: Exit the environment with deactivate if activated. Delete only this project’s .venv, outputs and deliberately changed fixture copies using the file manager. Preserve source, pristine fixtures and your evidence.

Expected result: Local disposable resources are removed. There are no cloud resources or subscriptions to cancel.

Verification: Check that source and original data remain. A later new environment and run should reproduce the original outputs.

Recovery: If useful evidence was deleted, rerun from the preserved source. Do not delete a parent repository or use a broad recursive cleanup command.

## Acceptance checks

Eight tests pass; all five pristine replay cases match; one normal recommendation is REVIEW and four are HOLD; an altered expected outcome creates a visible mismatch; invalid values fail closed to HOLD; no output operates equipment.

## Evidence and interview story

Keep README, source, fixtures, tests, architecture, actual run output, break/fix notes and a short demo. Explain the problem, limits, design, personal changes, failed case, recovery and intended value. Assistant testing proves this supplied implementation only; Bunamin must reproduce and explain it before making a personal completion claim.

## Conditional career wording

After Bunamin reproduces and explains the work: Built and tested an independent Python scenario-replay tool that checks stale and invalid inputs, threshold boundaries and human-review recommendations using synthetic marine-themed data. No live equipment control or safety certification implied.

## Optional extension

Add structured audit logs, a simple user interface and a versioned rule configuration with change review. An optional AI explanation must quote deterministic reasons and never change HOLD or authorise equipment use. Begin with the non-AI baseline because it is easier to inspect.

## Technical references

Python csv, statistics.linear_regression, venv and unittest documentation, checked 11 October 2026. See https://docs.python.org/3.12/library/csv.html and https://docs.python.org/3.12/library/statistics.html and https://docs.python.org/3.12/library/venv.html and https://docs.python.org/3.12/library/unittest.html. No Rolls-Royce internal technology stack is inferred.
