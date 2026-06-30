# SOP: Microsoft 365 Workspace Governance Engine Execution & Drift Remediation

## 1. Purpose & Objective
This Standard Operating Procedure (SOP) defines the operational, automated framework for monitoring workspace compliance drift, managing lifecycle optimizations, and enforcing data classification controls across our enterprise tenant.

## 2. Scope
Applies universally across all provisioned Microsoft 365 Groups, Microsoft Teams workspaces, and corporate SharePoint Online environments.

## 3. Roles and Responsibilities
* **Cloud Infrastructure Engineering Team**: Accountable for updating core scripts, provisioning configurations, and maintaining GitHub Actions pipeline status.
* **Information Security & Governance Team**: Responsible for defining data classification targets and auditing alert reports.

## 4. Step-by-Step Production Execution
### Manual Execution Path
If unexpected system drift or alert events occur outside scheduled midnight runs:
1. Log into the enterprise GitHub Control Panel.
2. Navigate to **Actions** > Select **M365 Tenant Compliance & Optimization Scan**.
3. Select **Run workflow** dropdown menu and confirm by clicking the button.

### Certificate Rotation Routine (Annual Requirement)
1. Run `New-SelfSignedCertificate` via administrative PowerShell to produce a updated `.cer`/`.pfx` block.
2. Upload the updated public key to the Entra ID Enterprise App Registration dashboard.
3. Update `${{ secrets.AZURE_CERT_THUMBPRINT }}` environment flags inside the GitHub Repository secret variables workspace.

## 5. Troubleshooting & Error Mitigation Paths
* **Error Code: `Authentication Failed / Token Expired`**
    * *Root Cause*: Expired Client Certificate configuration or wrong Thumbprint match.
    * *Remediation*: Verify local/runner thumbprints match the thumbprint registered in Azure Entra ID.
* **Error Code: `Insufficient Privileges / 403 Forbidden`**
    * *Root Cause*: Administrator consent was missing for added Microsoft Graph API permissions.
    * *Remediation*: Navigate to Azure Portal > Entra ID > App Registrations > API Permissions, and re-apply **Grant Admin Consent**.

## 6. Emergency Rollback Procedures
If an automation update causes widespread unintended modifications:
1. Navigate to the GitHub main repository code tree.
2. Revert the last merge request or commit via Git:
   ```bash
   git revert HEAD
   git push origin main
   ```
3. If immediate lockdown is needed, temporarily remove the Entra ID application registration's API permissions to pause all system writes.
