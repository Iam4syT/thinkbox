# Workplace OS Lab

## Current status

Phase: Foundation — Lab 0, in progress.

Published baseline revision:
6dec95e3e7d13394c4af19120d04001232d19b4f

The repository contains a documentation scaffold.
The capabilities and acceptance criteria below are planned.

## Objective

Build a demonstrable workplace control plane that manages and
verifies employee workplace readiness using Microsoft 365 as its
first provider.

The intended users are employees, managers, workplace administrators
and security/compliance reviewers.

## Version 1 scope

- One non-production lab organisation using Microsoft 365.
- Identity and access foundations, with a controlled pilot.
- Joiner, mover and leaver workflows.
- Collaboration access and onboarding tasks.
- Device compliance and workplace readiness.
- Defender and Purview evidence where licensing permits.
- Desired-state comparison and drift detection.
- A React interface and FastAPI control plane.
- Provider-neutral business logic with a Microsoft adapter.
- AI status explanations and approval-controlled action proposals.
- Audit records, automated tests, documentation and a hosted
  development deployment.

Unavailable licensed capabilities must be recorded as limitations
or extension work. Simulated results must be labelled clearly.

## Outside Version 1

- Production deployment or production user administration.
- Commercial billing and production multi-tenant SaaS operations.
- Complete integrations with additional cloud providers.
- Unrestricted AI administration.
- Automatic destructive remediation without explicit approval.

## Acceptance criteria — not yet verified

- [ ] Documented setup produces a working local health endpoint.
- [ ] A joiner request creates a traceable workflow and expected
      identity, access and onboarding task state.
- [ ] Repeating a joiner request does not create duplicate resources.
- [ ] At least one dynamic group is verified using lab identities.
- [ ] Collaboration access and task provisioning are demonstrated.
- [ ] Device compliance is demonstrated or documented as an
      extension because of lab constraints.
- [ ] At least three desired-state deviations are detected and
      explained.
- [ ] A mover workflow identifies both new and obsolete access.
- [ ] An approved leaver workflow blocks lab-user access and
      produces an audit report.
- [ ] AI explanations use authorised project data, and high-risk
      actions cannot execute without approval.
- [ ] Automated tests cover validation, access control, duplicate
      requests and provider failures.
- [ ] Defender and Purview evidence is demonstrated where licensed;
      unavailable capabilities are documented honestly.
- [ ] CI passes and a hosted development deployment is observable.
- [ ] Architecture, permissions, threat model, operating guidance
      and sanitised demonstration evidence are complete.

## Working rules

- Use dedicated lab identities, devices and synthetic test data.
- Keep credentials, tenant-specific configuration and private
  evidence outside the public repository.
- Use sanitised evidence for public documentation.
- Check licensing and costs before provisioning resources.
- Default automated tests and CI use fixtures or fake providers.
- Live tenant checks require explicit scope and authorisation.
- Add tests, security controls and audit behaviour alongside
  implementation.
- Record actual results in EVALUATION.md and changes in CHANGELOG.md.
- Keep acceptance criteria unchecked until supporting evidence
  has been reviewed.
