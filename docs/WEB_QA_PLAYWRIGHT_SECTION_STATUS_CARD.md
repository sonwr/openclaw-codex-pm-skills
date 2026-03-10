# Web QA Playwright Section Status Card

Use this mini-card when you need to hand one report section to the next operator without pasting the full validation JSON.

## Copy-ready format

```text
Section: <functional|visual|off_happy>
Status: <READY|BLOCKED>
Primary blocker: <missing_target_refs|incomplete_evidence_refs|missing_timestamps|status_inconsistency|none>
Checkpoint ids: <comma-separated ids or none>
Next step: <single deterministic repair instruction>
```

## When to use it

Use the card when:

- strict-plus JSON already identified a blocked or ready section,
- you want one short rerun handoff per section,
- or a reviewer needs a human-readable summary before reopening the full artifact.

## How to fill it

1. Copy the section name from `effective_replay_section_status`.
2. If the section is blocked, copy the blocker from `effective_replay_readiness_hotspot_primary_blocker_key_by_section` when available.
3. Copy checkpoint ids from `effective_replay_readiness_hotspot_primary_blocker_checkpoint_ids_by_section`.
4. Copy the repair sentence from `effective_replay_readiness_hotspot_primary_blocker_next_step_by_section`.
5. If the section is ready, keep `Primary blocker: none` and `Checkpoint ids: none`.

## Example

```text
Section: visual
Status: BLOCKED
Primary blocker: incomplete_evidence_refs
Checkpoint ids: V2, V3
Next step: Re-run visual checkpoints V2 and V3, attach fresh artifact paths, then confirm the same stable target refs remain valid before signoff.
```

## Why this exists

The full JSON contract is intentionally rich. This card exists for the opposite need: one small, deterministic section-level handoff that still preserves blocker type, checkpoint scope, and the next repair action.
