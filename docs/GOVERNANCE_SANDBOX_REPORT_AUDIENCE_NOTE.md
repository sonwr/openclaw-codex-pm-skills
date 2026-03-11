# Governance sandbox report audience note

Use this note when a governance-sandbox scenario needs to carry the intended memo audience directly into the generated markdown and HTML report.

## Why it exists

Scenario-file input is already the source of truth for proposal text, stakeholder presets, and report naming. Audience metadata belongs in that same file when the handoff target matters.

## Recommended pattern

- Put `report.audience` in the scenario file when the memo targets a specific reviewer group.
- Treat `report_audience` as a top-level fallback alias for thinner fixtures.
- Keep the wording short and role-oriented, for example: `Delegates preparing a treasury vote`.

## Verification loop

1. Run one scenario file through `--report-markdown` and confirm the memo includes a visible audience section.
2. Run the same scenario through `--report-html` and confirm the audience appears in the report summary panel.
3. Keep the audience string scoped to who should read the memo first, not the whole roadmap.
