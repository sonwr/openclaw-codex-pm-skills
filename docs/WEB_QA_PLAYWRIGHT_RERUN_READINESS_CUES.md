# Web QA Playwright rerun readiness cues

Use this page when strict-plus validation already passed, but the team still needs a fast answer to: **"Can we rerun now, or do we still need repair work first?"**

## Green-light cues

A rerun is usually the next move when all of the following are true:

- failed check ids are named clearly,
- the next action references the failed check ids directly,
- at least one target ref or selector clue exists,
- at least one artifact path or screenshot reference exists,
- and the recovery owner is obvious from the failure notes.

## Yellow-light cues

Pause for a short repair pass when the report is valid but one of these is still weak:

- next action says "rerun" without naming the failing check,
- artifact evidence exists but does not match the failing step,
- target refs are implied in prose but not captured as concrete refs,
- or multiple owners could claim the same failure.

## Red-light cues

Do not call the report rerun-ready yet when any of these apply:

- the failed lane has no artifact path,
- the next action does not cover every failed check id,
- checkpoint notes do not explain where the replay diverged,
- or signoff still hides owner or section-level blocker gaps.

## Fast wording pattern

Use a short rerun-ready sentence that names the lane, artifact, and owner:

> Rerun-ready for F2 with `artifacts/f2-failure.png`, target `/login`, owner `qa-product`.

That sentence is short enough for PR handoff notes but still preserves the replay essentials.
