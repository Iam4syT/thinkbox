# M365 service review

A small independent learning demo for a support engineer's recurring service-health and usage review. Status: evaluated synthetic local slice. Live integration, personal independent operation, AI and workplace impact remain unestablished.

## The recurring problem

A useful review needs current observations and a named next action. Missing or stale data must remain visible; a provider incident does not establish a local root cause. This demo standardises a readable checklist around four workloads, activity, storage and a declared audit window. It is not a production monitoring service or commissioned customer work.

## Contribution and current scope

Bunamin authorised the learning brief. Codex wrote and ran the standard-library Python demo, synthetic fixtures, behaviour tests and documentation. Read [CONTRIBUTIONS.md](CONTRIBUTIONS.md) before interpreting the result as personal capability.

| Component | State | Evidence |
|---|---|---|
| Deterministic local review and missing-data boundaries | Implemented and tested on synthetic input | [Source](scripts/review.py), [tests](tests/test_review.py) |
| Normal and review snapshots | Simulated | [Fixtures](templates/healthy.json), [run record](evidence/run-metadata.json) |
| Graph/usage/audit collection | Planned and unrun | [Adapter boundary](docs/adapter.md), [lab](LAB.md) |
| AI incident explanation | Planned, no calls or measured benefit | [Lab extension](LAB.md) |

## Run a small example

Python 3.11 or newer; no package installation, token or cloud account. From a thinkbox clone:

```sh
cd "Modern Workplace Solutions/m365-service-review"
python3 -m unittest discover -s tests -v
python3 scripts/review.py templates/healthy.json --as-of 2026-09-30T09:00:00Z
python3 scripts/review.py templates/review.json --as-of 2026-09-30T09:00:00Z
```

Windows may replace python3 with py -3. The normal fixture returns NO_RULE_FINDINGS and exit 0. The intentionally problematic fixture returns REVIEW and exit 1 with five findings. Invalid/missing/unknown observations return INCOMPLETE or an error and exit 2. The clock is fixed for reproducibility; it is not a live service timestamp. No rule findings is not proof of tenant health or security.

## Design and results

The simpler baseline is a manual review checklist. Readable rules retain missing-data boundaries and human judgement. AI is optional only if a later, grounded explanation beats a template baseline. On 30 September 2026, 14 behaviour tests passed; the two synthetic CLI scenarios returned their expected states. This is not a comparative time study or a customer outcome. See [EVALUATION.md](EVALUATION.md), [architecture](docs/architecture.md) and the [demo script](DEMO%20SCRIPT.md).

## Learn, reuse and clean up

Follow [LAB.md](LAB.md) for novice steps, break/fix, prerequisites and cleanup. A future collector needs permitted test-tenant access, complete source reconciliation, role/licence checks and private handling of exports. The current program reads local files and prints a report; it cannot change a tenant. Keep real identities, tenant exports and tokens out of the public package. Delete only your scratch fixtures when finished.

Original code follows the [MIT licence](LICENSE); linked vendor documentation retains its own terms. [CHANGELOG.md](CHANGELOG.md) records the actual scope and remaining work.
