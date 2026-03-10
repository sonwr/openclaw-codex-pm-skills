# Web QA Playwright replay signals

This note defines the smallest signal set a human or bot should scan before deciding whether a blocked run is replay-ready.

## Priority order

1. `effective_replay_section_status`
2. `effective_replay_readiness_hotspot_primary_blocker`
3. `effective_replay_readiness_hotspot_next_step`
4. `next_action_replay_support_level`
5. `unresolved_failed_check_handoff_summary`

## How to use the signals

- Start with section status to decide whether the next rerun lane is `functional`, `visual`, or `off_happy`.
- Read the hotspot blocker object before opening the full checkpoint list.
- Use the hotspot next-step sentence as the default handoff text when a repair owner needs one copy-ready instruction.
- If `next_action_replay_support_level` is `none`, expect to add stable target refs and artifact refs before the rerun is considered deterministic.
- If `unresolved_failed_check_handoff_summary` is non-empty, do not claim the report is fully replay-ready even when the section counts look stable.

## Recommended operator sentence

Use this compact sentence in tickets, PR comments, or chat handoff:

```text
Replay lane: <section> | blocker: <blocker_key> | next step: <copy-ready next step> | failed-check handoff: <summary or none>
```

## Why this doc exists

The validator already emits rich strict-plus metadata, but rerun operators often need a stable first-look order more than another long JSON dump. This guide keeps the first scan deterministic.
