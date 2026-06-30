<#
.SYNOPSIS
    Audits and uncovers unused or stagnant SharePoint Online sites to limit data sprawl and save license costs.
#>
param (
    [Parameter(Mandatory=$true)]
    [string]$ConfigFilepath
)

# Load Operational Configuration thresholds
if (-not (Test-Path $ConfigFilepath)) { throw "Configuration file not found!" }
$Config = Get-Content -Raw $ConfigFilepath | ConvertFrom-Json

$InactivityDays = $Config.TenantSettings.InactivityThresholdDays
$TargetDate = (Get-Date).AddDays(-$InactivityDays)



Import-Module Microsoft.Graph.Sites -ErrorAction Stop

try {
    Write-Host "Fetching all active SharePoint sites..." -ForegroundColor Cyan
    # Retrieve all sites within the M365 tenant
    $AllSites = Get-MgSite -All -Property "id,webUrl,displayName,lastModifiedDateTime"
    
    $StaleSites = @()

    foreach ($Site in $AllSites) {
        # Check if site activity has lapsed past our defined threshold
        if ($null -ne $Site.LastModifiedDateTime -and $Site.LastModifiedDateTime -lt $TargetDate) {
            $StaleSites += [PSCustomObject]@{
                SiteID           = $Site.Id
                SiteName         = $Site.DisplayName
                URL              = $Site.WebUrl
                LastActivityDate = $Site.LastModifiedDateTime
            }
        }
    }

    # Output details or execute actions
    if ($StaleSites.Count -gt 0) {
        Write-Host "Found $($StaleSites.Count) stale sites violating compliance policy:" -ForegroundColor Yellow
        $StaleSites | Format-Table -AutoSize
        
        # In production, this data payload can be written directly to a Blob or piped to Power BI
        $StaleSites | ConvertTo-Json | Out-File "$(Build.ArtifactStagingDirectory)/stale-sites-report.json" -Force
    } else {
        Write-Host "Tenant scan complete. Zero compliance violations discovered." -ForegroundColor Green
    }
}
catch {
    Write-Error "Error executed during site governance run: $_"
}
