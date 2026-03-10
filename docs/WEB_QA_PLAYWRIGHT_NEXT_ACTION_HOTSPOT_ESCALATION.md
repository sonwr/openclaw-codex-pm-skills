# Web QA Playwright next-action hotspot escalation

Use this note when a passing validator artifact still has multiple blocked lanes and the handoff writer needs one escalation sentence.

## When to use it

Use this guide when:

- strict or strict-plus validation already passes,
- more than one failed lane still looks actionable,
- and the team needs one hotspot-first escalation line instead of a long replay summary.

## Default escalation order

1. Name the failed check with the highest blocker density.
2. Name the stable target or screen when it exists.
3. Name the missing artifact or evidence refresh needed for the rerun.
4. End with the owner or rerun cue.

## Compact sentence template

`Escalate <failed-check-id> on <target/screen>; refresh <artifact/evidence>; rerun with <owner-or-lane>.`

## Example

`Escalate F2 on login spinner timeout; refresh artifacts/f2-failure.png and fresh dashboard evidence; rerun with qa-runtime.`

## Quick reject rule

If the sentence does not identify a failed check id, a proof target, and a rerun or owner cue, it is still too vague for handoff.
