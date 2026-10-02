# AFRIST Modern Workplace OS Demonstration

## Current demonstration

Walk through the documented engineering foundation: product scope,
architecture proposal, recorded contributions and evaluation evidence.
Application capabilities and live integrations remain planned.

## Preparation

Open a terminal at the Thinkbox repository root and run:

```bash
cd "Modern Workplace Solutions/Workplace OS"
```

## Walkthrough

1. Display the scope and architecture documentation checkpoint:

```bash
git show --stat --oneline be95575
```

Explain which documentation files this commit contains.

2. Display the implementation scope:

```bash
cat LAB.md
```

Explain the objective, Version 1 boundaries and unchecked acceptance criteria.

3. Display the proposed architecture:

```bash
cat docs/adr/ADR-001-control-plane-and-adapters.md
```

Explain the control plane, Microsoft adapter and fake provider.
Identify the Proposed decision and Planned implementation status.

4. Display the evidence record:

```bash
cat EVALUATION.md
```

Distinguish dated findings from outstanding work.

5. Display the contribution record:

```bash
cat CONTRIBUTIONS.md
```

Explain the recorded engineering work and its supporting checkpoints.

## Walkthrough acceptance

The viewer can identify the product objective, planned boundaries,
proposed architecture, available evidence and remaining work.

## Future demonstration

Add verified joiner, mover, leaver, drift, approval and recovery
walkthroughs as those capabilities become available.

Use dedicated non-production identities and sanitised evidence.
Keep credentials and private tenant information out of the demonstration.
