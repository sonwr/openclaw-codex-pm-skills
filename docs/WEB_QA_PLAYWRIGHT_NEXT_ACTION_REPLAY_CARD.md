# Next-action replay card

Use this compact card when a Playwright-style interactive run is blocked and the rerun owner needs a deterministic first move.

## Why this exists

`Next action:` prose is often the first thing people copy into a ticket, Slack thread, or rerun note.
If that line does not preserve stable refs, artifact paths, and a repair order, recovery becomes guesswork.

This card keeps the handoff small while preserving the principles from the interactive Playwright guidance:

1. stabilize the same target before changing scope,
2. repair one checkpoint at a time,
3. verify after every recovery step,
4. keep refs and artifacts explicit so the rerun stays reproducible.

## Copy-ready shape

```text
Next action: Repair F2 using ref=e17, compare `artifacts/f2-before.png` vs `artifacts/f2-after.png`, rerun login submit once, then confirm PASS evidence in the execution log.
```

## Minimum fields

- **Failed check id** — keep the blocked lane explicit (`F2`)
- **Stable target ref** — preserve the UI anchor (`ref=e17`)
- **Artifact refs** — point to the evidence you are comparing or replacing
- **Single rerun verb** — rerun one path, not the whole suite
- **Verification cue** — say what PASS condition must be confirmed before signoff

## Repair order

1. Reuse the original target ref when possible.
2. Compare the latest failure artifact with the replacement artifact.
3. Rerun only the affected step or narrow path.
4. Record the verification outcome in the execution log before broadening scope.

## Anti-patterns

Avoid these weak handoffs:

- `Next action: investigate login bug`
- `Next action: rerun tests`
- `Next action: look into screenshot issue later`

They omit refs, evidence, repair order, and verification.

## Good / better examples

### Too vague

```text
Next action: Investigate F2.
```

### Better

```text
Next action: Repair F2 selector drift at ref=e17, capture a fresh `artifacts/f2-selector-fix.png`, rerun the login submit path, and confirm the toast checkpoint passes.
```

### Best when two evidence points matter

```text
Next action: Repair F2 at ref=e17, compare `artifacts/f2-timeout-before.png` with `artifacts/f2-timeout-after.png`, rerun only the login submit path, and confirm PASS evidence plus timestamped recovery in the execution log.
```

## When to escalate

Escalate instead of rerunning immediately when:

- the original target ref is gone and cannot be repaired deterministically,
- artifact refs are missing for the failed checkpoint,
- multiple blocker classes are mixed into one next-action sentence,
- chronology is broken and checkpoint timestamps cannot prove the rerun order.

In those cases, repair the report metadata first before expanding the rerun scope.
