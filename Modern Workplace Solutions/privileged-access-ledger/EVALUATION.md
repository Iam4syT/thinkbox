# Evaluation — 18 October 2026

Baseline: manually compare the same small synthetic inputs. No timed human comparison performed. Target: reproducible findings and explicit refusal of unsafe/invalid evidence; zero tenant writes.
Method: 10 behavioural tests plus two CLI fixtures, run locally with Python 3.12.14. Results: 10/10 automated tests passed. Normal CLI exited 0; fault fixture exited 1 as expected. See evidence/. No latency benchmark or financial saving measured. Runtime API cost zero; local compute cost not measured.

Scope: small, authored fixtures, not representative coverage or security certification. The failure path is deliberately introduced. No Microsoft API, tenant policy, actual privilege expiry, sign-in or mailbox outcome was tested. Operator adoption and independent rebuild remain to be demonstrated.
