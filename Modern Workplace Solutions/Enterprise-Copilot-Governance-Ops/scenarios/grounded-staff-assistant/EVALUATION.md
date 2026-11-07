# Evaluation
Date: 7 November 2026. Runtime: 3.11.9; macOS arm64. Automated local execution recorded separately from the learner's own work.
Baseline: permission-filtered extraction without an LLM.
Sample: 10 unittest methods over fixed synthetic examples. All passed; see evidence/tests.txt. Demo output is in evidence/demo.json.
Target: safe outcomes for the listed allowed/refused/unknown or approved/rejected/failure cases.
No real API, tenant, authentication, model or production load was tested. Latency, cost, user adoption, time savings and real security effectiveness are not measured. The role/actor inputs are simulation values, not secure identity.
Next evaluation: learner changes one case and explains a failure; separately run the documented Microsoft extension before claiming integration.
