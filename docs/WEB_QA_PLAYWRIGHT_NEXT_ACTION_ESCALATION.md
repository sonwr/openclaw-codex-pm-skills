# Web QA Playwright Next-Action Escalation

Use this note when a report already contains a plausible `next_action`, but the operator needs a quick rule for when that action should be escalated instead of retried.

## Escalate immediately when

- the same blocker appears across multiple reruns,
- the owner is unknown after the first triage pass,
- evidence is missing for a failed check and cannot be reconstructed from artifacts,
- a section is blocked by an upstream dependency instead of a local repair,
- a retry would repeat the same environment or selector assumptions.

## Keep local when

- the owner is known,
- the blocker is isolated to one section,
- the report still has enough evidence to support a targeted fix,
- the rerun plan changes one concrete input or dependency,
- the expected exit signal is explicit.

## Suggested handoff sentence

`Escalate this next action when the blocker survives one targeted rerun or when ownership remains unresolved after triage.`
