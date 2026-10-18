# Architecture

Twelve synthetic dated rows enter validation; eight train a one-feature least-squares model, four remain held out. A frozen last-observation baseline is compared with model RMSE, the typical prediction error size. A decision is pass only when error beats baseline and is at most 2 target units. This prints a decision; it never deploys anything.

Local input → validation/access boundary → numerical or retrieval component → measured output → human review. Public synthetic fixtures only. See LAB.md for operational limits and recovery.
