# Governance Sandbox report output-name alias note

When a `governance-sandbox` scenario file already carries reviewer-facing report naming, prefer one of these alias patterns instead of repeating file names on the CLI:

- `report.output_name` — best when the scenario already has a `report:` block.
- `report.name` — short bundle basename alias for report-first fixtures.
- top-level `report_name` — lightweight fallback when the scenario does not need a nested `report:` block yet.

Use `--report-dir artifacts/demo` to emit the JSON/Markdown/HTML bundle from that basename in one replayable command.
