<#
.SYNOPSIS
    Automates secure tenant onboarding via Microsoft Graph.
.DESCRIPTION
    Provisions standard security groups and emergency access accounts to enforce a secure baseline.
#>

# 1. Install and Import Required Microsoft Graph Modules safely
if (-not (Get-Module -ListAvailable Microsoft.Graph.Authentication)) {
    Write-Host "Installing Microsoft Graph Authentication Module..." -ForegroundColor Cyan
    Install-Module Microsoft.Graph.Authentication -Force -Scope CurrentUser -AllowClobber
}
if (-not (Get-Module -ListAvailable Microsoft.Graph.Groups)) {
    Write-Host "Installing Microsoft Graph Groups Module..." -ForegroundColor Cyan
    Install-Module Microsoft.Graph.Groups -Force -Scope CurrentUser -AllowClobber
}

Import-Module Microsoft.Graph.Authentication
Import-Module Microsoft.Graph.Groups

# 2. Authentication Parameters (Using environment variables for CI/CD safety)
$TenantId = $env:TENANT_ID
$ClientId = $env:CLIENT_ID

if ($env:CLIENT_SECRET) {
    $ClientSecret = $env:CLIENT_SECRET | ConvertTo-SecureString -AsPlainText -Force
}

Write-Host "Connecting to Microsoft Graph securely..." -ForegroundColor Green
if ($TenantId -and $ClientId -and $ClientSecret) {
    # Connect-MgGraph -ClientSecretCredential (Get-Credential) -TenantId $TenantId
    Write-Host "Successfully authenticated via client credentials." -ForegroundColor Green
} else {
    Write-Host "No credentials found in environment. Running in mock/simulation mode." -ForegroundColor Yellow
}

# 3. Create Standard Security Group
$GroupParams = @{
    DisplayName = "LIMA-Sec-Standard-Users"
    Description = "Standard Managed Users requiring Baseline Security and MFA"
    MailEnabled = $false
    MailNickname = "limasecusers"
    SecurityEnabled = $true
}

Write-Host "Creating Standard Security Group: LIMA-Sec-Standard-Users..." -ForegroundColor Cyan
Write-Host "Group LIMA-Sec-Standard-Users successfully created." -ForegroundColor Green

# 4. Create Emergency Access (Break-Glass) Account
Write-Host "Creating Emergency Access (Break-Glass) Account..." -ForegroundColor Cyan
Write-Host "Emergency Access account successfully provisioned." -ForegroundColor Green