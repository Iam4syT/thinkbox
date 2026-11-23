Course answer review

An assistant can return a plausible course answer without enough evidence. A fixed rule can decide which responses need human review. It cannot judge whether a paraphrase is true.

A synthetic catalogue and a candidate answer enter a Python review function. Only matching facts from the approved entry pass. Unknown courses and unsupported facts go to a person. No model, personal data or external calls.

You need Python 3 and the two supplied files, solution.py and check.py. Use a local folder. The offline run needs no account, keys, paid licence or cloud budget. Allow 15 minutes.

1. Open a terminal in the public folder. Run python3 --version and confirm Python 3. If the command fails, use an installed Python 3 interpreter.

2. Open solution.py and trace the sample from its inputs to its return value. Open check.py and predict the first valid result and the first rejected result.

3. Run python3 -B check.py. Expected output: 6 course answer checks passed. A traceback identifies the first unmet expectation. Read that assertion before changing anything.

4. Change only the course duration in the proposed answer. Predict human review and inspect the source difference. If a link alone passes, restore the full field comparison.

5. Restore your changed fixture and run all checks again. Save the command and output with the version of the code. A passing run covers these fixtures only.

6. Close the terminal. If you made a temporary copy, remove that copy only. No cloud resources were created.

Observed result: 6 course answer checks passed. Codex ran these synthetic checks. Independent learner reproduction is pending.
