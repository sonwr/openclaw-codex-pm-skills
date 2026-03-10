# WEB_QA_PLAYWRIGHT_NEXT_ACTION_HUMAN_READY_CHECK

Use this quick check after the validator passes but before you call a report handoff-ready.

## What this card is for

A validator-clean artifact can still be hard for another reviewer to act on.
Use this card to keep the `Next action:` sentence specific, owner-aware, and replay-friendly.

## 30-second check

Confirm all four points:

1. **Targeted lane** — name the exact blocked lane, failed checkpoint, or replay slice.
2. **Owner route** — say who should take the next step, even if that is a temporary owner alias.
3. **Proof target** — name the artifact, section, or fixture that should be updated or replayed next.
4. **Narrow scope** — keep the sentence lane-scoped; do not imply the whole run is ready.

## Good pattern

```text
Next action: QA owner reruns checkout failure lane using the current screenshot bundle and updates the signoff note if checkpoint C2 turns green.
```

## Warning signs

- Uses vague verbs like "follow up" or "check again"
- Omits the owner or evidence target
- Sounds like whole-run approval instead of a narrow repair or rerun handoff
- Hides unresolved failed checks behind generic PASS language
