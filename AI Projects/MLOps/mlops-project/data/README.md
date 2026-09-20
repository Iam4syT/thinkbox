# Dataset and model provenance

`olist_customers_dataset.csv` is the existing Olist-derived fixture from the attributed upstream customer-satisfaction project. See [upstream README](../UPSTREAM%20README.md) for the dataset/tutorial source. Dataset rights are separate from the repository's code licence; verify the original licence before redistribution or other use. No new external dataset was added in this repair.

The supported `demo.py` groups rows by order_id before splitting, fits preprocessing on training rows and compares Ridge with a mean predictor. Models are rebuilt in memory. The old unprovenanced pickle was removed; no committed model is loaded. Legacy ZenML code is retained for study, with its historical dependencies separately labelled.
