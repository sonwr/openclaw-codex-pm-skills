# Web QA Playwright next-action coverage

Use this checklist when the validator reports failed checks but the signoff `Next action` is still too vague for replay handoff.

## What a complete next action should cover

1. Name every failed check id that still needs work.
2. Say who owns the recovery when the report already records a recovery owner.
3. Mention the replay intent (`rerun`, `replay`, `capture fresh evidence`, or equivalent).
4. Keep the sentence short enough to copy into a ticket, PR comment, or follow-up runbook.

## Good examples

- `Fix F2 selector drift with qa-ui, capture fresh evidence, and rerun deterministic replay before signoff.`
- `Route V2 to design-systems, update spacing token, and rerun screenshot coverage for V2.`
- `Repair F1 and F3 with checkout-team, capture new artifacts, and rerun the blocked checkout flow.`

## Weak examples

- `Investigate the issue.`
- `Rerun later.`
- `Fix the bug and retest.`

## Quick review prompts

- Can a reviewer see which failed checks are still unresolved?
- Can an owner tell whether they need to fix code, selectors, or product behavior?
- Does the line tell the next runner which replay or rerun should happen?

## Related docs

- `docs/WEB_QA_PLAYWRIGHT_FAILURE_HANDOFF.md`
- `docs/WEB_QA_PLAYWRIGHT_JSON_HANDOFF.md`
- `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_REPLAY_CARD.md`
