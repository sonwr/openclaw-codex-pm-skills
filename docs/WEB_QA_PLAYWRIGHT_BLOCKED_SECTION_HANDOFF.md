# Web QA Playwright blocked-section handoff

Use this mini handoff when a strict-plus report says a section is still replay-blocked and you need to move repair work to the next operator without losing deterministic context.

## 1) Copy the blocked lane first

Prefer the section-scoped replay fields already emitted by the validator:

- `effective_replay_readiness_hotspot_primary_blocker_by_section`
- `effective_replay_readiness_hotspot_primary_blocker_summary_by_section`
- `effective_replay_readiness_hotspot_primary_blocker_next_step_by_section`

These fields preserve the section (`functional`, `visual`, `off_happy`), blocker key, checkpoint ids, and the first repair sentence.

## 2) Keep the handoff to one repair lane

A good blocked-section handoff answers four things only:

1. which section is blocked,
2. which blocker dominates it,
3. which checkpoint ids are inside that blocker lane,
4. what the next deterministic repair step is.

Avoid mixing multiple sections into one sentence unless they are explicitly tied and the receiver cannot act on only one lane.

## 3) Preferred handoff sentence

```text
Blocked section: functional -> missing_target_refs at CP2, CP3. Next step: restore stable target refs for each failed checkpoint, rerun only the affected lane, then confirm evidence artifacts before signoff.
```

## 4) When to stop and rerun

Rerun after the blocked lane has both:

- stable target refs for every affected checkpoint, and
- artifact evidence for the same checkpoint set.

If either dimension is still missing, keep the report in BLOCKED state and do not write a READY-style signoff summary.

## 5) Fast operator checklist

- Identify the blocked section from JSON, not from memory.
- Copy the section-specific blocker summary instead of rebuilding it manually.
- Repair one blocker lane at a time.
- Re-run validation after the repair.
- Promote the section to READY only after refs and evidence both exist.
