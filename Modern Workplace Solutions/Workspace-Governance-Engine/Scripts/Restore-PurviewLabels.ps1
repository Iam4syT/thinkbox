<# Restore one locally saved change after reviewing its backup and current tenant state. #>
[CmdletBinding(SupportsShouldProcess=$true, ConfirmImpact='High')]
param([Parameter(Mandatory)][string]$BackupPath, [switch]$Apply)
$ErrorActionPreference = 'Stop'
$backup = Get-Content -Raw -LiteralPath $BackupPath | ConvertFrom-Json
Import-Module Microsoft.Graph.Groups -ErrorAction Stop
$context = Get-MgContext
if (-not $context -or $context.AuthType -ne 'Delegated' -or $context.TenantId -ne $backup.TenantId) { throw 'Connect with delegated access to the tenant recorded in the backup.' }
$current = Get-MgGroup -GroupId $backup.GroupId -Property 'id,assignedLabels' -ErrorAction Stop
if ((@($current.AssignedLabels.LabelId | Sort-Object) -join ',') -ne (@($backup.Applied.LabelId | Sort-Object) -join ',')) { throw 'Current labels differ from the recorded change; investigate instead of overwriting.' }
$before = @($backup.Before | ForEach-Object { @{LabelId=[string]$_.LabelId} })
if ($Apply -and $PSCmdlet.ShouldProcess($backup.GroupId, 'Restore previous sensitivity label state')) {
    Update-MgGroup -GroupId $backup.GroupId -BodyParameter @{AssignedLabels=$before} -ErrorAction Stop
    $verified = Get-MgGroup -GroupId $backup.GroupId -Property 'id,assignedLabels' -ErrorAction Stop
    if ((@($verified.AssignedLabels.LabelId | Sort-Object) -join ',') -ne (@($before.LabelId | Sort-Object) -join ',')) { throw 'Restore returned; verification pending. Keep the backup.' }
    'Restore verified'
} else { $backup }
