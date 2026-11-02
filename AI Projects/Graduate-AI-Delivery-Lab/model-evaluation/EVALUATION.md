# Evaluation

2 November 2026; Python 3.11.9; automated local run. python3 -B demo.py: exit 0; evidence/run-1.txt
python3 -B demo.py --group-shift 20: exit 0; evidence/run-2.txt
python3 -B -m unittest discover -s tests -v: exit 0; evidence/run-3.txt

10 test methods per solution. Tiny synthetic samples; no production/generalisation/business claim. Personal rerun/change/explanation pending. Baseline and failure details are in LAB.md; raw outputs in evidence. No latency/cost/time-saving claim. HTTP tests use real loopback sockets, not a cloud deployment.
