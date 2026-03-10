# Web QA Playwright signoff owner sequence

Use this short sequence after strict-plus validation passes but the report still feels weak for owner handoff.

## 1. Confirm the blocked lane

Start from the hottest blocked lane, not the broadest summary.

- Read the failed-check ids named in `Next action:`.
- Confirm the lane label (`functional`, `visual`, or `off_happy`).
- Verify the lane still has current proof artifacts.

## 2. Name the owner before polishing prose

Do not polish the sentence first and guess the owner later.

Preferred owner order:

1. recovery owner already named in the artifact
2. section owner implied by the failed check scope
3. test/replay operator when the evidence gap blocks routing
4. escalation owner when the lane cannot be safely rerun

## 3. Keep the handoff sentence deterministic

A useful owner-ready signoff line usually contains four parts:

- failed lane
- failed check ids
- owner
- next proof or rerun cue

Example:

> `functional` remains blocked on `checkout-submit` / `payment-timeout`; route to QA owner with the latest trace + screenshot set and rerun the checkout lane after selector repair.

## 4. Stop if owner coverage is still ambiguous

If two owners still look equally valid, do not call the artifact handoff-ready.

Open these docs next:

- `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_GAPS.md`
- `docs/WEB_QA_PLAYWRIGHT_OWNER_TRIAGE_CARD.md`
- `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_HANDOFF.md`

## 5. Final yes/no check

Call the report owner-ready only when all of the following are true:

- the blocked lane is explicit,
- the failed check ids are explicit,
- the owner is explicit,
- the next proof or rerun cue is explicit.
