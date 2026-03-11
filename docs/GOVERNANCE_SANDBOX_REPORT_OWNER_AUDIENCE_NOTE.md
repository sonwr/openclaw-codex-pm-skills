# Governance Sandbox Report Owner + Audience Note

Use this note when one governance-sandbox scenario file needs to keep both `report.owner` and `report.audience` visible in the same replayable JSON/Markdown/HTML bundle.

## What to check

- the scenario file declares the intended audience
- the scenario file declares the owner or handoff person
- the generated bundle keeps both fields readable without reopening the raw JSON

Keep the proof small: one scenario file, one generated report bundle, one reviewer-visible owner/audience check.
