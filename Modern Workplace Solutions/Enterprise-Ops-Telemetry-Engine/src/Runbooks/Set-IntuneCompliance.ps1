<# Payload illustration only; no policy has been sent or enforced. #>
[pscustomobject]@{
    Mode='simulation'; PerformedActions=@();
    ProposedPolicy=@{DisplayName='Synthetic Windows baseline'; RequireFirewall=$true; RequireAntivirus=$true};
    Note='Validate the intended Graph payload, licensing, permissions and rollback in an authorised test tenant before implementation.'
} | ConvertTo-Json -Depth 5
