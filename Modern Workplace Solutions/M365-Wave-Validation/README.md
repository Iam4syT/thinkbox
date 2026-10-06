# M365-Wave-Validation
Independent learning tool for Microsoft cloud delivery teams. No client commissioning.
Implemented: offline boolean evidence checks and synthetic fixtures. Tested: local normal/failure cases. Planned/unrun: every cloud/tenant step in LAB.md. A checklist result is not approval or proof of actual resource state.
Quick start from project root: python3 scripts/check.py templates/sample.json
Run tests: python3 -m unittest discover -s scripts -p 'test_*.py' -v
Failure demo: python3 scripts/check.py templates/failure.json (expected exit 1).
See LAB.md, EVALUATION.md, docs/architecture.md and evidence/. Python 3.10+, no dependencies. Manual checklist is the simpler baseline; AI is optional and does not decide release.
Public research basis: https://www.applicable.com/consultancy/ ; technical references linked in lab context. No private application, CV or customer data included.
