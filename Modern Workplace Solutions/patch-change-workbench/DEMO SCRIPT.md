# Three-minute demonstration

1. Explain the recurring operator task and synthetic scope. State assistant provenance and unrun tenant boundaries.
2. Open `templates/findings.json`. Point to LAB-VULN-03 escalation, LAB-VULN-04 pending restart and LAB-VULN-06 failed app health.
3. Run `python3 scripts/change_workbench.py --output outputs/result.json`. Open the output and show the human next action. No mutation or message sending occurs.
4. Copy the fixture; remove the security recheck from the otherwise complete finding. Rerun and show that closure is withheld.
5. Run `python3 -m unittest discover -s tests -v`; explain one meaningful failure boundary rather than reciting the count.
6. State the lesson: successful installation is only one part of safe remediation. Explain the next tenant test and its licence/approval dependencies.

No video recorded. A future recording should show actual run output and exclude private identifiers. Do not narrate unrun steps as completed experience.
