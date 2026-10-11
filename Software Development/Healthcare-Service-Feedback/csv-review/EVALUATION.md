# Local evaluation
11 October 2026, Python 3.12.14. Codex executed 8 behaviour tests successfully and one normal CLI run using 4 synthetic rows. Test names and actual output: [tests](evidence/tests.txt), [report](evidence/demo.json). No elapsed time, cost saving or operational accuracy measured.
Manual expected baseline: Manually read four rows and count each category. Expected counts: access 2, workflow 1, report 1. The automated report must reproduce these counts and identify S002 missing evidence and S003 safety/owner actions. No time-saving measurement performed.
The rule report matched the stated sample expectations. Automated checks exercise failure cases; Bunamin’s manual break/fix walkthrough and personal explanation remain pending. No live SystmOne, clinical data, cloud deployment, real launches or hosted CI executed.
Next validation: independent reviewer marks ten new synthetic records; compare decisions and record all disagreements.
