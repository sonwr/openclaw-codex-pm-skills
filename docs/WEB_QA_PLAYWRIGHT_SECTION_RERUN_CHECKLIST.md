# Web QA Playwright section rerun checklist

Use this note after `report_metadata first look` identifies one blocked section (`functional`, `visual`, or `off_happy`) and you want the **smallest safe rerun loop**.

This follows the Playwright-interactive habit of keeping one lane stable at a time: verify the target, confirm the post-action state, save evidence, then decide whether to widen scope.

## 1) Freeze the rerun lane

Before acting, capture these fields from JSON:

- `report_metadata.effective_replay_readiness_hotspot_section`
- `report_metadata.effective_replay_readiness_hotspot_primary_blocker_by_section`
- `report_metadata.effective_replay_readiness_hotspot_primary_blocker_checkpoint_ids_by_section`
- `report_metadata.missing_checkpoint_evidence_dimensions_by_section`

Do not jump across sections until the current lane is stable.

## 2) Choose the smallest repair first

Apply this order every time:

1. restore missing `ref=<id>` target refs
2. restore missing artifact paths / screenshot paths
3. restore missing or non-monotonic timestamps
4. rerun only the listed hotspot checkpoints
5. update failed-check owner / next-action prose last

## 3) Per-section checklist

### `functional`

- Reconfirm the exact action target before clicking or typing.
- Verify the resulting UI state in the same checkpoint lane.
- Save one artifact path that belongs only to that checkpoint.

### `visual`

- Keep the same viewport/device assumptions for the rerun.
- Refresh screenshot evidence before discussing cosmetic regressions.
- Avoid bundling multiple visual claims into one checkpoint note.

### `off_happy`

- Recreate only the failure branch you need.
- Preserve the error proof (toast, banner, blocked CTA, log path) in the same checkpoint.
- Confirm the recovery note still references the same failed check id(s).

## 4) Stop conditions

Stop widening the rerun when any of these remain true:

- the hotspot checkpoint still lacks `ref=<id>`
- the hotspot checkpoint still lacks an artifact path
- the checkpoint order is still ambiguous
- `next_action_failed_check_refs` does not cover the failed checks you just touched

## 5) One-line operator summary

Use a copy-ready sentence like:

- `Rerun functional first: restore refs for F2/F3, refresh screenshot+trace evidence, then repeat only F2/F3 before updating owner notes.`
- `Rerun visual first: keep the same viewport, refresh V2 screenshot evidence, then re-check only V2 before widening scope.`

This keeps human and bot handoffs aligned around the same narrow rerun lane.
