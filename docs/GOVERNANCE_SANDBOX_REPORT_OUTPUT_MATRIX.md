# Governance Sandbox Report Output Matrix

Use this note when you want a fast artifact check after replaying one governance-sandbox scenario file.

Expected bundle:
- JSON: machine-readable simulation output
- Markdown: reviewer-friendly memo
- HTML: shareable visual report
- Optional alias files: `report.json`, `report.md`, `report.html` when a named basename is also emitted

Fast check:
1. Confirm the scenario file resolved cleanly.
2. Confirm the report directory contains JSON, Markdown, and HTML outputs.
3. Confirm the report metadata points at the same artifact paths.
4. Confirm the markdown/html headings still match the selected report title.
