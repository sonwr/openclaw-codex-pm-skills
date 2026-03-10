# Web QA Playwright Signoff Missing Fields

This guide explains how to handle signoff fields that are still missing even when a report is otherwise replay-ready.

## Why this matters

A run can pass structural validation while still carrying an incomplete signoff block.
The most common example is a missing `next_action` field.
That usually means the artifact is good enough to inspect, but not good enough to hand to another operator without extra interpretation.

## Common missing fields

- `next_action` — the concrete next repair or replay step
- `owner` or recovery owner metadata — who should take the next step
- `decision` / signoff outcome — whether the run is approved, blocked, or needs rerun
- evidence references — which artifact proves the signoff claim

## Triage rule of thumb

1. Treat missing signoff fields as handoff debt, not cosmetic debt.
2. Fill `next_action` first when only one field is missing.
3. If multiple fields are missing, prefer the order: outcome -> owner -> next action -> evidence reference.
4. Do not describe a report as fully handoff-ready until the signoff block is complete.

## Example

A validator summary like this:

```text
signoff field coverage: 75.00% (1 missing field(s))
missing signoff fields: next_action
```

should be interpreted as:

- the report is structurally valid,
- the main replay hotspot can still be identified,
- but the downstream operator still needs an explicit next step before the artifact is merge-ready.

## Suggested authoring pattern

Use a short, imperative `next_action` line:

```text
Repair missing timestamps for F1-F5, rerun strict-plus validation, then refresh signoff.
```

That format keeps the signoff block actionable and easy to transfer across chat, PR comments, and incident handoff docs.
