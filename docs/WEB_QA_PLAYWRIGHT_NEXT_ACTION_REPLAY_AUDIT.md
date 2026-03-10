# Web QA Playwright next-action replay audit

Use this quick audit when the validator already passes but you still need to decide whether the `Next action:` line is replay-ready enough for handoff.

## Goal

Confirm that a passing report names the right failed lane, the right proof target, and a narrow rerun path before someone else picks it up.

## Four-line audit

1. **Failed check coverage** — Does the sentence name every failed check id that still blocks the lane?
2. **Target clarity** — Does it say what should be reopened, rerun, or inspected next?
3. **Artifact clarity** — Does it mention the screenshot, trace, log, or fixture gap that should be refreshed?
4. **Replay boundary** — Does it keep the work scoped to the smallest useful rerun instead of asking for a vague full replay?

## Safe status language

- **Replay-ready** — failed checks, target, and proof asset are all obvious from one sentence.
- **Rerun-ready but thin** — failed checks are named, but the next operator still has to guess the proof asset.
- **Not handoff-ready** — the sentence sounds actionable, but it does not identify the blocked lane precisely enough to replay.

## Example

```text
Next action: Rerun F2 login submit against `/login`, refresh `artifacts/f2-failure.png`, and confirm whether the spinner clears before signoff.
```

That sentence keeps the lane small, names the target, and tells the next operator which artifact should change.
