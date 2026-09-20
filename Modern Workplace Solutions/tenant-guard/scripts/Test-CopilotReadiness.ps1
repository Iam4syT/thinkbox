<#
.SYNOPSIS
    Evaluates SharePoint and Purview environments for AI semantic indexing safety.
#>

$BaselinePath = Join-Path $PSScriptRoot "..\templates\Base-M365-DesiredState.json"
$Baseline = Get-Content -Raw -Path $BaselinePath | ConvertFrom-Json

Write-Host "=== STEP 3: Executing AI & Copilot Data Governance Safety Scan ===" -ForegroundColor Cyan

# Mock data simulating a discovery of an over-shared site
$SharePointSites = @(
    @{ SiteName = "Finance-Internal"; AnonymousSharing = $false; PublicAccess = "Restricted" },
    @{ SiteName = "Executive-Board-Drafts"; AnonymousSharing = $true; PublicAccess = "OpenToAllEmployees" }
)

$VulnerabilitiesFound = 0

foreach ($Site in $SharePointSites) {
    if ($Site.AnonymousSharing -eq $true -or $Site.PublicAccess -eq "OpenToAllEmployees") {
        Write-Host "[RISK] Over-Shared Directory Exposed to Copilot Index: $($Site.SiteName)" -ForegroundColor Red
        Write-Host "       -> Fixture indicates broad access; real membership and retrieval behaviour are untested." -ForegroundColor Yellow
        $VulnerabilitiesFound++
    }
}

if ($VulnerabilitiesFound -gt 0) {
    Write-Host "[ALERT] Audit failed. Synthetic fixture contains the expected broad-access finding." -ForegroundColor Red
    Exit 1
} else {
    Write-Host "[PASS] No finding in the checked fixture; this is not a deployment clearance." -ForegroundColor Green
    Exit 0
}
