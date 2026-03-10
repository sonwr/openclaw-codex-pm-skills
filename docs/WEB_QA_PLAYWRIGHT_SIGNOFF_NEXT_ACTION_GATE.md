# Web QA Playwright signoff next-action gate

Use this card after a report passes validation but before you call it signoff-ready.

## Ask these three questions

1. Does the `Next action:` sentence name the hottest blocked lane?
2. Does it point to the proof target or artifact needed for replay?
3. Does it make the owner handoff obvious without reopening the full JSON?

If any answer is no, the artifact is validator-clean but not signoff-ready.

## Compact rewrite pattern

Use:

```text
Next action: <owner> repairs <hotspot/check ids> by reproducing <target/artifact> and rerunning strict-plus validation.
```

## Fast examples

- Good: `Next action: QA owner repairs F2/F3 by recapturing checkout screenshots and rerunning strict-plus validation.`
- Weak: `Next action: investigate failures.`

## When to stop at signoff instead

If the report has no failed checks, no replay blockers, and complete signoff ownership metadata, keep the next action focused on approval or archival instead of repair.
