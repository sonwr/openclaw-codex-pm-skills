# WEB QA Playwright recovery-owner drill

Use this drill when a browser automation run fails and you need a repeatable, reviewer-friendly recovery handoff.

It turns the Playwright-interactive principles into a small loop:

1. **Stabilize the target** — keep the same tab/session, reuse stable refs when possible, and avoid jumping ahead before the UI state is confirmed.
2. **Verify step-by-step** — record what was attempted, what changed, and which checkpoint or check id failed.
3. **Assign recovery clearly** — every failed check should name a recovery owner before the report is handed off.
4. **Prepare replay evidence** — keep the artifact path, target ref, and next rerun instruction together so the next operator can reproduce the state quickly.

## Minimal recovery-owner template

```text
- Failed check: F2 — checkout CTA stayed disabled after shipping form fill.
  - Evidence: screenshot `artifacts/checkout-disabled.png`
  - Target ref: `checkout.submit_button`
  - Recovery owner: qa-ui
  - Replay note: rerun from the saved checkout page state and verify the CTA after field blur.
```

## What to verify before handoff

- The failing check id is explicit (`F*`, `V*`, or `O*`).
- The next action references the same stable target ref or artifact evidence used in the failure note.
- The replay instruction is concrete enough to reproduce in one pass.
- The recovery owner is a team/person label the next runner can route immediately.
- If the issue is intermittent, say what was already retried and what should be retried next.

## Good handoff shape

```text
Next action:
- Reuse target ref `checkout.submit_button` on the current checkout tab and replay the final blur/submit sequence.
- If the CTA is still disabled, capture a fresh screenshot and compare against `artifacts/checkout-disabled.png`.
- Route the failure to Recovery owner: qa-ui if the state remains reproducible.
```

## Failure-recovery notes

- Prefer one recovery owner per failed check.
- If multiple teams are involved, assign the first unblocker and name downstream follow-up in the next action.
- Do not replace evidence with general guesses; keep the handoff tied to the exact failed check and saved artifact.

## Why this exists

A report can be detailed and still be hard to act on if it does not say **who owns the next recovery step**. This drill keeps the handoff reproducible, scoped, and easy to rerun.