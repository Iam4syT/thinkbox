# Evaluation —19October2026
Scope: Python standard-library local prototype, synthetic CSV. No tenant/device/ITSM connection.
Baseline: manual reading of four synthetic records against the written policy. The baseline is a reference answer, not measured staff time.
Target: all four expected normal outputs, duplicate/schema/invalid-value rejection and boundary/unknown handling must pass; invalid CLI must exit2 without success JSON.
Observed: four records matched the stated reference, five behavioural tests passed, and one invalid CLI file was rejected with exit2. Test report: evidence/test-results.txt. Output: evidence/example-output.json. This small authored fixture set is not an independent held-out evaluation; no precision/recall, latency, cost saving or real workplace benefit claimed.
Executor: automated local checks in the preparation environment. Bunamin's own rebuild/use has not been observed. Failure recovery: rejected invalid input fixed by returning to sample.csv; no live state to roll back.
Untested: Windows-native execution, physical devices, Microsoft365/AD/Intune access, real ticket queues, concurrent edits, large files, production security and licences. Next: Bunamin reproduce normal and failure case, explain a rule choice, then obtain supervised test-device practice.
Source SHA256: 0590818d25f24145524940bbf986d0468e677ec5f68e4e0fe13d78d96982538f
