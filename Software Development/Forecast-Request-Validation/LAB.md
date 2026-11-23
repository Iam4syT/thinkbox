Forecast request validation

A forecast API needs to reject invalid readings before using a model. A deterministic check is cheaper and easier to test than an AI decision for this task.

A synthetic JSON request reaches a Python handler shaped for AWS Lambda. It returns an HTTP-style status and a JSON body. No model or AWS service is invoked.

You need Python 3 and the two supplied files, solution.py and check.py. Use a local folder. The offline run needs no account, keys, paid licence or cloud budget. Allow 15 minutes.

1. Open a terminal in the public folder. Run python3 --version and confirm Python 3. If the command fails, use an installed Python 3 interpreter.

2. Open solution.py and trace the sample from its inputs to its return value. Open check.py and predict the first valid result and the first rejected result.

3. Run python3 -B check.py. Expected output: 7 forecast request checks passed. A traceback identifies the first unmet expectation. Read that assertion before changing anything.

4. Change the valid reading from 450 to -1. Predict 400 before running it. If True passes, check that the type guard excludes Boolean values.

5. Restore your changed fixture and run all checks again. Save the command and output with the version of the code. A passing run covers these fixtures only.

6. Close the terminal. If you made a temporary copy, remove that copy only. No cloud resources were created.

Observed result: 7 forecast request checks passed. Codex ran these synthetic checks. Independent learner reproduction is pending.
