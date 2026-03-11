# GOVERNANCE_SANDBOX_STDIN_REPORT_BUNDLE_NOTE

Use stdin when a scenario payload already exists in another tool or browser form.

## Minimal command

```bash
cat examples/scenario-report-bundle.yaml | \
  PYTHONPATH=src python3 -m governance_sandbox.cli run \
    --scenario-file - \
    --report-dir artifacts/stdin-demo
```

## Why this matters
- Keeps scenario-file support replayable in shell pipelines.
- Preserves the same JSON/Markdown/HTML report bundle flow.
- Fits browser-form or automation handoffs without creating a temporary file first.
