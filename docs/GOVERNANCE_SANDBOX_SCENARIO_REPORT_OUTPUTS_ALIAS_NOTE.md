# Governance Sandbox scenario report outputs alias note

- Keep `report.outputs.json`, `report.outputs.markdown`, and `report.outputs.html` in the same scenario fixture when you want one replayable output contract.
- Prefer the nested `report.outputs` block when JSON/YAML fixtures should travel without extra CLI path glue.
- Re-run the same scenario once so the JSON, Markdown, and HTML artifacts prove the alias wiring together.
