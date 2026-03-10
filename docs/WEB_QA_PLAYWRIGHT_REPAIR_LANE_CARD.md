# Web QA Playwright repair-lane card

Use this short card when a strict-plus JSON artifact already tells you which replay lane is hottest and you need one deterministic repair pass before opening the full report.

## 60-second repair lane flow

1. Read `effective_replay_readiness_hotspot_primary_blocker` first.
2. Copy the related `..._checkpoint_ids` list into the rerun note.
3. Keep the original target refs and artifact naming pattern unchanged.
4. Repair one blocker class only (`missing_target_refs`, `missing_artifact_refs`, `missing_timestamps`, `status_consistency`, or owner handoff drift).
5. Rerun the smallest section that still covers those checkpoint ids.
6. Revalidate the canonical PASS fixture before widening scope.

## Copy-ready lane note

```text
Repair lane: <section> / <blocker_key>
Checkpoint ids: <F1, F2, ...>
Keep fixed: preset/profile, target refs, artifact naming
Rerun scope: smallest section covering the unresolved checkpoints
Exit rule: validator passes or the same single blocker remains isolated
```

## Why this exists

- Turns hotspot JSON into an operator-ready rerun card.
- Prevents broad reruns before one blocker class is isolated.
- Keeps replay work aligned with Playwright-style stability and evidence discipline.
