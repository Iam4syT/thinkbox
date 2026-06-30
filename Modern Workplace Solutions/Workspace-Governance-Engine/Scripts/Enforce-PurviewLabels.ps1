<#
.SYNOPSIS
    Programmatically audits Microsoft 365 Groups and enforces Microsoft Purview sensitivity labels.
#>
param (
    [Parameter(Mandatory=$true)]
    [string]$ConfigFilepath
)

$Config = Get-Content -Raw $ConfigFilepath | ConvertFrom-Json
$TargetLabelId = $Config.TenantSettings.ClassificationLabels.HighCompliance

Import-Module Microsoft.Graph.Groups -ErrorAction Stop

try {
    Write-Host "Analyzing Group classification spaces..." -ForegroundColor Cyan
    $Groups = Get-MgGroup -All -Property "id,displayName,assignedLabels"

    foreach ($Group in $Groups) {
        $HasLabel = $false
        foreach ($Label in $Group.AssignedLabels) {
            if ($Label.LabelId -eq $TargetLabelId) { $HasLabel = $true }
        }

        if (-not $HasLabel) {
            Write-Host "Compliance Gap Found: Unified Group '$($Group.DisplayName)' lacks strict classification tags. Remediation in progress..." -ForegroundColor Yellow
            
            # Construct Microsoft Graph update payload
            $UpdateParams = @{
                AssignedLabels = @(
                    @{
                        LabelId = $TargetLabelId
                    }
                )
            }
            
            # Apply compliance label programmatically
            Update-MgGroup -GroupId $Group.Id -BodyParameter $UpdateParams
            Write-Host "Successfully applied Purview Label to '$($Group.DisplayName)'." -ForegroundColor Green
        }
    }
}
catch {
    Write-Error "Failed to fully enforce regulatory labels: $_"
}
