# Web QA Playwright replay input stability

Use this note when a replay loop keeps failing even though the visible page looks unchanged.

## Stable replay input order

1. Reuse the same target refs captured in the prior validated report whenever they still resolve.
2. Prefer explicit scenario inputs over improvised re-entry during repair loops.
3. Keep checkpoint ids and checkpoint order unchanged unless the scenario itself changed.
4. Regenerate artifacts only after the minimal repair step completes.

## Handoff note

A replay handoff is stronger when it says which inputs stayed stable and which ones had to be re-captured.
