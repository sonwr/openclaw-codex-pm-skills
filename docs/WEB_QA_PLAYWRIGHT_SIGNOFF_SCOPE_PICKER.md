# WEB_QA_PLAYWRIGHT_SIGNOFF_SCOPE_PICKER

Use this card when a validator-clean report needs a fast, honest scope label before handoff.

## Goal

Pick the narrowest true signoff scope so the handoff stays reviewable.

## Scope choices

1. **Checkpoint scope** — use when one failed checkpoint has a stable target, artifact, and next action.
2. **Lane scope** — use when several checkpoints share the same blocked lane and the repair owner is the same.
3. **Section scope** — use when the blocker spans multiple lanes inside one section and the report still should not sound whole-run ready.
4. **Whole-run scope** — use only when replay blockers, owner gaps, and unresolved failed-check coverage are all cleared.

## Quick picker

Choose the first line that is true:

- Only one checkpoint needs follow-up → checkpoint scope.
- One hotspot lane clearly dominates → lane scope.
- One section still owns the unresolved work → section scope.
- No narrower boundary is needed and signoff coverage is complete → whole-run scope.

## Posting rule

If two scopes both seem possible, post the narrower one and name the wider scope as a follow-up review question.
