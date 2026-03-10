# Web QA Playwright hotspot handoff card

Use this card when strict-plus validation already exposed a replay hotspot and the next operator needs the shortest possible rerun brief.

## What to capture first

1. `effective_replay_readiness_hotspot_section`
2. `effective_replay_readiness_hotspot_primary_blocker.key`
3. `effective_replay_readiness_hotspot_checkpoint_ids`
4. `effective_replay_readiness_hotspot_next_step`
5. `next_action_replay_support`

## Copy-ready handoff shape

```text
Hotspot section: <section>
Primary blocker: <blocker key>
Checkpoint ids: <checkpoint ids>
Next step: <copy-ready rerun sentence>
Replay support: <target_and_artifact_refs|target_refs_only|artifact_refs_only|none>
```

## Operator rule

- If replay support is `none`, repair target refs and artifact refs before asking for a rerun.
- If replay support is partial, keep the handoff scoped to the missing dimension instead of rewriting the whole report.
- If multiple sections tie, keep the tied sections explicit until one section gains a clear blocker lead.
