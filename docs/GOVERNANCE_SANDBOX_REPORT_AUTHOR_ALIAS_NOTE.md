# Governance Sandbox report-author alias note

When a governance-sandbox scenario fixture already uses `report_author` or `report_authors`, treat those fields as report-owner aliases instead of forcing a rename before validation.

Keep the handoff small:
- one scenario file
- one owner line in the generated memo
- one green validator run before push
