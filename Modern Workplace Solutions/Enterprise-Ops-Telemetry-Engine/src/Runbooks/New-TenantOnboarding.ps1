<# Synthetic plan only: no module installation, authentication or tenant writes. #>
[CmdletBinding()]
param([string]$Organisation = 'Synthetic lab')
[pscustomobject]@{
    Mode='simulation'; Organisation=$Organisation; Authenticated=$false; PerformedActions=@();
    ProposedActions=@('Review security group scope', 'Plan emergency-access accounts', 'Document verification and rollback')
} | ConvertTo-Json -Depth 5
