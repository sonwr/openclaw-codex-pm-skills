# Web QA Playwright next-action rerun decider

Use this card after strict or strict-plus validation already passed, but the report still needs a narrow next action.

## Goal

Decide whether the next action should stay a rerun cue, expand into a repair handoff, or stop at signoff review.

## Fast order

1. Check whether every failed check id is named in `Next action:`.
2. Check whether stable target refs are already present.
3. Check whether fresh artifact refs are already present.
4. If both refs are missing, write a repair-first handoff instead of a rerun-first sentence.
5. If failed checks + targets + artifacts are all present, keep the next action rerun-scoped.

## Decision guide

- **Rerun now** — failed check ids, stable target refs, and artifact refs are all present.
- **Repair first** — failed check ids are present, but target refs or artifact refs are still missing.
- **Signoff only** — there are no unresolved failed checks and the artifact is already signoff-ready.

## Copy-ready phrasing

- Rerun now: `Rerun F2 against the saved target refs, capture fresh artifacts, and confirm the blocked lane clears.`
- Repair first: `Repair missing target/artifact refs for F2 before requesting a focused rerun.`
- Signoff only: `No rerun requested; move to signoff review with the validated artifact.`
