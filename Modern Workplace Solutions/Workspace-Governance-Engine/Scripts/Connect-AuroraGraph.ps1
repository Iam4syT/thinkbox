<#
.SYNOPSIS
    Handles secure certificate-based authentication to Microsoft Graph.
.DESCRIPTION
    Leverages the local certificate store or an environment certificate variable 
    to securely authenticate without exposed passwords or secrets.
#>
param (
    [Parameter(Mandatory=$true)]
    [string]$TenantId,
    [Parameter(Mandatory=$true)]
    [string]$ClientId,
    [Parameter(Mandatory=$true)]
    [string]$CertificateThumbprint
)

# Import Microsoft Graph Authentication module safely
Import-Module Microsoft.Graph.Authentication -ErrorAction Stop

try {
    Write-Host "Attempting secure certificate-based authentication to Microsoft Graph..." -ForegroundColor Cyan
    
    # Establish connection using the client certificate
    Connect-MgGraph -TenantId $TenantId -ClientId $ClientId -CertificateThumbprint $CertificateThumbprint -NoWelcome
    
    Write-Host "Successfully connected to Microsoft Graph." -ForegroundColor Green
}
catch {
    Write-Error "Authentication failure: $_"
    exit 1
}
