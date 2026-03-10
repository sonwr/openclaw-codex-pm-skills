# Web QA Playwright Next-Action Handoff

Use this card when validation already passed but the report still needs a single, clear `next_action` before rerun or human handoff.

## When to use it

Use this guide if:

- replay readiness is blocked by missing or vague next steps,
- signoff coverage is almost complete except for the next action,
- owner routing is known but the actual repair move is still underspecified.

## 60-second handoff flow

1. Identify the dominant blocker section from the report metadata.
2. Name the first concrete repair step, not the whole recovery plan.
3. Tie the action to the failing checkpoint ids.
4. Point to the artifact or evidence gap that should change after rerun.
5. Keep the sentence short enough to paste into signoff without rewriting.

## Good `next_action` shape

Prefer this format:

```text
Repair <primary blocker> across <checkpoint ids>, then rerun the affected section and refresh the failure evidence.
```

Examples:

- `Repair missing timestamps across F2 and F4, then rerun the functional section and refresh the failure evidence.`
- `Capture the missing visual artifact for V2, then rerun the visual section and confirm signoff coverage is complete.`
- `Assign a recovery owner for O1, then rerun the off-happy-path section and update the blocker summary.`

## Avoid

- vague verbs like `investigate`, `review`, or `follow up` without a concrete repair target,
- multi-paragraph plans that hide the first executable step,
- actions that do not mention the blocked section or checkpoint ids,
- owner-only statements that never say what should happen next.

## Pair with

- `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_MISSING_FIELDS.md`
- `docs/WEB_QA_PLAYWRIGHT_OWNER_TRIAGE_CARD.md`
- `docs/WEB_QA_PLAYWRIGHT_RERUN_HANDOFF_CARD.md`
