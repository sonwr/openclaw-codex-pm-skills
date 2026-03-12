# Governance Sandbox Scenario Report Minimum Progress Check

Use this check when a planning pass needs to prove the smallest acceptable governance-sandbox improvement without overscoping the branch.

## Minimum acceptable slice

1. Import one governance scenario from a JSON or YAML file.
2. Produce at least one validated report artifact from that scenario-driven run.
3. Keep the proof path small enough that the next pass can still add presets, demo UI, or media capture without reworking the CLI contract.

## Review prompt

- Did the change improve scenario-file intake, report generation, or replayable evidence?
- Can a reviewer rerun the smallest happy path with one command?
- Did the repo keep report artifacts explicit enough for downstream handoff?

## Suggested proof bundle

- scenario fixture path
- exact CLI command
- produced JSON/Markdown/HTML artifact path
- validator or smoke-test command
