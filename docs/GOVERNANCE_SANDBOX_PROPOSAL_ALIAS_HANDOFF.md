# Governance sandbox proposal alias handoff

Keep scenario-file growth focused on reviewer-visible proposal import evidence.

## What to keep aligned
- Prefer one small alias at a time when extending proposal input support.
- Pair the alias with one replayable scenario fixture or test.
- Re-run the governance-sandbox report bundle proof so proposal import and markdown/html/json outputs stay coupled.

## Current low-risk alias lane
- `proposal_outline`
- `proposal_notes`
- `proposal_details`

## Reviewer check
Confirm the imported proposal still renders readable title/body text in the generated report bundle, not only in raw JSON.
