# Governance runbook

The supported local lab uses fixture files and never connects to a tenant. Run the tests and inspect the plan before considering live operation.

For a separately authorised live read, install the Graph modules and authenticate for the required scope. Certificate authentication in Connect-AuroraGraph.ps1 is suitable only for supported application-permission reads; a hosted runner would need the actual installed certificate, not just its thumbprint. Root CI contains no certificate or tenant jobs.

Sensitivity-label updates require delegated Graph access and a supported administrator role, not application-only credentials. See [Microsoft group update documentation](https://learn.microsoft.com/en-us/graph/api/group-update?view=graph-rest-1.0), checked 13 September 2026. Confirm exact permissions, licensing and label policy in your test tenant.

Use Enforce-PurviewLabels.ps1 with -Live and explicit -GroupIds to plan. Review output. -Apply is required for writes and supports -WhatIf/confirmation. Existing labels are retained unless -ReplaceExisting is explicitly requested. A pre-change backup is written before each mutation and the script refuses a detected concurrent label change. Live behaviour has not been tenant-tested here.

Restore-PurviewLabels.ps1 reads one backup, checks tenant identity and expected current labels, and plans a restore. -Apply is required to perform it. Inspect current state when verification is delayed or a write fails; preserve backups. Keep all live artifacts private. No recurring tenant mutation schedule is included.

SharePoint lastModifiedDateTime is an inactivity clue, not a last-access measurement or compliance verdict. Review candidates with owners and usage evidence before archiving anything.
