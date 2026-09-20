# Lab — Learning notes and small experiments

## Prerequisites

Python 3.11 and a clean thinkbox checkout. Use the exact directory `AI Projects/kaggle/agy-cli-projects/bq-releases-notes`. This lab uses permitted local fixtures; no employer system or account is required.

## Steps and verification

1. Read README.md and CONTRIBUTIONS.md to establish scope and the starting point. Expected result: you can identify implemented, simulated and untested components.
2. Follow the README clone/navigation and dependency commands. Expected result: the required imports/build tools load from your environment. If dependencies fail, retain the error and runtime version; do not report a successful run.
3. Run the commands in the README from the designated directory. The supported demo parses a synthetic Atom document without network access. The optional /api/releases endpoint fetches the official BigQuery feed; it is not run by the offline test.
4. Inspect the actual output and [verification record](evaluation.md). Compare the expected normal behaviour with a meaningful failure case: malformed/missing input, unknown metadata, unsupported platform or unavailable integration as applicable. A service-dependent step stays unrun if its prerequisites are absent.
5. Explain the result in plain language. This is a learning area. Reference PDFs are third-party material, not authored portfolio applications. Google Drive/AGY automation is separate and unvalidated here.
6. Record the command, date, environment, source revision, actual output and limitation in CHANGELOG.md/evidence before publishing a new result.

## Recovery and cleanup

Stop a local server with Ctrl-C. Re-run deterministic tests after a change. Remove only your newly generated environment/build/output files when no longer needed; preserve source fixtures and previous evidence. Keep tenant backup/artifact files private. Never perform a bulk tenant action to make a local demonstration look complete.

For a baseline comparison, retain both results even when the simpler approach wins. Distinguish no finding from missing data, and a planned external action from a verified one.
