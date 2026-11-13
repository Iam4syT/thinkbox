# Lab 1 Synthetic ledger validator

## Need and repeated use

A team handling money-related records needs a quick, repeatable check before accepting a batch. That is a plausible banking scenario. The vacancy explicitly asks for maintainable code, reliable unit testing, secure handling and risk controls. This lab builds a small evidence sample for those criteria. It uses an artificial rule that each account’s entries must net to zero. Real ledgers can use different reconciliation rules.

## Architecture prerequisites and cost

A local command reads CSV, validates columns and unique entry IDs, sums signed integer pence per account and returns 0 for balanced, 1 for unbalanced and 2 for invalid input. Unit tests call the pure reconciliation function. Use Python 3.10 or later, a terminal and the supplied public folder. No packages, credentials, tenant, licence purchase or cloud cost are required. Allow 30–45 minutes. Use only the supplied synthetic data. Rules are easier to audit than an AI judgement on arithmetic. AI might help explain failure summaries later, but any summary would need a privacy review and a comparison against templated messages.

## Build and verify

- Open Terminal in this solution’s public folder. Run `python3 --version` and `ls`. Expect Python 3.10+ and main.py, test_main.py and data. If Python is missing, install it through your approved environment before proceeding.
- Open data/sample.csv. Confirm the header reads id,account,pence and accounts A and B each have two offsetting entries. Run `python3 -B main.py data/sample.csv` and then `echo $?`. Expect Balanced and status 0. If the path fails, run `pwd` and check that you are in public.
- Copy the CSV to data/broken.csv. Change account A’s -1250 entry to -1200. Run `python3 -B main.py data/broken.csv` and then `echo $?`. Expect A to have an imbalance of 50 and status 1. If it still passes, check that you ran the copy.
- Restore the amount in broken.csv and change the second ID to 1. Rerun and check status 2 with a duplicate-entry message. Restore the ID and change the amount to invalid. Check status 2 again. Restore the amount and check that the original run passes.
- Run `python3 -B -m unittest -v`. Expect four passing tests for balance, separate accounts, duplicate ID and malformed amount. If any fail, compare exact input and output before changing validation logic. Add your own blank-file or invalid-header test and have a peer review the change.
- Save the command outputs and your test diff with the date and Python version. Delete data/broken.csv when done. Keep the supplied fixture and source. Store no personal financial data.

## Acceptance and interview use

Pass when the four supplied tests pass, the deliberate imbalance and duplicate produce their expected exit codes, and another person can run the commands from the README. The demo is two minutes. Explain why pence are integers, show the balanced batch, make the 50-pence change, then explain how a later pipeline could hold the batch and route it for review. After your own build and review, you could describe a synthetic reconciliation project with explicit input validation and unit tests. Only report the runs and changes you performed. A useful extension is a streaming parser and tests for file-size limits.
