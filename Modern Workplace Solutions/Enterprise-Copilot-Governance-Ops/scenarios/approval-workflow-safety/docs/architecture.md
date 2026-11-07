# Architecture and boundaries

Caller-supplied requester/reviewer → pending → reviewer decision → injected response handling → local terminal state/audit. State is in memory, identity is simulated and no API is called. Real integration needs durable state, authenticated identities and concurrency protection.
