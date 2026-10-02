# ADR-001: Control plane and provider adapters

Status: Proposed
Date: 2026-09-26
Implementation status: Planned

## Context

Workplace OS will use Microsoft 365 first, while keeping its
workplace rules independent of Microsoft-specific APIs.

The project must support automated tests without changing a
live tenant.

## Proposed decision

Use a provider-neutral control plane with provider adapters.

- The React interface calls the FastAPI application.
- Domain code describes people, roles and desired workplace state.
- Services coordinate workflows, approvals and audit records.
- Provider interfaces describe the external operations needed.
- The Microsoft adapter handles Microsoft-specific API calls
  and translates their results into application models.
- A fake provider supports automated tests without live changes.

Keep these as modules within the initial application.
Separate deployed services are not required for this prototype.

## Alternatives considered

1. Microsoft API calls throughout the application:
   simpler initially, but couples workplace rules to Microsoft.

2. A Microsoft-specific low-code solution:
   useful for platform-focused automation, but changes the intended
   portable application architecture and learning scope.

## Consequences

- Workplace rules can be tested independently of Microsoft.
- Microsoft API changes can be handled within the adapter.
- Interfaces and result mappings require additional design work.
- Provider differences must be represented honestly.
- Portability remains a design intention until another provider
  has been implemented and tested.

## Security and verification

- Approval and authorisation rules belong in server-side logic.
- Secrets must not enter source control or frontend code.
- Default automated tests use the fake provider.
- Later tests must prove that high-risk actions cannot bypass
  approval and that provider failures are handled correctly.

This record does not claim that any component is implemented.
