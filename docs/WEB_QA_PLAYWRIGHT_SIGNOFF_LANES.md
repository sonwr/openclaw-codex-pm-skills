# Web QA Playwright signoff lanes

Use this note when a strict-plus JSON artifact already exists and you need to decide the next deterministic replay lane quickly.

This doc follows the same Playwright-interactive priorities used elsewhere in the repo:

1. stabilize the run context first,
2. read machine-visible blockers before prose,
3. repair one lane at a time,
4. confirm recovery before broad reruns.

## Quick lane split

Read these JSON fields first:

- `effective_replay_ready_sections`
- `effective_replay_blocked_sections`
- `effective_replay_section_status`
- `effective_replay_readiness_hotspot_primary_blocker`
- `effective_replay_readiness_hotspot_primary_blocker_by_section`
- `effective_replay_readiness_hotspot_next_step_by_section`

Interpret them as follows:

- **READY lane**: sections listed in `effective_replay_ready_sections` can be reused as-is for the next replay pass.
- **BLOCKED lane**: sections listed in `effective_replay_blocked_sections` still have a deterministic blocker and should be repaired before wider reruns.
- **Hotspot lane**: use `effective_replay_readiness_hotspot_primary_blocker` when you want one global first fix, or `..._by_section` when each blocked section should keep its own first-fix owner.

## Recommended operator order

### 1) Freeze replay context

Before touching the blocked section, keep these stable:

- same replay preset (`--strict-plus` or one replay-profile alias)
- same browser profile / environment metadata
- same target-ref naming scheme
- same artifact-path naming scheme

If any of those changed, repair the environment first and regenerate the JSON artifact before triage.

### 2) Reuse READY sections untouched

If `functional` is READY and `visual` is BLOCKED, do not rewrite functional checkpoints just because the report is open. Preserve already-replayable evidence.

### 3) Repair only the hottest blocker lane

Use the blocker key to pick the first deterministic repair:

- `missing_target_refs` -> restore selector traceability first
- `incomplete_evidence_refs` -> restore artifact paths / evidence refs second
- `missing_checkpoint_timestamps` or ordering blockers -> repair chronology next
- status or signoff blockers -> fix the final verification/handoff layer last

### 4) Re-run one isolated fixture or one blocked section

Do not widen to the whole suite immediately. Re-run the single blocked fixture/section that proves the blocker is gone.

### 5) Confirm READY/BLOCKED split again

After repair, regenerate JSON and confirm:

- the repaired section moved from BLOCKED to READY, or
- the hotspot blocker changed to the next expected lane.

## Copy-ready reviewer note

Use a short note like this in PRs or handoffs:

```text
Replay triage lane: BLOCKED -> visual
Primary blocker: incomplete_evidence_refs
Next deterministic step: restore missing artifact refs for V1/V2, rerun only the visual lane, then regenerate strict-plus JSON.
```

## When to read other docs

- Need the overall execution loop? Read `docs/WEB_QA_PLAYWRIGHT_EXECUTION_LOOP.md`.
- Need pre-run stability rules? Read `docs/WEB_QA_PLAYWRIGHT_PRECHECK.md`.
- Need section/blocker JSON semantics? Read `docs/WEB_QA_PLAYWRIGHT_JSON_HANDOFF.md`.
- Need repair-order details? Read `docs/PLAYWRIGHT_INTERACTIVE_REPAIR_LOOP.md`.
