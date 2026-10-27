# Architecture

Synthetic JSON → local schema and rule checks → JSON review prompts → human review. No network, access grant, tenant update or closure. Dummy authority flags do not authenticate access; future integration needs real authorisation, tenant isolation, secure retention and audit. Python standard library, no extra package install.
