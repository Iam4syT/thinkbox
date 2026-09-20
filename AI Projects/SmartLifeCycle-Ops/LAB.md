# Lab — SmartLifeCycle Ops — endpoint and ML lab

## Prerequisites

Python 3.11 and a clean thinkbox checkout. Use the exact directory `AI Projects/SmartLifeCycle-Ops`. This lab uses permitted local fixtures; no employer system or account is required.

## Steps and verification

1. Read README.md and CONTRIBUTIONS.md to establish scope and the starting point. Expected result: you can identify implemented, simulated and untested components.
2. Follow the README clone/navigation and dependency commands. Expected result: the required imports/build tools load from your environment. If dependencies fail, retain the error and runtime version; do not report a successful run.
3. Run the commands in the README from the designated directory. 2,500 synthetic records; 2,000 training and 500 test rows. The generating rule is the baseline. A fresh small model is built in memory; no committed pickle is loaded.
4. Inspect the actual output and [recorded evaluation](evidence/evaluation.json). Compare the expected normal behaviour with a meaningful failure case: malformed/missing input, unknown metadata, unsupported platform or unavailable integration as applicable. A service-dependent step stays unrun if its prerequisites are absent.
5. Explain the result in plain language. No Intune, JAMF or directory changes. The class probability describes synthetic labels; it is not real device-failure risk.
6. Record the command, date, environment, source revision, actual output and limitation in CHANGELOG.md/evidence before publishing a new result.

## Recovery and cleanup

Stop a local server with Ctrl-C. Re-run deterministic tests after a change. Remove only your newly generated environment/build/output files when no longer needed; preserve source fixtures and previous evidence. Keep tenant backup/artifact files private. Never perform a bulk tenant action to make a local demonstration look complete.

For a baseline comparison, retain both results even when the simpler approach wins. Distinguish no finding from missing data, and a planned external action from a verified one.
