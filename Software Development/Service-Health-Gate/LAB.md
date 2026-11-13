# Lab 2 Service health release gate

## Need and repeated use

A delivery team needs a repeatable check after each service build or deployment. It needs to see when an endpoint is failing or taking too long. This is a plausible use case for the advertised software testing, DevOps, performance and control responsibilities. It does not depend on any proprietary tooling or data.

## Architecture prerequisites and cost

A local Python command reads a synthetic JSON list of recorded HTTP status and latency. It passes only when every response is 200 and every latency is at most 250 milliseconds. It returns 0 for pass, 1 to hold release and 2 for malformed data. These are exercise thresholds, not a service target. Use Python 3.10+, the supplied public folder and about 30–45 minutes. No deployment, tokens, live requests or cloud costs. Deterministic checks give reproducible output. A later AI summary might group failure patterns, but a plain template is the baseline and any model would require separate evaluation.

## Build and verify

- Open Terminal in this solution’s public folder. Run `python3 --version` and `ls`. Verify main.py, test_main.py and data/sample.json are visible. If files are missing, check your working folder.
- Open data/sample.json and look for status 200 and latency values 110 and 250. Run `python3 -B main.py data/sample.json` followed by `echo $?`. Expect Release checks passed and status 0. The exact threshold counts as a pass.
- Copy the sample to data/broken.json. Change the first status to 503 and the second latency to 251. Rerun the command using the copy and check for both failing rows and status 1. If it passes, verify the file path and saved edits.
- Change the copy to an empty list using []. Run it again. Expect Invalid health data and status 2. Restore the original data from sample.json and confirm status 0. Use only synthetic data.
- Run `python3 -B -m unittest -v`. Expect four tests for boundary behaviour, service failures, empty input and invalid types. If a test fails, read the first error and check the fixture and field types. Add a test for a missing status and ask a peer to review the message and exit code.
- Save your test diff and results with the Python version. Remove data/broken.json and keep the synthetic fixture. No live service needs cleanup.

## Acceptance and interview use

Pass when the four tests pass, the healthy fixture returns 0, the two unhealthy rows return 1 and empty input returns 2. Walk a reviewer through how the command would stop a build, what each status means and why a synthetic latency file cannot establish live service performance. After your own successful run, you could describe a local release check with tested latency boundaries and invalid input handling. A useful extension is to collect outputs from a sandbox service and compare a rolling percentile with a single-run threshold.
