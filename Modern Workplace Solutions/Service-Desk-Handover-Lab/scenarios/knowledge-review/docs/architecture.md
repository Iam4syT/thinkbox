# Architecture and operational boundary

Author → synthetic article metadata → local validation → ready/hold report → reviewer. Ready means metadata checks passed, not that repair steps are safe or technically correct.
Local user runs code under ordinary filesystem permissions. Input is permitted synthetic JSON only. No tenant identity, secret, network call or write to a business service. Reject malformed records; review reports before acting. Four-hour rule is a lab parameter, not an employer SLA. Technical documentation checked 29 October 2026: https://docs.python.org/3.12/library/json.html and https://docs.python.org/3.12/library/unittest.html .
