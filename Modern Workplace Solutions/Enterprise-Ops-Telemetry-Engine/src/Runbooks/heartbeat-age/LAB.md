# Lab 1 • Is the site heartbeat fresh?
At handover, an operator must tell a fresh device report from a stale one. This exercise models monitoring across sites. The input is elapsed minutes since the last report. A fixed threshold is easier to audit than an AI prediction for this decision.
### Set up
Allow 15 minutes. Open a terminal in the exercise folder containing check.py and test_check.py. Run python3 --version. Use Python 3.8 or newer. The standard library is sufficient. No accounts, licence fees or network calls are required.
### Run and investigate
1. Open check.py. Find the five-minute threshold. Before running the rule, write down what you expect for 2, 5 and 6 minutes.
2. Run python3 -B -c "from check import heartbeat; print([heartbeat(x) for x in (2,5,6,None,-1)])". Expect fresh, fresh, investigate, review input, review input. Match each label to its input.
3. Break/fix: in a disposable copy, change > 5 to >= 5. Run the tests below. The boundary test should fail because exactly five minutes is allowed. Restore > 5 and check that the test passes again.
### Check, explain and extend
Run python3 -B -m unittest -v test_check. Compare every named test with its expected decision. Save the console output with the date. If an import fails, check that both files are in the current folder. Work on a copy for experiments. Restore the supplied files and rerun the tests after changing a rule. No external resources need cleanup.
Six automated checks passed locally. A stale report is a reason to investigate. It cannot tell you whether a link, clock or device failed. Real monitoring agents and time synchronisation remain untested.
After personal replication, explain why missing data needs its own result. Conditional portfolio line: “Tested a heartbeat rule against six synthetic cases.” Next add time-stamped samples and test clock skew before considering alert delivery.
