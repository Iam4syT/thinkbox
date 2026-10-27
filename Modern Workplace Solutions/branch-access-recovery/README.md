# Branch access: DNS, permissions and recovery

Independent support-learning scenario. Offline rules are implemented and evaluated on 5 synthetic records. Device/Windows/VM operations remain unrun; no client system or measured business result is claimed.

Intended user: a support engineer checking evidence before handover. Use explicit observations rather than guessed causes. This adds a small server-access and recovery learning project.

## Run locally

Python 3.10+, standard library only. From this folder run:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check.py templates/sample.json outputs/result.json
```

On Windows use `py -3` if needed. No account, credential, network request or install is needed for the offline checker. Rules preserve unknowns and never approve changes. AI is unnecessary for this baseline.

Read [the full lab](LAB.md), [evaluation](EVALUATION.md), [architecture](docs/architecture.md), [demo](DEMO%20SCRIPT.md), [contribution scope](CONTRIBUTIONS.md) and [change record](CHANGELOG.md). Licence: repository MIT terms; no third-party code copied. Microsoft/Cisco/BCN links are documentation and context, not endorsements.
