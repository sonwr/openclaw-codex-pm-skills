# governance-sandbox preset JSON handoff

Use `gov-sandbox run --list-presets-json` when a scenario builder, browser form, or automation script needs a stable catalog of stakeholder preset labels plus their summary copy.

Quick review loop:

1. Run `PYTHONPATH=src python3 -m governance_sandbox.cli run --list-presets-json`
2. Confirm each preset exposes `label`, `summary`, `stance`, `concern`, and `mitigation`
3. Feed that payload into the scenario-form or web-demo layer instead of duplicating preset copy

Why it helps:

- keeps CLI and UI preset wording aligned
- gives form builders a machine-readable trait inventory
- reduces hard-coded preset descriptions in demo code or docs
