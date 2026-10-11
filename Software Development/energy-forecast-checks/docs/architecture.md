Operator -> validated local CSV -> first eight rows for training -> next four rows for testing -> previous-observation baseline and fitted straight-line forecast -> local metrics.json -> human review. The baseline uses the last observed value available before each forecast. The fitted model uses training rows only. No identity provider or service account is needed.

Eight tests pass; original output has 8/4 chronological split and MAE 5/0; negative and non-finite values are rejected; the 900 kW change affects error, not fitted parameters; no live services or personal data are used.

Replace the straight-line fixture with permitted representative data, add a held-out seasonal period and compare a justified ML model against persistence. Specify deployment monitoring and a human review threshold before considering any cloud service. Paid services and live systems are outside this lab.
