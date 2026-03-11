# Governance Sandbox scenario -> report stack note

Use this note when one governance-sandbox change should still prove the same narrow flow:

1. one scenario file import,
2. one simulated stakeholder run,
3. one JSON/Markdown/HTML report bundle.

## Why this exists

Small governance-sandbox changes are easier to trust when scenario input and report output stay coupled.

## Minimal replay

```bash
PYTHONPATH=src python3 -m governance_sandbox.cli run \
  --scenario-file examples/scenario-report-bundle.yaml \
  --report-dir artifacts/replay
```

## Review cues

- confirm the scenario file is explicit and reusable
- confirm the generated report bundle includes JSON, markdown, and HTML
- confirm the README or handoff language points to the same replay path

## Stop condition

Do not widen scope until the same scenario-file -> report-bundle path still replays cleanly after the edit.
