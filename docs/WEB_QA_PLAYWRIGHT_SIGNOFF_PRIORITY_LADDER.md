# Playwright signoff priority ladder

Use this ladder after strict-plus validation passes but the report still feels too broad for a clean handoff.

## 1. Replay blocker first

Start with the section that still has the highest replay-blocker count.
If there is a tie, prefer the lane that blocks the most failed checks from being replayed in one rerun.

## 2. Owner clarity second

If two lanes have similar blocker weight, choose the one whose owner is already known.
That keeps the next action shippable instead of turning the handoff into another triage round.

## 3. Proof target third

Prefer the lane that already names the artifact, page, or checkpoint that will prove the fix.
A lane with a visible proof target is easier to rerun and easier to audit.

## 4. Bundle the handoff in one sentence

A compact handoff sentence should answer four things:

- which lane is hottest,
- who owns it,
- what proof target should change,
- and whether the next move is rerun or repair.

## Quick template

`Priority lane: <section> (<owner>) because it carries the hottest replay blocker load; update <proof target> before the next rerun.`

## English note

Keep the ladder short enough to use during a passing-but-not-handoff-ready review.
The goal is not more taxonomy; it is faster, more specific rerun routing.
