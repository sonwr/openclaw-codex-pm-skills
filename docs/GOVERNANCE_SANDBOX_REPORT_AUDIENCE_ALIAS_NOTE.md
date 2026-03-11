# Governance Sandbox report audience alias note

Use this note when a governance-sandbox scenario fixture needs one reviewer-facing audience field without duplicating memo copy across CLI, docs, and web-demo handoff payloads.

## Preferred order
1. Keep `report.audience` as the primary field inside the fixture.
2. Allow `report_readers`, top-level `report_audience`, or top-level `audience` only as import aliases.
3. Verify the generated markdown/html memo shows the resolved audience string once.

## Why it exists
- Scenario-file-first report bundles should keep audience metadata inside the same replayable fixture.
- Web demo and Playwright proof loops should read the same audience text instead of hard-coding card copy.
- Reviewer handoff should not require a second manually maintained memo note.
