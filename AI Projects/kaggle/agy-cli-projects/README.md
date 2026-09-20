# CLI experiments and release-note learning

Start with the offline parser example in bq-releases-notes: install its requirements.txt and run `python demo.py`. That is the supported first-run check. The Flask viewer can be run with `python app.py`; its live release endpoint reads the official Google feed.

The retained automate_pipeline.py and upload_to_drive.py are separate integration experiments requiring external CLI/API configuration and applicable publishing authorisation. They were not run in this repair. No automatic Drive upload or recurring schedule is enabled by the portfolio lab. Inspect their source and dependencies before use.

Reference/course material and release-note text retain original rights and attribution; the code licence does not relicense third-party publications.
