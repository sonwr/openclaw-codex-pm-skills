# Web QA Playwright signoff artifact reuse

Use this note when a signoff-ready failure report should be replayed or escalated without losing the original evidence trail.

## Reuse order

1. Reuse the original report path and execution log reference before copying snippets into chat or tickets.
2. Keep the failing check refs and target refs together so downstream reviewers can replay the same hotspot.
3. Carry forward recovery owner, next action, and blocker priority fields in the same handoff.
4. Add only fresh screenshots or traces that change the decision; do not duplicate unchanged artifacts.

## Minimum signoff handoff

- failing section or checkpoint
- artifact paths used for proof
- blocker priority
- assigned recovery owner
- next action for rerun, repair, or escalation

## Escalate instead of reusing when

- the artifact path is missing or no longer accessible
- target refs changed between runs
- the report mixes evidence from different reruns without labeling them
- the current owner cannot reproduce the blocker with the reused artifact set
