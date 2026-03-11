# Governance Sandbox scenario JSON quickstart

Use this when you want the shortest JSON-native replay for proposal input plus report artifacts.

## Command

```bash
PYTHONPATH=src python3 -m governance_sandbox.cli run \
  --scenario-file examples/scenario-report-bundle.json \
  --report-dir artifacts/json-demo
```

## What to verify

- the CLI accepts the JSON scenario file without converting it to YAML first
- `artifacts/json-demo/report.json` exists
- the matching markdown and HTML report files exist beside it
- the stdout payload keeps `report.scenario_file` and artifact paths visible
