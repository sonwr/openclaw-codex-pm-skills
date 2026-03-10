# Web QA Playwright section repair order

Use this note when a strict-plus report already exposes section replay metadata and you need one deterministic repair order without reopening the full report.

## Repair order

1. Split the run into `READY` vs `BLOCKED` lanes from `effective_replay_section_status`.
2. Start with the hotspot section from `effective_replay_readiness_hotspot_tied_section_labels` or `effective_replay_readiness_hotspot_primary_blocker_by_section`.
3. Fix the dominant blocker key before any lower-frequency cleanup in that same section.
4. Re-run only the checkpoints listed under `effective_replay_readiness_hotspot_primary_blocker_checkpoint_ids_by_section`.
5. Confirm the repaired section now has stable target refs, artifact refs, and timestamps before moving to the next section.

## Operator checklist

- `functional` first when hotspot counts tie and a product-critical happy path is blocked.
- `visual` first when screenshot or layout evidence is the only missing artifact lane.
- `off_happy` first when the unresolved blocker belongs to error handling or guardrail coverage.
- If a section is already `READY`, do not replay it just to gather nicer prose.

## Minimal handoff sentence

Copy this structure into the next rerun note:

`Repair <section> first: blocker=<blocker_key>; checkpoints=<ids>; prove recovery with fresh ref + artifact + timestamp.`
