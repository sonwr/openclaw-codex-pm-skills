# governance-sandbox scenario report start note

Use this note when PM-facing guidance only needs the smallest honest replay for governance-sandbox scenario-file input plus generated JSON/Markdown/HTML reports.

## Starter command

```bash
PYTHONPATH=src python3 -m governance_sandbox.cli run \
  --scenario-file examples/scenario-report-bundle.yaml \
  --report-dir artifacts/review
```

Keep the handoff scoped to one imported scenario file and one generated report bundle before widening into broader UI or Playwright proof.
