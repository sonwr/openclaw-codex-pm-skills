# Web QA Playwright step template

A copyable checkpoint template for teams that want Playwright-interactive discipline in markdown QA reports without inventing a format from scratch.

## Why this exists

Interactive browser testing breaks down when one checkpoint mixes multiple actions, vague evidence, and missing recovery ownership.
This template keeps each checkpoint stable, reproducible, and easy to replay.

## One-checkpoint template

Use the block below when drafting a new checkpoint or repairing a flaky one.

```md
### Checkpoint F1 — Open the checkout screen

- Target ref: `e12`
- Preconditions: logged in as seeded buyer, cart already contains 1 item, viewport `1440x900`
- Action: click `Checkout`
- Expected state: shipping form is visible and the order summary still shows 1 item
- Evidence: `artifacts/f1-checkout-open.png`
- Verification note: URL changed to `/checkout`, heading `Checkout` is visible
- If this fails: classify as `selector` / `runtime` / `product`, name the owner, and write `Next action:` before widening scope
```

## Quick drafting checklist

Before you mark a checkpoint as complete, confirm all of the following:

1. **One action burst only** — the checkpoint covers one meaningful state transition.
2. **Explicit preconditions** — the starting state is copyable by another reviewer.
3. **Immediate verification** — the expected state is checked right after the action.
4. **Replay-ready evidence** — screenshot/log/trace paths are unique and tied to this checkpoint.
5. **Recovery-first handoff** — any failure names classification, owner, and next action before adjacent checks continue.

## Functional / visual / off-happy examples

### Functional checkpoint

- Goal: prove the requested behavior happened.
- Best evidence: screenshot + visible state marker + URL/title/assertion note.

### Visual checkpoint

- Goal: prove the signed-off UI state matches the claim.
- Best evidence: screenshot captured only after the target state is stable.

### Off-happy checkpoint

- Goal: prove a fragile or failure-prone path is understood.
- Best evidence: explicit failure classification plus a recovery note if the path blocks signoff.

## Recovery ladder

Use the smallest recovery scope that matches the failure.

1. **Selector issue** — repair the locator, rerun the affected checkpoint, then continue.
2. **Runtime issue** — reload or relaunch according to the execution loop, rerun the affected checkpoint, then continue.
3. **Product issue** — keep the evidence, mark the report as blocked, and point `Next action:` at the failed check ids.

## Recommended pairing

- Read this template with `docs/WEB_QA_PLAYWRIGHT_EXECUTION_LOOP.md` for the full signoff loop.
- Use `docs/WEB_QA_PLAYWRIGHT_STABILITY_CHECKLIST.md` when you need a shorter pre-rerun reminder.
- Use `docs/WEB_QA_PLAYWRIGHT_FAILURE_HANDOFF.md` when a failed checkpoint needs owner + replay metadata.
