# Architecture

A local CLI receives a question and a fixture role; eligible synthetic documents are filtered before keyword scoring; it emits a document citation or null. The role argument is simulated. A real service must derive roles from verified identity and enforce permissions server-side. No network or LLM is used.

Local input → validation/access boundary → numerical or retrieval component → measured output → human review. Public synthetic fixtures only. See LAB.md for operational limits and recovery.
