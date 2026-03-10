# WEB_QA_PLAYWRIGHT_RERUN_SCOPE_LADDER

Use this quick ladder when a validator-clean report still needs a rerun handoff and the team is unsure how wide the rerun should be.

## Goal

Keep the rerun as narrow as the evidence allows while still naming a believable next step.

## Ladder

1. **Checkpoint scope** — choose this when one failed checkpoint already has a stable target ref, fresh artifact path, and an obvious repair action.
2. **Blocked-lane scope** — choose this when multiple checkpoints fail for the same blocker inside one lane (`functional`, `visual`, or `off_happy`).
3. **Section scope** — choose this when the lane is clear but the hotspot still spans several blocker families inside the same section.
4. **Whole-run scope** — choose this only when the report cannot isolate one trustworthy lane or the supporting replay metadata is incomplete.

## Fast decision cues

- If the hotspot JSON already names one blocker key and one lane, stay at **blocked-lane scope**.
- If the next action can cite exact failed check ids plus one proof artifact, stay at **checkpoint** or **blocked-lane scope**.
- If owner routing changes between checkpoints, widen to **section scope**.
- If stable refs or artifacts are missing across sections, do not fake precision; escalate to **whole-run scope**.

## Copy-ready reminder

> Prefer the smallest rerun scope that still preserves failed check ids, target refs, artifact proof, and owner routing.
