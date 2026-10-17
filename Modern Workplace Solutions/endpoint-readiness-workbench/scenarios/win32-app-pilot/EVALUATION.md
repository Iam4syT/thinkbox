# Evaluation on 17 October 2026

Codex ran Python 3.11.9 standard-library tests and the README example on macOS. 7/7 tests passed; exact output in evidence/test-output.txt and example-output.json. Fixtures cover a normal path and explicit invalid/scope/failure cases. Test-run seconds are incidental harness output, not a measured human efficiency gain.

Baseline: manual inspection of the fixed synthetic package/events. Target: agreement with expected states and rejection of unsafe/malformed inputs. Actual: all named fixture expectations passed. No independent human baseline timing, native execution, tenant integration, Windows syntax execution or Bunamin reproduction was measured. Native CMD and PowerShell scripts are reviewed source only. A Python detection model is not a validated Intune detection rule. Real pilot/collection/rollback/learner evidence remains pending in LAB.md.
