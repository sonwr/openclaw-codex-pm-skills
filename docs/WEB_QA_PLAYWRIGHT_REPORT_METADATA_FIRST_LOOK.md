# Web QA Playwright report_metadata first look

Use this note when a validator JSON artifact exists and you need the fastest safe order for deciding what to rerun next.

It is intentionally short: the goal is not to describe every key, but to help operators and bots inspect the **same fields in the same order** every time.

## First-look order

1. **Preset + top-level state**
   - `active_profile_preset`
   - `status`
   - `report_metadata.replay_readiness`

   Start here so you know which replay contract produced the artifact and whether the signoff says the run is ready or blocked.

2. **Section split before checkpoint detail**
   - `report_metadata.effective_replay_ready_sections`
   - `report_metadata.effective_replay_blocked_sections`
   - `report_metadata.effective_replay_section_status`

   This mirrors the Playwright-interactive habit of stabilizing the failing area first instead of scanning every checkpoint in one pass.

3. **Hotspot section and flattened rerun list**
   - `report_metadata.effective_replay_readiness_hotspot_section`
   - `report_metadata.effective_replay_readiness_hotspot_sections`
   - `report_metadata.effective_replay_readiness_hotspot_checkpoint_ids`
   - `report_metadata.effective_replay_readiness_hotspot_summaries`

   If you only have time for one repair lane, start with the hotspot summary and rerun the listed checkpoint ids before reading lower-priority sections.

4. **Evidence gaps before owner prose**
   - `report_metadata.missing_checkpoint_target_ref_ids`
   - `report_metadata.missing_checkpoint_artifact_ref_ids`
   - `report_metadata.missing_checkpoint_timestamp_ids`
   - `report_metadata.missing_checkpoint_evidence_dimensions_by_id`

   Follow the replay-first rule: restore stable refs, artifact paths, and chronology before polishing recovery notes.

5. **Failed-check handoff coverage**
   - `report_metadata.failed_check_ids`
   - `report_metadata.next_action_failed_check_refs`
   - `report_metadata.unresolved_failed_check_ids`
   - `report_metadata.next_action_failed_check_classifications_by_id`
   - `report_metadata.unresolved_failed_check_classifications_by_id`
   - `report_metadata.next_action_failed_check_recovery_owners`

   This tells you whether the next action already names the failed checks that need replay and who should own each branch.

## Recommended repair order

Use the same order for humans and automation:

1. confirm the replay preset and READY/BLOCKED state
2. choose the hotspot section
3. repair missing target refs / artifact refs / timestamps
4. rerun the flattened hotspot checkpoints
5. refresh failed-check owner + next-action notes only after replay evidence is stable

## Bot-friendly triage questions

- Which section is the hotspot right now?
- Are any checkpoints missing both `ref=<id>` and artifact paths?
- Are unresolved failed checks clustered in one classification (`selector`, `runtime`, `product`)?
- Does `next_action_failed_check_refs` fully cover `failed_check_ids`?

If any answer is unclear, stop and repair the evidence gap before widening the rerun scope.
