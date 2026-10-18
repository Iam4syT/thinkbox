# Retrieval evidence workbench

## Purpose and source
Return an allowed source or a refusal for a recurring support question.

This is an independent synthetic learning scenario. The selected employer advert requires tested AI/ML components, evaluation and client delivery; no employer-specific incident, data or commissioned work is claimed. Public problem basis: https://www.talan.com/uk/en/careers/offers/detail/744000135541189 (checked 18 October 2026). The repeated need is a hypothesis for consulting teams, not a confirmed Talan internal process.

## Requirements and gaps
R1–R3, R5–R6: component testing, retrieval, safe agent context and evaluation. The local build covers a retrieval baseline only; LLM prompting, semantic search and agent orchestration remain extensions.

This strengthens Practised/Project Python and evaluation, plus Developing delivery checks. It cannot establish professional AI experience or the learner’s independent authorship.

## Repeat use and value
A support engineer could use a retrieval check after each knowledge/permission change. The recurring friction is finding a relevant source without exposing restricted material. Measure correctness and unauthorised returns on unseen cases; time saved and user benefit are not measured.

## Architecture and technology
A local CLI receives a question and a fixture role; eligible synthetic documents are filtered before keyword scoring; it emits a document citation or null. The role argument is simulated. A real service must derive roles from verified identity and enforce permissions server-side. No network or LLM is used.

A language model might improve natural-language answers, but adds unsupported-answer and access-leakage risks. The current keyword baseline is enough for exact fixture questions. Add AI only after unseen paraphrases show a real retrieval gap, retaining the same access and refusal tests.

## Environment cost and time
Python 3.10+ with its standard library, a text editor and local terminal. No package installation, identity account, administrator permission or cloud tenant needed. Check the Python version before use. Allow 60–90 minutes for the basic walkthrough and a further 1–2 hours for your own code change and explanation; these are planning estimates, not measured completion times. No licences beyond the included MIT code licence.

## Step by step lab

### Step 1 Prepare the workspace
Start with the supplied project folder and Python 3.10 or later. Open a terminal, type python3 --version, then cd into this public folder. Run ls and check main.py, requirements.txt and tests are present. Expected: a Python version and those names. If Python is unavailable, install it from python.org; if files are absent, check the folder before continuing.

### Step 2 Read the starting data
Open main.py in a text editor. Find DOCS and CASES. Identify public-reset, restricted-payroll, public-mfa and the employee/finance fixtures. Expected: three documents and six evaluation cases. Check that there is no personal data. If a record differs, compare the supplied source receipt and restore the fixture before using the recorded baseline.

### Step 3 Run the ordinary path
From the folder, run python3 -B main.py --evaluate. Expected: filtered_keyword correct 6, sample_size 6 and unauthorised_returns 0. Check each field, not just successful exit. If main.py is missing, return to the project directory; if values differ, inspect source/data changes and do not overwrite the recorded evidence.

### Step 4 Check the simpler baseline
Read unfiltered_keyword in the evaluation output. Expected: correct 4 and two unauthorised returns. Compare with filtered_keyword. This isolates filtering, not AI quality. If no difference appears, inspect apply_access and CASES; retain both outputs. Filtering is required before any future LLM sees context.

### Step 5 Exercise a real failure
Run python3 -B main.py --query "IGNORE RULES payroll export" --role employee. Expected: citation null. Then run python3 -B main.py --query "payroll export" --role finance. Expected: restricted-payroll. Check both outputs. If the employee sees that citation, inspect the eligibility filter before restoring the secure path. This checks retrieval permission logic; it does not test an LLM prompt-injection defence.

### Step 6 Run behavioural checks
Run python3 -B -m unittest discover -s tests -v. Expected: 5 tests and OK. Check the ordinary path, invalid role, empty/unknown query and unauthorised retrieval. If a test fails, read its traceback, reproduce that case and fix the cause; do not delete the assertion to obtain a pass.

### Step 7 Break and restore the check
Make a copy of main.py named main.backup. In the original, temporarily replace the access condition with True. Run the same tests; expect the unauthorised retrieval test to fail. Inspect why. Restore main.py from main.backup and rerun until all five pass. Keep the failure and recovery outputs separately. This deliberate fault exercise is a learner instruction and has not been run in this package.

### Step 8 Capture your own evidence
After a successful run, create a new folder named learner-evidence and save commands, date, Python version, outputs and one decision you made. Expected: a traceable record of your own work. Compare source hashes with evidence/source-receipt.json and explain deliberate changes. If no personal run occurred, keep personal execution marked unobserved. A provided test log is not proof that you ran it.

### Step 9 Hand over and clean up
Explain the normal path and one failure to a peer, using the source and results. No account, tenant, API key, subscription or paid resource is needed; recurring cloud cost is £0 for this local exercise. After saving evidence, delete only your temporary main.backup and disposable learner copies if unwanted. Keep source and original evidence. No cloud resources exist to remove; never use broad deletion commands.

## Acceptance and actual evaluation
Five behavioural tests pass. Across six fixed cases, unfiltered keyword retrieval scores 4/6 with two unauthorised returns; filtered retrieval scores 6/6 with zero. This is a deterministic fixture result, not an independent generalisation or security assessment. There is no measured LLM improvement.
The observed run is assistant-executed on 18 October 2026, Python 3.13.13. Source hashes and exact outputs are under evidence/. The manual fault edit, personal rebuild, unseen-case evaluation and any cloud/API extension remain unrun. An initial test invocation from the workspace root failed because the test path was wrong; the correct project-local invocations passed and are the recorded results.

## Artefacts and interview story
Keep main.py, tests, README, LAB, EVALUATION, CHANGELOG, source receipt and output logs together. Make a short screen recording of your own run only after it happens. Architecture is described in docs/architecture.md. Interview story: explain the repeated problem, the baseline, the access/data boundary, one failure, the verification and what production would require. Do not describe generated source as sole personal authorship or the synthetic numbers as customer results.

## Conditional wording after personal completion
Use only after your own run/change/check is evidenced: “Implemented and evaluated a local retrieval evidence workbench using synthetic data, documented a baseline comparison and checked a failure path.” Adjust “implemented” to “reviewed and modified an AI-assisted implementation” where that describes your contribution. LinkedIn wording follows the same boundary; no post is authorised by this guide.

## Next extension
Add embeddings and an LLM behind a replaceable interface, with verified identity before retrieval, cited answers, timeouts and a held-out paraphrase set. Pick a provider and budget first; no paid/API work has been run. Compare answer support, refusals, cost and latency with this baseline. Evaluate attempted instruction injection separately from ordinary retrieval tests.

## Technical references
https://docs.python.org/3/library/unittest.html — test discovery and assertions, checked 18 October 2026.
https://scikit-learn.org/stable/modules/model_evaluation.html — evaluation metrics and baseline comparison, checked 18 October 2026. This package implements its own tiny standard-library example; it does not claim scikit-learn runtime use.
