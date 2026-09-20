# Architecture

Fixture JSON → scoped PowerShell checks → proposed changes / inactivity candidates → local artifacts.

Live mode is optional and separately authorised. Group label changes use delegated Graph context, selected Microsoft 365 group IDs, existing-label preservation, pre-change backup, change detection and post-write verification. Rollback checks the recorded tenant and current labels before restoring. No root workflow performs a live operation.

Connect-AuroraGraph.ps1 retains certificate authentication for supported read scenarios; it is not the authentication path for sensitivity-label updates. See SOP-Tenant-Governance.md for the documented boundary and current Microsoft source.
