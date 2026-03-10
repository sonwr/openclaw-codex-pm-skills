# Web QA Playwright signoff scope examples

Use these examples after validation passes but the report still needs an honest handoff label.

## Checkpoint-scoped

Use when a single failed checkpoint has the clearest next move.

```text
Validator PASS. Signoff scope: checkpoint-only. Re-run the checkout address checkpoint with the saved selector evidence before calling the section ready.
```

## Section-scoped

Use when several failed checks belong to the same section and share the same recovery lane.

```text
Validator PASS. Signoff scope: section-only. Repair the checkout section blockers and collect a fresh screenshot plus trace before broader replay.
```

## Lane-scoped rerun

Use when the failure lane is known and replay support is already strong enough for a focused rerun.

```text
Validator PASS. Signoff scope: rerun lane. Retry the payment-submit lane with the recorded target and artifact bundle.
```

## Whole-run hold

Use when validation passes but the artifact still should not be described as full-run ready.

```text
Validator PASS, but signoff stays below whole-run scope. Owner coverage and next-action evidence are still incomplete for unresolved failed checks.
```

## Quick rule

Pick the narrowest honest scope that still matches the evidence. If the sentence starts sounding broader than the proof bundle, step back one scope level.
