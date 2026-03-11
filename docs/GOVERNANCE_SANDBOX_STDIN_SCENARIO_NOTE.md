# Governance sandbox stdin scenario note

Use `--scenario-file -` when one scenario bundle should be piped into the CLI from another script or browser-proof workflow.

Recommended proof command:

```bash
cat examples/scenario-report-bundle.yaml | \
  PYTHONPATH=src python3 -m governance_sandbox.cli run \
    --scenario-file - \
    --report-dir artifacts/stdin-proof
```

Why this matters:

- keeps scenario-file support replayable without temporary files,
- helps browser and automation flows hand off JSON/YAML payloads directly,
- preserves the same JSON + markdown + HTML report bundle contract.
