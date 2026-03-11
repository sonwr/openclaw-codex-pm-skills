# Governance Sandbox preset JSON result-card note

When the workstream needs the smallest preset-catalog handoff before a browser form or report card update, use:

```bash
PYTHONPATH=src python3 -m governance_sandbox.cli run --list-presets-json
```

Treat the exported preset JSON as a result-card contract:

- keep the preset key stable,
- keep the human label visible,
- keep the short summary beside the preset,
- and reuse the same payload for CLI, report, and first web-demo form reviews.

This keeps preset-aware scenario input aligned with the same proof surface used by markdown/html report cards.
