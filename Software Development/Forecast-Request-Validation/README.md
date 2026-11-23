Forecast request validation

A forecast API needs to reject invalid readings before using a model. A deterministic check is cheaper and easier to test than an AI decision for this task.

A synthetic JSON request reaches a Python handler shaped for AWS Lambda. It returns an HTTP-style status and a JSON body. No model or AWS service is invoked.

Run python3 -B check.py in this folder. See LAB.md for the exercise and EVALUATION.md for scope. Codex implemented and tested this offline demonstration.
