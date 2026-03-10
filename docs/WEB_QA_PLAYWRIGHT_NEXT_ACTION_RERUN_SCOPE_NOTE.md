# Web QA Playwright next-action rerun scope note

Use this note after strict-plus validation passes but the report is still blocked on rerun clarity.

## 30-second check

1. Name the blocked section first (`functional`, `visual`, or `off_happy`).
2. Say whether the rerun stays checkpoint-scoped or expands to section scope.
3. Keep one stable target ref or artifact ref in the sentence.
4. End with the proof signal that should flip the lane to ready.

## Copy-ready pattern

`Next action: rerun <section> at <scope> scope, starting from <target/artifact>, and confirm <proof signal> before signoff.`

## Escalate scope when

- multiple checkpoints in the same section share the same blocker,
- the hotspot summary already points to section-wide evidence gaps,
- or the narrow rerun sentence cannot name a stable target.

## Stay narrow when

- one checkpoint owns the blocker,
- the target ref is already stable,
- and the proof artifact for success is obvious.
