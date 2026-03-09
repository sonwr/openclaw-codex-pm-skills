# Web QA Playwright JSON handoff guide

Use this guide when a validated markdown QA report also needs a machine-readable handoff artifact for CI, reruns, or human triage.

The goal is simple:

1. validate the report with deterministic replay gates,
2. persist JSON metadata for downstream jobs,
3. route the next owner with explicit failed-check references.

This mirrors Playwright-interactive operating principles:

- **stability** — preserve the same replay metadata keys across reruns
- **reproducibility** — keep a committed command that regenerates the JSON payload
- **step-by-step verification** — inspect checkpoint/check counts instead of trusting prose
- **failure recovery** — hand off failed check ids, owners, and next actions explicitly

---

## Recommended PASS handoff command

```bash
python3 scripts/validate_web_qa_report.py \
  --file examples/web_qa_playwright_strict_plus_with_check_refs_pass.md \
  --strict-plus \
  --require-qa-inventory-check-refs \
  --require-qa-inventory-full-coverage \
  --json-out artifacts/web-qa.validation.json
```

Expected result:

- exit code `0`
- `status=PASS`
- `active_profile_preset=strict-plus`
- `qa_inventory_check_refs` includes all 10 fixed ids (`F1..F5`, `V1..V3`, `O1..O2`)

---

## Recommended FAIL handoff command

```bash
python3 scripts/validate_web_qa_report.py \
  --file examples/web_qa_playwright_strict_fail_missing_check_refs_only.md \
  --strict-plus \
  --require-qa-inventory-check-refs \
  --json-out artifacts/web-qa.fail.validation.json
```

Expected result:

- exit code `1`
- `status=FAIL`
- one isolated replay-triage error mentioning `qa inventory check refs`
- `report_metadata.qa_inventory_check_refs=[]`

This is the preferred failure-recovery pattern: isolate one broken invariant, capture it in JSON, then rerun only after that layer is fixed.

---

## JSON fields worth consuming downstream

### Top-level contract

- `status`
- `validation_schema_version`
- `active_profile_preset`
- `counts`
- `errors` / `error_count` (on FAIL)

### `report_metadata` fields for replay + handoff

- `checkpoint_order`
- `checkpoint_count`
- `checkpoint_section_counts`
- `qa_inventory_check_refs`
- `failed_check_ids`
- `unresolved_failed_check_ids`
- `failed_check_classifications_by_id`
- `failed_check_classification_counts`
- `failed_check_classification_coverage_rate`
- `failed_check_recovery_owner_coverage_rate`
- `next_action_failed_check_refs`
- `checkpoint_target_refs_by_id`
- `checkpoint_artifact_refs_by_id`
- `checkpoint_reused_target_refs`
- `checkpoint_reused_artifact_refs`
- `has_signoff_section`
- `reported_regressions`
- `merge_recommendation`
- `replay_readiness`
- `missing_signoff_fields`
- `missing_signoff_field_count`
- `signoff_field_coverage_rate`
- `has_next_action`
- `next_action_text`

---

## Suggested CI assertions

Use these as lightweight downstream checks:

```text
status == PASS
validation_schema_version == 1
active_profile_preset == strict-plus
counts.functional == 5
counts.visual == 3
counts.off_happy == 2
len(report_metadata.qa_inventory_check_refs) == 10
len(report_metadata.unresolved_failed_check_ids) == 0
```

For blocked runs, switch the assertion style:

```text
status == FAIL
error_count >= 1
len(report_metadata.failed_check_ids) >= 0
len(report_metadata.next_action_failed_check_refs) >= 0
```

The important part is not to guess. Read the emitted JSON and branch from explicit fields.

---

## Human handoff checklist

Before sending a blocked run to the next owner, confirm that the artifact answers these questions:

1. Which exact check id failed first?
2. Which replay profile produced the artifact?
3. Which checkpoint refs and artifact paths are safe to reuse?
4. Which failed-check ids are named in `Next action:`?
5. Is there any unresolved checklist-to-checkpoint drift?

If one of those answers is missing, tighten the validator flags before the next rerun.


## Coverage-rate cues

- `checkpoint_target_ref_coverage_rate` and `checkpoint_artifact_ref_coverage_rate` show how much of the 10-checkpoint execution log carries explicit replay handles.
- `checkpoint_evidence_ref_ids_by_section`, `checkpoint_evidence_ref_count_by_section`, and `checkpoint_evidence_ref_coverage_rate_by_section` show which `functional` / `visual` / `off_happy` bands already carry both stable target refs and artifact paths, so replay owners can focus repair on the weakest section first.
- `missing_checkpoint_evidence_ref_ids`, `missing_checkpoint_evidence_ref_count_by_section`, and `missing_checkpoint_evidence_ref_coverage_rate_by_section` mirror that view from the gap side, making it easier to assign replay-recovery work by section without recomputing missing evidence coverage in CI.
- Treat the by-section evidence fields as a recovery ladder: fix `functional` first when a rerun is blocked by missing target refs or shared selector drift, then close `visual`, then `off_happy`, so replay work follows the Playwright-interactive principle of step-by-step verification instead of ad-hoc screenshot backfilling.
- Reused-ref counters (`checkpoint_reused_target_ref_count_by_section`, `checkpoint_reused_artifact_ref_count_by_section`) should stay at `0`; if a single section spikes above zero, treat it as a reproducibility bug in that section rather than a report-formatting issue.
- `checkpoint_timestamp_coverage_rate` plus `missing_checkpoint_timestamp_ids` show how much of the execution log is ready for timestamp-based replay ordering without re-parsing the markdown body.
- `missing_checkpoint_timestamp_ids_by_section` groups timestamp gaps into `functional` / `visual` / `off_happy`, so replay triage can tell whether ordering evidence drift is concentrated in one checklist band before opening the markdown report.
- `checkpoint_reused_target_ref_coverage_rate` and `checkpoint_reused_artifact_ref_coverage_rate` show how much of the checkpoint set is affected by duplicate handle reuse.

## Signoff triage cues

When a report is blocked because the closing signoff is incomplete, prefer the explicit counters instead of re-parsing prose:

- `has_signoff_section` tells you whether the signoff block exists at all.
- `missing_signoff_fields` lists the exact missing closure items.
- `missing_signoff_field_count` lets CI branch on incomplete signoff without counting strings downstream.
- `signoff_field_coverage_rate` is the fast replay/readiness ratio for dashboards.
- `reported_regressions`, `merge_recommendation`, and `replay_readiness` give the structured closure state once the block is complete.
- `replay_readiness_blocker_count_by_section` and `replay_readiness_blocker_coverage_rate_by_section` show how much replay-recovery work remains per section, so CI can route follow-up without re-deriving blocker density from individual missing-ref lists.
- `has_next_action` plus `next_action_text` separate missing closure from a present-but-incomplete handoff note.

This keeps the handoff aligned with Playwright-interactive-style step verification: inspect the explicit JSON closure fields first, then reopen the markdown only when a human needs narrative context.
