# aurora-tenant-guard

Automated Identity Governance, Endpoint Compliance Monitoring, and AI Integration Framework for Modern Enterprises via Microsoft Graph and PowerShell CI/CD.

## Business Value & Core Concept
Manual administration across international cloud environments exposes businesses to compliance drifts, unmapped administrative access, and data over-sharing. **aurora-tenant-guard** implements **Infrastructure as Code (IaC)** principles across Microsoft 365 architecture. 

By tracking architectural standards inside a structured version-controlled repository, any changes to live configurations are caught, flagged, and audited systematically.

## High-Level Architecture Flow
1. **Define Baseline:** Core configurations reside safely inside `Base-M365-DesiredState.json`.
2. **Audit Scripts Execution:** Modern PowerShell connects securely via Graph API endpoints to review configurations.
3. **Continuous Enforcement:** GitHub Actions automatically runs checks every hour to prevent configuration shifts.

## Quick Installation & Local Verification

To run this laboratory simulation framework manually on your local system for testing, execute these commands inside your terminal:

```powershell
# 1. Clone your repository workspace
git clone https://github.com/YOUR_GITHUB_USERNAME/aurora-tenant-guard.git
cd aurora-tenant-guard

# 2. Execute Identity Access Review Script
./scripts/Run-EntraIdentityAudit.ps1

# 3. Execute Intune Fleet Matching Script
./scripts/Sync-IntuneDevicePolicies.ps1

# 4. Run AI Environment Validation Audit
./scripts/Test-CopilotReadiness.ps1
```
