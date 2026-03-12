# Governance-sandbox nested report output files note

When governance-sandbox scenario work already owns the report artifact contract, keep the JSON, Markdown, and HTML paths together under `report.outputs.files`.

Use this when one scenario fixture should hand off `files.json`, `files.markdown`, and `files.html` as a single reviewable bundle instead of repeating separate sibling keys.

That keeps scenario-file input and report generation progress visible in one compact PM-facing check.
