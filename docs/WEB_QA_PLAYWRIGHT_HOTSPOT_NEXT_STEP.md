# WEB_QA_PLAYWRIGHT_HOTSPOT_NEXT_STEP

Use this note when strict-plus JSON already identifies the replay hotspot and you only need the next repair sentence.

## When to open this

Open this after validation passes enough to emit replay metadata, but the report is still blocked by a hotspot section or blocker lane.

Typical signal:

- `effective_replay_readiness_hotspot_next_step` is present in JSON
- one section dominates blocker count
- the operator needs a one-screen decision before rerunning

## 60-second loop

1. Read the hotspot section label first (`functional`, `visual`, or `off_happy`).
2. Read the primary blocker key next.
3. Copy the JSON-provided `effective_replay_readiness_hotspot_next_step` sentence as the default rerun brief.
4. Repair only that blocker layer.
5. Re-run the validator before widening scope.

## Repair order

Keep the replay repair order deterministic:

1. target refs
2. artifact evidence
3. timestamps / chronology
4. status consistency
5. owner handoff / next action

## Example handoff

```text
Hotspot: functional
Blocker: missing_timestamps
Next step: Repair `missing_timestamps` across hotspot checkpoints: F1, F2, F3, F4, F5.
```

## Rule of thumb

If the hotspot next-step sentence already names the blocker and checkpoint ids, do not rewrite the whole report first.
Repair that exact lane, rerun validation, then decide whether broader cleanup is still needed.
