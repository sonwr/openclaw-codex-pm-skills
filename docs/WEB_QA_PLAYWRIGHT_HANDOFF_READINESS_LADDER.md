# Web QA Playwright handoff readiness ladder

Use this ladder after validation passes but before you call a report rerun-ready or handoff-ready.

## Level 1 — Validator-clean

Required signs:

- strict or strict-plus validation passes,
- checkpoint formatting is coherent,
- missing-field output is understood.

Question:

- Is the artifact structurally valid, even if the next action is still weak?

## Level 2 — Signoff-complete

Required signs:

- signoff fields are present,
- missing signoff fields are either zero or explicitly accepted,
- the report can survive a quick reviewer skim.

Question:

- Can another operator understand the current state without reopening raw logs?

## Level 3 — Owner-routable

Required signs:

- failed checks have recovery owners,
- owner gaps are either zero or explicitly called out,
- the next action names the repair lane clearly.

Question:

- If this artifact changes hands right now, will the receiving owner know it belongs to them?

## Level 4 — Replay-routable

Required signs:

- blocker hotspot is obvious,
- checkpoint ids to revisit are named,
- the rerun scope is smaller than the whole suite when possible.

Question:

- Can the next operator replay the right lane first instead of restarting from scratch?

## Level 5 — Handoff-ready

Required signs:

- the artifact is validator-clean,
- signoff-complete,
- owner-routable,
- replay-routable,
- and the next action can be pasted directly into a task or PR comment.

Question:

- Does the report tell the next person what happened, where to look, and what to do next in one pass?

## Shortcut rule

If you cannot answer yes through Level 4, do not call the artifact handoff-ready yet.
