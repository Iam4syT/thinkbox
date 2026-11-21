# Local evaluation
Five checks against explicit expected routes. Two fictional records are the baseline. The tests measure routing only. No live rollout, time saved or model quality has been established.

Original two rows → P1: HANDOVER REVIEW / P2: GOVERNANCE REVIEW (exit 0)
Changed review input → P1: IMPROVE / P2: GOVERNANCE REVIEW (exit 0)
Duplicate ID → Invalid input: Duplicate ID: P1 (exit 1)
Invalid flag → Invalid input: Check flags must be true or false. (exit 1)
Redundant purpose → P1: RETIRE REVIEW / P2: GOVERNANCE REVIEW (exit 0)
