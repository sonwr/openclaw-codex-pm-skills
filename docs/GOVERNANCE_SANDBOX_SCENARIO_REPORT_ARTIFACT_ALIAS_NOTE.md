# Governance Sandbox scenario report artifact alias note

When a scenario file uses `report.outputs.artifacts`, treat it as the same bundle contract as `report.outputs.files`: one scenario input should still fan out into one JSON/Markdown/HTML report bundle.

Keep the alias small and reviewable: scenario authors should be able to switch between `files` and `artifacts` without changing the validator expectation or the report bundle shape.
