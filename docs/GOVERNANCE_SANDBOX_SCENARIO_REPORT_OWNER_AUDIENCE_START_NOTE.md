# Governance Sandbox scenario/report owner+audience start note

Keep the first governance-sandbox proof narrow: one imported scenario file, one generated JSON/Markdown/HTML bundle, and visible report owner plus audience metadata in the same replay.

Suggested check:

```bash
PYTHONPATH=src python3 -m governance_sandbox.cli run \
  --scenario-file examples/scenario-review-pack.yaml \
  --report-dir artifacts/review-pack
```

Pass when the replay keeps these visible together:
- imported scenario file path
- generated report bundle paths
- report owner metadata
- report audience metadata
