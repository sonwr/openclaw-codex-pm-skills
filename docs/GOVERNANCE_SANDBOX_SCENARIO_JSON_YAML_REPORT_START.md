# governance-sandbox scenario JSON/YAML report start

Use one imported JSON or YAML scenario file plus one generated JSON/Markdown/HTML report bundle as the smallest proof slice.

Quick replay:

```bash
PYTHONPATH=src python3 -m governance_sandbox.cli run \
  --scenario-file examples/scenario-report-bundle.yaml \
  --report-dir artifacts/replay
```

Keep the scenario-file source, shared basename, and generated artifact trio visible in the same handoff.
