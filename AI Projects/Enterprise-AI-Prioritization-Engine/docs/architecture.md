# Architecture

Streamlit inputs → validated core scoring → quadrant and illustrative coefficient arithmetic → visible assumptions and comparison.

The core rejects non-finite/out-of-range scores and invalid token counts. The 60/40 weights, 65 threshold and resource coefficients are teaching choices. See assumptions.md for units/provenance and tests/test_inputs.py for boundary checks. The Dockerfile is packaging source, not evidence of a cloud deployment. No production or sustainability outcome is asserted.
