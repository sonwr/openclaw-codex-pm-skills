# Governance sandbox report_readers alias note

Use `report.report_readers` when a scenario fixture wants reviewer-facing audience metadata to stay nested under the report block.

Keep it equivalent to `report.audience`, `report.audiences`, and top-level `report_readers` so one scenario replay can still prove the same JSON, Markdown, and HTML audience handoff.
