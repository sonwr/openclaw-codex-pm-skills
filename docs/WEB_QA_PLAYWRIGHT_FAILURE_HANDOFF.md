# Web QA Playwright failure handoff

Use this guide when a deterministic browser QA run fails and the next owner needs a clean replay handoff.
It complements `docs/WEB_QA_PLAYWRIGHT_REPLAY_PROFILE.md` by focusing on **what to read first** in the markdown artifact and the validator JSON payload.

## Why this exists

Playwright-interactive style runs are most useful when a broken report is still actionable.
A failed run should answer four questions immediately:

1. Which checks failed?
2. What evidence is attached?
3. Who owns recovery?
4. What exact next rerun should happen?

The validator already surfaces this in `report_metadata`; this document turns that into an operator playbook.

## Fast failure triage order

### 1) Open the markdown report signoff first

Read these lines in `## 4) Signoff`:

- `Regressions:`
- `Merge recommendation:`
- `Replay readiness:`
- `Next action:`
- `Failure breakdown:` (when enabled)

This tells you whether the run is blocked, whether recovery is replay-ready, and whether the next step already points at a failed check id such as `F2` or `V1`.

### 2) Read failed checklist blocks before the execution log

For each failed check block, confirm the report includes:

- `Expected:`
- `Observed:`
- `First failure timestamp:`
- `Retry:`
- `Failure classification:`
- `Evidence:`
- `Recovery plan:`
- `Recovery owner:`

This keeps failure recovery human-readable before dropping into raw checkpoint traces.

### 3) Use validator JSON for deterministic reruns

Generate machine-readable metadata:

```bash
python3 scripts/validate_web_qa_report.py \
  --file examples/web_qa_playwright_strict_plus_with_check_refs_pass.md \
  --strict-plus \
  --require-qa-inventory-check-refs \
  --json-out artifacts/validation.json
```

For a failing run, inspect these `report_metadata` keys first:

- `failed_check_ids`
- `failed_check_classifications_by_id`
- `failed_check_recovery_owners`
- `missing_failed_check_recovery_owner_ids`
- `next_action_failed_check_refs`
- `unresolved_failed_check_ids`
- `checkpoint_target_refs_by_id`
- `checkpoint_artifact_refs_by_id`
- `qa_inventory_check_refs`

## Recommended recovery loop

### Selector issue

Signal:
- classification `selector`
- stable failure on one target ref

Next rerun:
- repair locator strategy
- preserve `ref=<id>` evidence mapping
- rerun only the affected check path first

### Runtime issue

Signal:
- classification `runtime`
- flaky waits, navigation timing, browser/runtime drift

Next rerun:
- confirm deterministic preconditions (URL, viewport, account)
- keep timestamped checkpoint order
- capture fresh trace/log artifact before broad rerun

### Product issue

Signal:
- classification `product`
- repeated failure with correct selector + stable evidence

Next rerun:
- keep the failure artifact as baseline evidence
- route the report to product/engineering owner
- rerun only after the product fix lands

## Handoff checklist for the next owner

- Confirm `Next action:` references at least one failed check id when regressions exist.
- Confirm every failed check has one evidence artifact and one recovery owner.
- Confirm checkpoint `ref=<id>` and artifact paths remain unique enough for replay.
- Confirm QA inventory mappings still cover the failing check ids.
- Prefer a narrow rerun over a full suite rerun until the invariant is repaired.

## Example: blocked handoff reading order

1. `failed_check_ids = ["F2"]`
2. `next_action_failed_check_refs = ["F2"]`
3. `failed_check_recovery_owners = {"F2": "qa-oncall@example.test"}`
4. `checkpoint_target_refs_by_id["F2"] = ["e44"]`
5. `checkpoint_artifact_refs_by_id["F2"] = ["artifacts/f2-timeout.trace"]`

That is enough to assign ownership and reproduce the failure without re-reading the whole report.

## Related docs

- `docs/WEB_QA_PLAYWRIGHT_REPLAY_PROFILE.md`
- `docs/PR_MERGE_POLICY.md`
- `examples/web_qa_playwright_strict_plus_with_check_refs_pass.md`
- `examples/web_qa_playwright_strict_fail_status_inconsistency_only.md`
