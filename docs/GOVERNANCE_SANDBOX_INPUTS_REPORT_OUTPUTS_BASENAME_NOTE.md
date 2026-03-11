# Governance Sandbox inputs.report.outputs basename note

Use this note when a governance-sandbox scenario fixture keeps report bundle naming under `inputs.report.outputs` instead of the top-level `report` block.

## What to keep true

- One imported scenario file should still drive the default JSON/Markdown/HTML bundle basename.
- `inputs.report.outputs.basename` should behave like `report.outputs.basename`.
- The same basename should remain visible in generated report metadata so PM handoff copy stays stable.

## Quick replay

```bash
PYTHONPATH=src python3 -m governance_sandbox.cli run \
  --scenario-file examples/scenario-report-bundle.yaml \
  --report-dir artifacts/review
```

If the scenario fixture carries `inputs.report.outputs.basename`, expect the generated bundle to use that basename across `.json`, `.md`, and `.html` files.
