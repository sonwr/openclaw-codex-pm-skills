# Governance Sandbox report.file_stem alias note

Use `report.file_stem` when one scenario fixture should drive a reusable JSON/Markdown/HTML bundle basename without changing the visible report title.

Quick check:

1. Put `report.file_stem` in the scenario file.
2. Run `--report-dir` once.
3. Confirm the `.json`, `.md`, and `.html` artifacts all reuse that shared basename.
