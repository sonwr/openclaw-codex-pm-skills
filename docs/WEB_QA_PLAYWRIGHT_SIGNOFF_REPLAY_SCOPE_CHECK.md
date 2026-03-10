# Web QA Playwright signoff replay scope check

Use this note when a validator-PASS artifact still feels too broad for a clean handoff.

## Goal

Decide whether the signoff language should stay:

- checkpoint-scoped,
- section-scoped, or
- whole-run scoped.

## Fast check

Keep the handoff narrow unless all of these are true:

1. the highest blocker lane is named,
2. the next action already identifies the proof target,
3. owner routing is obvious from the artifact,
4. unresolved failed checks are either absent or explicitly scoped.

## Safe wording cues

- **Checkpoint scope** — use when a single failed check or unstable target still dominates the replay risk.
- **Section scope** — use when one section is repairable as a bundle, but other sections still need separate review.
- **Whole-run scope** — use only when replay blockers, owner gaps, and next-action ambiguity are all cleared.

## Default rule

If you hesitate between two scopes, choose the narrower one and name the remaining blocker or owner gap directly.
