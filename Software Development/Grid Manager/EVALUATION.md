# Evaluation scope

Java 24+ and Maven 3.9+ required. run.sh uses Maven from the project directory; ./run.sh gui is optional. Tests target the current CostCalculationService, not removed SwitchReport methods.

Commands and outcomes are recorded in the root docs/verification.json after the verification pass.

Scope limit: Inputs and source switching are software scenarios. No physical grid or live sensor integration. Cost/carbon coefficients and demand-to-energy conversion are assumptions, not validated savings.

See [repository verification](../../docs/VERIFICATION.md) for actual command results, environment and date. An installed dependency or successful syntax check alone is not an end-to-end test. Live services not exercised remain unverified.
