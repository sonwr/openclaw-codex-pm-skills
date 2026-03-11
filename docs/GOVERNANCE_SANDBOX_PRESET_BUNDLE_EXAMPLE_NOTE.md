# Governance Sandbox preset bundle example note

Use `examples/scenario-preset-bundle.yaml` in the governance-sandbox repo when you need one replayable fixture that proves two things together:

1. stakeholder presets can be loaded from a scenario file, and
2. the same run can emit a JSON/Markdown/HTML report bundle.

Copy-paste replay command:

```bash
python3 -m governance_sandbox.cli run \
  --scenario-file examples/scenario-preset-bundle.yaml \
  --report-dir artifacts/preset-bundle
```

Reviewers should confirm that the JSON payload keeps `preset` values on each stakeholder response and that the report directory contains `delegate-confidence-rehearsal.json`, `.md`, and `.html`.
