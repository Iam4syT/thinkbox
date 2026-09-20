# Draft assessment architecture

HTTP draft → static sample policies in trusted system context → untrusted draft as data → optional provider → strict JSON consistency validation → model suggestion requiring human review.

No vector store or indexed retrieval is implemented. Missing credentials, provider failures and malformed output never issue approval. Local contract tests inject synthetic provider responses; they do not measure live model quality. The labelled examples in evaluation-cases.json support a future authorised model evaluation with false-approval/rejection and abstention metrics.

Temperature zero is not a guarantee of deterministic or correct output. The application is a lab, not a regulatory certification system or a complete security boundary. Production authentication, privacy controls, policy ownership and live evaluation remain separate requirements.
