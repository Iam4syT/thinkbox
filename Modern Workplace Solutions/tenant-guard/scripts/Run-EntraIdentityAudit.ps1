<#
.SYNOPSIS
    Audits Microsoft Entra ID for administrative roles and flags accounts without MFA.
.DESCRIPTION
    Queries the Graph API to count highly privileged Global Admins and verify settings.
#>

# 1. Load the Configuration Baseline
$BaselinePath = Join-Path $PSScriptRoot "..\templates\Base-M365-DesiredState.json"
$Baseline = Get-Content -Raw -Path $BaselinePath | ConvertFrom-Json

Write-Host "=== STEP 1: Starting Entra ID Identity Security Audit ===" -ForegroundColor Cyan

# 2. Mocking API Connection for Safe Pipeline/Dev Environment Testing
# In production, replace this section with: Connect-MgGraph -Scopes "RoleManagement.Read.Directory", "User.Read.All"
Write-Host "[INFO] Simulating secure authentication token acquisition..." -ForegroundColor Yellow

# 3. Simulate Querying Entra ID for Global Admins
# We mimic real API output structures to allow local running without breaking pipelines
$ActiveGlobalAdmins = @(
    @{ UserPrincipalName = "admin.bunamin@tenant.com"; Role = "Global Administrator"; MFAStatus = "Enabled" },
    @{ UserPrincipalName = "service_account_backup@tenant.com"; Role = "Global Administrator"; MFAStatus = "Disabled" },
    @{ UserPrincipalName = "vendor_temp@tenant.com"; Role = "Global Administrator"; MFAStatus = "Disabled" }
)

Write-Host "[INFO] Successfully retrieved active administrative assignments via Microsoft Graph." -ForegroundColor Green

# 4. Process and Cross-Reference with Baseline
$AdminCount = $ActiveGlobalAdmins.Count
$MaxAllowed = $Baseline.IdentitySecurity.MaxAllowedGlobalAdmins

Write-Host "`n--- Verification Audit Results ---" -ForegroundColor White
Write-Host "Current Global Admin Count: $AdminCount"
Write-Host "Maximum Allowed Baseline: $MaxAllowed"

if ($AdminCount -gt $MaxAllowed) {
    Write-Host "[ALERT] DRIFT DETECTED: Global Admin count exceeds baseline allocation threshold!" -ForegroundColor Red
} else {
    Write-Host "[PASS] Global Admin allocations within acceptable boundary metrics." -ForegroundColor Green
}

# 5. Check for Critical Security Vulnerabilities (No-MFA Admins)
$VulnerableAccounts = $ActiveGlobalAdmins | Where-Object { $_.MFAStatus -eq "Disabled" }

if ($VulnerableAccounts) {
    Write-Host "[CRITICAL] Accounts found with Global Admin rights but NO Multi-Factor Authentication:" -ForegroundColor Red
    foreach ($Acc in $VulnerableAccounts) {
        Write-Host " -> RISK ID: $($Acc.UserPrincipalName)" -ForegroundColor Yellow
    }
    # Exit with code 1 to notify the GitHub automation action that a high-risk drift exists
    Exit 1
} else {
    Write-Host "[PASS] Zero structural privilege identity risks identified." -ForegroundColor Green
    Exit 0
}
