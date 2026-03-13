# openclaw-codex-pm-skills

A community-driven adaptation layer for applying PM skill frameworks (inspired by [phuryn/pm-skills](https://github.com/phuryn/pm-skills)) to **OpenClaw + Codex-style** workflows.

This project is designed for teams who want practical, reusable product-management skills that are:

- portable across environments,
- easy to audit,
- safe for collaborative use,
- and realistic to maintain in open source.

## Fast validation

Suggested PM loop: validate the repo first, update the prompt or evidence surface in a small slice, then rerun the validator before proposing handoff wording.


Use the repository smoke check before proposing README, example, or validator changes:

```bash
python3 -m unittest tests/test_validate_web_qa_report.py tests/test_validate_web_qa_report_cli.py
```

This keeps documentation tweaks and validation-rule changes tied to the same replay-readiness contract.
For broader validator or fixture rewrites, run `python3 -m unittest discover -s tests` before opening the PR so the full replay-readiness surface stays green.
If the workstream touches governance-sandbox scenario files or markdown/html report proof, use `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_PROOF_LOOP.md` before merging so scenario-input evidence and report-output evidence stay coupled.
If you need the shortest scenario-file -> JSON/Markdown/HTML replay path before the fuller proof loop, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_QUICKSTART.md` first.
If you need a compact reminder to keep one scenario import tied to one JSON/Markdown/HTML report bundle, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_STACK_NOTE.md`.
If you need a compact PM note for keeping scenario-file support and markdown/html report generation at the front of the queue, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_PRIORITY_LANE.md`.
If you need a one-screen PM reminder for the current governance-sandbox build order, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_PHASE_ONE_CHECK.md`.
If you need a compact maintainer loop for the current phase-one priority, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_PHASE_ONE_LOOP.md`.
If you need a compact PM reminder to validate the smallest repo-level slice before push, open `docs/OPENCLAW_PM_VALIDATE_THEN_PUSH_NOTE.md`.
If you need a compact PM note for keeping one small validated improvement visible across all five active repos while governance-sandbox still stays scenario-file/report-first, open `docs/GOVERNANCE_SANDBOX_FIVE_REPO_ACTIVE_SLICE_NOTE.md`.
If you need a compact PM reminder to keep every repo active in the same five-repo pass while preserving the one-line report gate, open `docs/OPENCLAW_PM_FIVE_REPO_ACTIVE_CHECK_NOTE.md`.
If you need a compact PM rule for keeping the repo order visible while each line still names the validation state and commit/push hold reason, open `docs/OPENCLAW_PM_FIVE_REPO_STATUS_LINE_ORDER_GATE.md`.
If you need a compact PM note for keeping governance-sandbox scenario-file/report-first progress paired with the same active five-repo slice, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_PROGRESS_NOTE.md`.
If you need an even shorter PM note for keeping each pass to one validated scenario/report-first slice, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_SMALL_SLICE_NOTE.md`.
If you need the matching one-line status cue for scenario-file import plus report refresh, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_SHORT_STATUS_NOTE.md`.
If you need a compact phase-one status reminder that keeps one scenario-file replay tied to one validated JSON/Markdown/HTML report bundle, open `docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_REPORT_PHASE_ONE_STATUS_NOTE.md`.

If you need a compact PM reminder to treat `report.output_label` as a stable governance-sandbox bundle-naming alias before widening web-demo scope, open `docs/GOVERNANCE_SANDBOX_REPORT_OUTPUT_LABEL_ALIAS_NOTE.md`.
If you need a compact PM reminder that repo 4 (`oss-launchpad-cli`) and repo 5 (`governance-sandbox`) stay mandatory in every five-repo slice, open `docs/GOVERNANCE_SANDBOX_FOUR_FIVE_NON_SKIP_RULE_NOTE.md`.
If you need the matching PM cue that repo 4 and repo 5 should still land one validated improvement each while repo 5 stays scenario-file/report-first, open `docs/GOVERNANCE_SANDBOX_FOUR_FIVE_VALIDATED_PROGRESS_NOTE.md`.
If you need a compact PM reminder that repo 5 still stays scenario-file/report-first even while repo 4 and repo 5 remain mandatory in each active slice, open `docs/GOVERNANCE_SANDBOX_FOUR_FIVE_PRIORITY_PAIR_NOTE.md`.
If you need a compact PM note for keeping the same five-repo loop to one short validated status line per repo, open `docs/GOVERNANCE_SANDBOX_FIVE_REPO_ONE_LINE_PROGRESS_NOTE.md`.
If you need a compact PM reminder that only fully validated repos should move to commit/push while the report still stays one line per repo, open `docs/OPENCLAW_PM_VALIDATED_COMMIT_GATE_NOTE.md`.
If you need a compact PM reminder that repos 4 and 5 are mandatory every run, open `docs/GOVERNANCE_SANDBOX_FOUR_FIVE_NON_SKIP_RULE_NOTE.md`.
If you need a compact PM reminder to keep repo 4 and repo 5 visibly active in every five-repo pass while repo 5 stays scenario/report-first, open `docs/GOVERNANCE_SANDBOX_ACTIVE_REPO_FOUR_FIVE_RULE.md`.
If you need a compact PM reminder that repo 4 and repo 5 should land together as the current phase-one pair while governance-sandbox stays scenario-file/report-first, open `docs/OPENCLAW_PM_REPO45_PHASE_ONE_PAIR_NOTE.md`.
If you need a compact PM reminder to keep repo 4 and repo 5 landing the same smallest validated progress pair before wider repo-1 handoff wording, open `docs/OPENCLAW_PM_REPO45_PROGRESS_PAIR_NOTE.md`.
If you need a compact PM reminder that repo 1 handoff wording should keep pointing at the same active scenario-file + report-bundle slice, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_ACTIVE_SLICE_NOTE.md`.
If you need a compact PM reminder to keep scenario-case wrapper growth tied to the same scenario-file -> JSON/Markdown/HTML report proof lane, open `docs/GOVERNANCE_SANDBOX_SCENARIO_CASE_WRAPPER_NOTE.md`.
If you need a compact PM note for keeping scenario-file input work explicitly ahead of preset expansion and web-demo scope, open `docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_FIRST_RULE.md`.
If you need a compact repo-1 handoff note that keeps PM wording pointed at the same scenario-file -> report-bundle proof lane, open `docs/OPENCLAW_PM_GOVERNANCE_SCENARIO_REPORT_ALIAS_NOTE.md`.
If you need a compact PM note for keeping stakeholder trait preset growth queued behind scenario-file import and markdown/html/json report proof, open `docs/GOVERNANCE_SANDBOX_TRAIT_PRESET_PHASE_NOTE.md`.
If you need the matching phase-one note that keeps scenario-file inputs, markdown/html report outputs, and preset-ready follow-up in one validated governance-sandbox slice, open `docs/GOVERNANCE_SANDBOX_TRAIT_PRESET_PHASE_ONE_NOTE.md`.
If you need a compact PM note for the first trait-preset bundle (`dao`, `delegates`, `contributors`, `investors`, `community`) while scenario/report work stays first, open `docs/GOVERNANCE_SANDBOX_TRAIT_PRESET_BUNDLE_QUEUE_NOTE.md`.
If you need a compact PM reminder to prove one scenario-storyboard wrapper with the same JSON/Markdown/HTML report bundle before widening governance-sandbox fixture scope, open `docs/GOVERNANCE_SANDBOX_SCENARIO_STORYBOARD_NOTE.md`.
If you need a compact PM note for scenario-file alias growth that keeps preset maps, trait aliases, and report outputs in the same proof lane, open `docs/GOVERNANCE_SANDBOX_SCENARIO_ALIAS_EXPANSION_LANE.md`.
If you need the matching PM note for design-studio exports that now arrive as `scenario_studio` or `scenario_studio_bundle`, open `docs/GOVERNANCE_SANDBOX_SCENARIO_STUDIO_NOTE.md`.
If you need a compact PM note for workshop exports that arrive as `scenario_workshop_bundle`, open `docs/GOVERNANCE_SANDBOX_SCENARIO_WORKSHOP_BUNDLE_NOTE.md`.
If you need the matching PM note for notebook-style exports that arrive as `scenario_notebook` or `scenario_notebook_bundle`, open `docs/GOVERNANCE_SANDBOX_SCENARIO_NOTEBOOK_WRAPPER_NOTE.md`.
If you need the matching PM note for `scenario_workbook_bundle` imports before widening fixture reuse, open `docs/GOVERNANCE_SANDBOX_SCENARIO_WORKBOOK_BUNDLE_NOTE.md`.
If you need a compact PM note for keeping `proposal_copy_markdown` in the same scenario-file/report-first proof lane, open `docs/GOVERNANCE_SANDBOX_PROPOSAL_COPY_MARKDOWN_ALIAS_NOTE.md`.
If you need a compact PM note for flat scenario fixtures that put `proposal_copy_markdown` at the top level, open `docs/GOVERNANCE_SANDBOX_TOP_LEVEL_PROPOSAL_COPY_MARKDOWN_NOTE.md`.
If you need a compact handoff for proposal-object aliases that still keeps scenario import tied to the report bundle proof, open `docs/GOVERNANCE_SANDBOX_PROPOSAL_ALIAS_HANDOFF.md`.
If you need the smallest PM-facing scenario file -> one JSON/Markdown/HTML report bundle check before widening scope, open `docs/GOVERNANCE_SANDBOX_SCENARIO_TO_REPORT_START.md`.
If you need the shortest PM note for keeping one JSON or YAML scenario input tied to one validated markdown/html/json report bundle, open `docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_REPORT_BUNDLE_START_NOTE.md`.
If you need a compact PM handoff that names the imported scenario, the report bundle basename, and the generated markdown/html/json artifacts in one place, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_BUNDLE_HANDOFF.md`.
If you need a compact reviewer-audience note that keeps one imported scenario tied to one governance report bundle, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_REVIEWERS_NOTE.md`.
If you need a compact PM cue for one scenario-file run that proves both the scenario source and the generated report directory, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_SOURCE_DIR_NOTE.md`.
If you need a compact PM reminder to keep one imported scenario file tied to one generated report-output-directory handoff, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_OUTPUT_DIRECTORY_NOTE.md`.
If you need a compact PM reminder that stdin-driven JSON/YAML replays should still report one visible JSON/Markdown/HTML bundle status line, open `docs/GOVERNANCE_SANDBOX_STDIN_REPORT_STATUS_NOTE.md`.
If you need the same proof path with a JSON fixture instead of YAML, open `docs/GOVERNANCE_SANDBOX_SCENARIO_JSON_QUICKSTART.md`.
If you need one compact PM cue for keeping JSON/YAML scenario import tied to the generated report bundle, open `docs/GOVERNANCE_SANDBOX_SCENARIO_JSON_YAML_REPORT_START.md`.
If the workstream needs reviewer-ready memo naming for governance-sandbox report bundles, open `docs/GOVERNANCE_SANDBOX_REPORT_TITLE_HANDOFF.md` before changing scenario metadata or report examples.
If you need a compact pass over whether one scenario file already produces a reusable JSON/Markdown/HTML proof bundle, open `docs/GOVERNANCE_SANDBOX_REPORT_BUNDLE_CHECK.md`.
If you need a short naming cue for keeping one scenario replay tied to one report bundle label across PM handoff copy, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_BUNDLE_LABEL_NOTE.md`.
If you need a quick wording cue for report.description-driven memo summaries across markdown/html outputs, open `docs/GOVERNANCE_SANDBOX_REPORT_SUMMARY_ALIAS_NOTE.md`.
If you need a compact PM note for carrying `report_synopsis` through the same governance-sandbox markdown/html/json memo-summary lane, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_SYNOPSIS_ALIAS_NOTE.md`.
If you need a compact PM note for keeping multiline proposal copy and decision memos readable in generated HTML reports, open `docs/GOVERNANCE_SANDBOX_HTML_MULTILINE_REPORT_NOTE.md`.
If you need a compact note for carrying `report.synopsis` into the same markdown/html/json memo summary lane, open `docs/GOVERNANCE_SANDBOX_REPORT_SYNOPSIS_ALIAS_NOTE.md`.
If you need a compact PM note for carrying `report.description` from one imported scenario file into the generated markdown/html memo bundle, open `docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_REPORT_DESCRIPTION_NOTE.md`.
If you need a compact PM cue for keeping one imported scenario file tied to visible report owner and report summary metadata before broader governance routing, open `docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_REPORT_OWNER_SUMMARY_NOTE.md`.
If you need the matching one-line maintainer update once that owner+summary pair is visible in the generated bundle, open `docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_REPORT_OWNER_SUMMARY_STATUS_LINE.md`.
If you need a compact PM cue for keeping one scenario file tied to a named markdown/html/json memo bundle with visible output paths, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_ARTIFACT_NOTE.md`.
If you need a compact PM review note for replaying one imported scenario file against one generated JSON/Markdown/HTML bundle, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_OUTPUT_REVIEW.md`.
If you need a compact PM recheck before handoff, open `docs/GOVERNANCE_SANDBOX_REPORT_BUNDLE_RECHECK_NOTE.md` to confirm one imported scenario still regenerates the same JSON/Markdown/HTML bundle before push.
If you need a quick note for title-derived report bundle naming when no explicit basename is set, open `docs/GOVERNANCE_SANDBOX_REPORT_BASENAME_TITLE_FALLBACK.md`.
If you need a compact note for keeping governance-sandbox artifact paths visible in report metadata, open `docs/GOVERNANCE_SANDBOX_REPORT_ARTIFACT_PATHS.md`.
If you need the shortest pipe-friendly scenario replay for governance-sandbox JSON/YAML input, open `docs/GOVERNANCE_SANDBOX_STDIN_SCENARIO_NOTE.md`.
If you need a one-line reviewer cue that keeps report subject, owner, queue, and bundle status aligned in the same saved summary handoff, open `docs/CLI_SUMMARY_REPORT_SUBJECT_OWNER_QUEUE_STATUS_NOTE.md`.
If you need the matching path-aware handoff once that same summary also needs the saved artifact location, open `docs/CLI_SUMMARY_REPORT_STATUS_OWNER_QUEUE_PATH_NOTE.md`.
If you need the same stdin path with a default report bundle handoff, open `docs/GOVERNANCE_SANDBOX_STDIN_REPORT_BUNDLE_NOTE.md`.
If you need a quick wording cue for report.description-driven memo summaries across markdown/html outputs, open `docs/GOVERNANCE_SANDBOX_REPORT_SUMMARY_ALIAS_NOTE.md`.
If you need a compact PM note for carrying `report_synopsis` through the same governance-sandbox markdown/html/json memo-summary lane, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_SYNOPSIS_ALIAS_NOTE.md`.
If you need a short note for driving the default report bundle basename from `report.name`, open `docs/GOVERNANCE_SANDBOX_REPORT_NAME_ALIAS_NOTE.md`.
If you need a short note for driving the same governance-sandbox report bundle from `report.output_slug` or `report.outputs.output_slug`, open `docs/GOVERNANCE_SANDBOX_REPORT_OUTPUT_SLUG_ALIAS_NOTE.md`.
If you need a quick note for `report.output_name` or top-level `report_name` bundle naming, open `docs/GOVERNANCE_SANDBOX_REPORT_OUTPUT_NAME_ALIAS_NOTE.md`.
If you need a one-screen replay check for scenario file + basename + artifact-path visibility together, open `docs/GOVERNANCE_SANDBOX_REPORT_METADATA_CARD.md`.
If you need the shortest PM handoff note before replaying those same governance-sandbox metadata artifacts, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_METADATA_START_NOTE.md`.
If you need the shortest PM handoff for scenario input and reviewer-visible report output together, open `docs/GOVERNANCE_SANDBOX_REPORT_RESULT_CARD_START_NOTE.md`.
If you need an even smaller PM-facing start for one scenario file plus one generated report bundle, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_START_NOTE.md`.
If you need a compact replay gate for confirming the same scenario file still owns the generated JSON/Markdown/HTML trio before handoff, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_REPLAY_GATE.md`.
If you need a compact owner-facing sentence once one scenario replay already produced a shared JSON/Markdown/HTML bundle, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_OWNER_HANDOFF_NOTE.md`.
If you need the shortest owner-first replay for one imported scenario plus one JSON/Markdown/HTML report bundle, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_OWNER_START.md`.
If you need a compact reviewer-ready follow-up that keeps scenario source, owner/audience routing, and the generated JSON/Markdown/HTML bundle in one handoff lane, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_OWNER_AUDIENCE_REVIEW_LOOP.md`.
If you need a compact PM note for keeping the reviewer list visible in the same governance-sandbox report bundle, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_REVIEWER_LIST_NOTE.md`.
If you need a compact rule for checking that scenario metadata and report artifact links stay readable together, open `docs/GOVERNANCE_SANDBOX_REPORT_METADATA_READABILITY_NOTE.md`.
If you need a short maintainer cue for the new governance-sandbox report owner aliases before wider handoff wording, open `docs/GOVERNANCE_SANDBOX_REPORT_OWNER_ALIAS_NOTE.md`.
If you need a compact PM note for keeping scenario source, report basename, and report owner visible in one governance-sandbox handoff, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_OWNER_BASENAME_NOTE.md`.
If you need a compact PM cue for keeping one validated governance-sandbox replay tied to the exact scenario fixture path, bundle basename, and report trio before widening the pass, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_FIXTURE_PROOF_NOTE.md`.
If you need a short PM alias note for carrying `scenario_source` / `source_path` metadata through stdin-driven governance-sandbox markdown/html report bundles, open `docs/GOVERNANCE_SANDBOX_SCENARIO_SOURCE_ALIAS_NOTE.md`.
If you need a compact PM note for the shorter `report.bundle_stem` alias before widening governance-sandbox report naming rules, open `docs/GOVERNANCE_SANDBOX_REPORT_BUNDLE_STEM_ALIAS_NOTE.md`.
If you need a compact rule for when nested source aliases should yield to the real scenario-file path, open `docs/GOVERNANCE_SANDBOX_SCENARIO_SOURCE_PRECEDENCE_NOTE.md`.
If you need a short reviewer cue for one DAO-flavored scenario example that already proves scenario-file input plus named JSON/Markdown/HTML output, open `docs/GOVERNANCE_SANDBOX_DAO_REPORT_EXAMPLE_NOTE.md`.
If you need a quick reminder to verify preset coverage before wiring a scenario file or web demo, open `docs/GOVERNANCE_SANDBOX_LIST_PRESETS_NOTE.md`.
If you need a compact example scenario that proves preset-driven stakeholders plus a report bundle in one replay, open `docs/GOVERNANCE_SANDBOX_PRESET_BUNDLE_EXAMPLE_NOTE.md`.
If you need a machine-readable preset catalog handoff for CLI, browser-form, or demo wiring, open `docs/GOVERNANCE_SANDBOX_PRESET_JSON_HANDOFF.md`.
If you need the shortest preset-catalog cue before wiring one result card or browser form, open `docs/GOVERNANCE_SANDBOX_PRESET_JSON_RESULT_CARD_NOTE.md`.
If you need a compact PM note for keeping preset-driven result-card work behind the same scenario-file -> report-bundle phase order, open `docs/GOVERNANCE_SANDBOX_PRESET_RESULT_CARD_PHASE_NOTE.md`.
If you need the matching PM note for download-oriented report bundle paths before widening that first result-card flow, open `docs/GOVERNANCE_SANDBOX_REPORT_DOWNLOADS_ALIAS_PM_NOTE.md`.
If you need a compact PM-facing start note for wiring `run --list-presets-json` into the first scenario form before wider web-demo work, open `docs/GOVERNANCE_SANDBOX_PRESET_JSON_FORM_START_NOTE.md`.
If you need a compact scenario-authoring cue for `trait` / `persona` preset aliases before widening report or web-demo work, open `docs/GOVERNANCE_SANDBOX_SCENARIO_TRAIT_ALIAS_NOTE.md`.
If you need the shortest PM-facing note for scenario-file input plus the default markdown/html/json report trio before broader demo work, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_MINIMUM_BUNDLE_NOTE.md`.
If you need a compact note for keeping the first governance-sandbox web demo recovery loop aligned with Playwright-interactive replay rules, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_PLAYWRIGHT_RECOVERY_NOTE.md`.
If you need the shortest PM-facing note for keeping scenario source plus the default report trio in one replay line, open `docs/GOVERNANCE_SANDBOX_SCENARIO_SOURCE_TRIO_NOTE.md`.
If you need the shortest reminder that `scenario_config` is also accepted as a scenario-file wrapper before widening import docs, open `docs/GOVERNANCE_SANDBOX_SCENARIO_CONFIG_WRAPPER_NOTE.md`.
If you need a shorter PM-facing cue for proving scenario-file input plus one markdown memo before widening the full report trio, open `docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_MARKDOWN_NOTE.md`.
If you need a compact PM note for keeping one imported scenario file tied to one generated JSON/Markdown/HTML bundle with replayable verification steps, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_VERIFICATION_LANE.md`.
If you need the shortest PM cue for the new `scenario_demo` wrapper before the broader demo-pack lane, open `docs/GOVERNANCE_SANDBOX_SCENARIO_DEMO_WRAPPER_NOTE.md`.
If you need a compact PM note for the more explicit `report.outputs.bundle_basename` alias before widening governance-sandbox naming rules, open `docs/GOVERNANCE_SANDBOX_REPORT_BUNDLE_BASENAME_ALIAS_NOTE.md`.
If you need a compact pre-merge check that the smallest acceptable governance-sandbox progress still means scenario import plus one validated report artifact, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_MIN_PROGRESS_CHECK.md`.
If you need one compact note for keeping scenario-file import, markdown/html report outputs, and report-priority wording aligned in the same smallest validated governance-sandbox slice, open `docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_REPORT_PRIORITY_STACK_NOTE.md`.
If you need a shorter proof card for the minimum acceptable scenario-file + JSON/Markdown/HTML bundle slice before widening scope, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_MINIMUM_PROGRESS_CARD.md`.
If you need a shortest-path PM reminder for one scenario file feeding one JSON/Markdown/HTML report bundle, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_ENTRY_NOTE.md`.

If you need a compact PM cue for the current governance-sandbox build order (scenario file -> report bundle -> presets -> web demo -> demo GIF), open `docs/GOVERNANCE_SANDBOX_DELIVERY_LADDER_NOTE.md`.
If you need a one-line PM status cue for keeping that delivery ladder visible during small validated slices, open `docs/GOVERNANCE_SANDBOX_DELIVERY_LADDER_STATUS_NOTE.md`.
If you need a compact PM reminder to keep repo 5 on scenario-file + markdown/html report proof while repo 4 stays visibly active in the same pass, open `docs/GOVERNANCE_SANDBOX_FOUR_FIVE_PHASE_ONE_BRIDGE_NOTE.md`.
If you need a compact PM rule for the required five-line short report across the active repos, open `docs/GOVERNANCE_SANDBOX_FIVE_REPO_SHORT_REPORT_RULE.md`.
If you need a shorter PM reminder for one-line repo status updates that still name change state, validation, and commit/push gate together, open `docs/OPENCLAW_PM_FIVE_REPO_SHORT_LINE_GATE_NOTE.md`.
If you need the matching PM cue that the exact same five-line pass should name commit/push hold reasons only after validation reruns, open `docs/OPENCLAW_PM_FIVE_REPO_VALIDATE_THEN_HOLD_REASON_NOTE.md`.
If you need a compact PM reminder to validate one small evidence-backed improvement in repo 1 before widening the five-repo pass, open `docs/OPENCLAW_PM_SMALL_VALIDATED_SLICE_NOTE.md`.
If you need a compact PM reminder to keep repos 4 and 5 moving through one small validated slice each before widening the pass, open `docs/OPENCLAW_PM_REPO45_SMALL_VALIDATED_SLICE_NOTE.md`.
If you need a compact PM reminder to recheck the active repos in the same visible order before writing the five-line report, open `docs/OPENCLAW_PM_FIVE_REPO_RECHECK_ORDER_NOTE.md`.
If you need a compact PM note for keeping that same recheck loop tied to repos 4 and 5 plus the validate-before-push gate, open `docs/OPENCLAW_PM_FIVE_REPO_RECHECK_VALIDATE_NOTE.md`.
If you need a compact PM cue for the five-repo short report while governance-sandbox still stays scenario-file/report-first, open `docs/OPENCLAW_PM_FIVE_REPO_PHASE_ONE_STATUS_LINE_NOTE.md`.
If you need a compact PM note for keeping repo order plus explicit hold reasons in that same five-repo status line, open `docs/OPENCLAW_PM_FIVE_REPO_STATUS_HOLD_ORDER_NOTE.md`.
If you need a compact PM reminder for the same five-repo loop to stay small, validated, and non-skipping across repos 4 and 5, open `docs/OPENCLAW_PM_FIVE_REPO_VALIDATE_LOOP_NOTE.md`.

If you need a compact PM note for keeping scenario-file input and markdown/html report output paired as the first delivery slice, open `docs/GOVERNANCE_SANDBOX_PRIORITY_PAIR_NOTE.md`.
If you need the matching one-line PM status cue for that same paired phase-one slice, open `docs/GOVERNANCE_SANDBOX_PRIORITY_PAIR_STATUS_NOTE.md`.
If you need the matching PM note for keeping that same phase-one pair visible in the scenario-file/report-first queue, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_PRIORITY_PAIR_NOTE.md`.
If you need a compact PM reminder for the current phase-one target (scenario file first, report bundle second), open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_PHASE_ONE_NOTE.md`.
If you need a compact PM checklist for the current governance-sandbox build order before widening scope, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_PHASE_ONE_CHECK.md`.
If you need a compact PM queueing note for keeping one scenario import and one markdown/html/json report bundle visible before broader review routing, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_QUEUE_NOTE.md`.
If you need a compact PM queue note for one scenario file plus one regenerated JSON/Markdown/HTML report bundle, open `docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_REPORT_QUEUE_NOTE.md`.
If you need a compact PM note for proving one scenario-file wrapper alias before widening preset or web-demo scope, open `docs/GOVERNANCE_SANDBOX_SCENARIO_WRAPPER_ENTRY_NOTE.md`.
If you need a compact PM note for workshop fixtures that arrive as `scenario_manifest_bundle` or `scenario_packet_bundle`, open `docs/GOVERNANCE_SANDBOX_SCENARIO_MANIFEST_BUNDLE_NOTE.md`.
If you need a compact PM note for imported fixtures wrapped as `scenario_demo_bundle`, open `docs/GOVERNANCE_SANDBOX_SCENARIO_DEMO_BUNDLE_NOTE.md`.
If you need the matching PM note for workshop fixtures that arrive as `scenario_session_bundle`, open `docs/GOVERNANCE_SANDBOX_SCENARIO_SESSION_BUNDLE_NOTE.md`.
If you need a compact PM note for `stakeholder_list` or `stakeholder_entries` scenario-file aliases before widening preset or web-demo scope, open `docs/GOVERNANCE_SANDBOX_STAKEHOLDER_LIST_ALIAS_NOTE.md`.
If you need a compact PM note for `scenario_record` archive-style wrappers before widening preset or web-demo scope, open `docs/GOVERNANCE_SANDBOX_SCENARIO_RECORD_WRAPPER_NOTE.md`.
If you need a compact PM status cue for the current smallest acceptable win in governance-sandbox, open `docs/GOVERNANCE_SANDBOX_MINIMUM_WIN_STATUS_NOTE.md`.
If you need a compact PM note for shipping one small governance-sandbox improvement while keeping scenario import and report bundle proof coupled, open `docs/GOVERNANCE_SANDBOX_SMALL_SLICE_RULE.md`.
If you need a compact PM note for proving one scenario source path and one report bundle basename together before a handoff, open `docs/GOVERNANCE_SANDBOX_SCENARIO_SOURCE_BASENAME_NOTE.md`.
If you need a short note for keeping one imported scenario file tied to one regenerated JSON/Markdown/HTML report stack, open `docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_REPORT_STACK_NOTE.md`.
If you need a compact PM rule for proving scenario-file aliases and markdown/html/json report artifacts in one reviewer-facing pass, open `docs/GOVERNANCE_SANDBOX_SCENARIO_ARTIFACT_PROOF_RULE.md`.
If you need a compact PM-facing status cue for one imported scenario file plus one generated JSON/Markdown/HTML report bundle, open `docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_REPORT_STATUS_NOTE.md`.
If you need a shorter PM note for keeping scenario import, regenerated report artifacts, and owner/reviewer handoff in one two-step slice, open `docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_REPORT_TWO_STEP_NOTE.md`.
If you need a shorter PM reminder that scenario-file input and markdown/html report output stay first in that order, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_PRIORITY_NOTE.md`.
If you need a compact PM note for keeping scenario-file import, markdown/html/json report proof, and the next smallest validated step in the same handoff, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_NEXT_SLICE_NOTE.md`.
If you need a compact PM cue for naming the scenario source, report basename, and generated artifact trio in one reviewer-facing line, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_STATUS_TRIO_NOTE.md`.
If you need a shortest-path PM reminder that scenario-file alias work still starts with one imported fixture plus one JSON/Markdown/HTML report bundle, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_ALIAS_START_NOTE.md`.
If you need a compact PM note for keeping one imported fixture tied to one regenerated JSON/Markdown/HTML report bundle, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPLAY_BUNDLE_NOTE.md`.

If you need a compact reminder to keep the first governance-sandbox web-demo form aligned with the exported preset catalog before widening scope, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_PRESET_FORM_NOTE.md`.
If you need a compact PM note for keeping one scenario-file replay tied to one generated markdown/html report artifact bundle, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_ARTIFACT_NOTE.md`.
If you need a compact PM cue for scenario files that package the proposal itself as a structured object before markdown/html report generation, open `docs/GOVERNANCE_SANDBOX_PROPOSAL_OBJECT_NOTE.md`.
If you need a compact PM note for keeping the next alias addition tied to the same scenario-file plus JSON/Markdown/HTML report bundle proof, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_ALIAS_QUEUE_NOTE.md`.
If you want the shortest replay note before wiring that preset JSON into a scenario form or review bot, open `docs/GOVERNANCE_SANDBOX_PRESET_JSON_START_NOTE.md`.
If you need the matching note for string-form stakeholder presets, open `docs/GOVERNANCE_SANDBOX_STRING_PRESET_NOTE.md`.
If you need a compact note for carrying report audience metadata from scenario files into markdown/html outputs, open `docs/GOVERNANCE_SANDBOX_REPORT_AUDIENCE_NOTE.md`.
If you need a short PM-facing cue for keeping preset labels paired with stakeholder concern summaries in governance-sandbox reports, open `docs/GOVERNANCE_SANDBOX_PRESET_SUMMARY_REPORT_NOTE.md`.
If you need the fastest scenario-file -> rendered-audience proof before wider report work, open `docs/GOVERNANCE_SANDBOX_REPORT_AUDIENCE_START_NOTE.md`.
If you need a short alias rule for keeping `report.audience`, `report_readers`, and top-level audience fields aligned in one replayable fixture, open `docs/GOVERNANCE_SANDBOX_REPORT_AUDIENCE_ALIAS_NOTE.md`.
If you need a compact PM-facing note for keeping report owner and audience metadata visible together in one governance-sandbox replay bundle, open `docs/GOVERNANCE_SANDBOX_REPORT_OWNER_AUDIENCE_NOTE.md`.
If you need a short alias note for nested `report.report_readers` audience metadata in governance-sandbox scenario files, open `docs/GOVERNANCE_SANDBOX_REPORT_READERS_ALIAS_NOTE.md`.
If you need a compact browser-proof recovery note for a flaky governance-sandbox web demo checkpoint, open `docs/GOVERNANCE_SANDBOX_PLAYWRIGHT_RECOVERY_NOTE.md`.
If you want the shortest bridge that keeps the first governance-sandbox web-demo form aligned with both UI/UX review rules and Playwright replay rules, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_UI_UX_PLAYWRIGHT_BRIDGE.md`.
If you need a short PM-facing cue for pairing stable browser-proof checkpoints with the same scenario/report artifacts, open `docs/GOVERNANCE_SANDBOX_PLAYWRIGHT_ARTIFACT_STABILITY_NOTE.md`.
If you need a compact matrix for checking which governance-sandbox report artifacts should be present after a scenario replay, open `docs/GOVERNANCE_SANDBOX_REPORT_OUTPUT_MATRIX.md`.
If you need a short PM note for scenario/report fixtures that describe the bundle directory as `report_dir`, `reports_dir`, `report_folder`, or `reports_folder`, open `docs/GOVERNANCE_SANDBOX_REPORT_OUTPUT_DIRECTORY_ALIASES_NOTE.md`.
If you need a compact PM note for keeping JSON/Markdown/HTML paths grouped under one `report.outputs.files` block, open `docs/GOVERNANCE_SANDBOX_REPORT_OUTPUT_FILES_NOTE.md`.
If you need a tiny reviewer-facing reminder that the same scenario replay still owns one visible JSON/Markdown/HTML artifact trio, open `docs/GOVERNANCE_SANDBOX_REPORT_OUTPUT_FILES_CARD.md`.
If you need a quick alias note for driving governance-sandbox report bundle filenames from `report.file_stem`, open `docs/GOVERNANCE_SANDBOX_REPORT_FILE_STEM_ALIAS_NOTE.md`.
If you need a compact alias note for driving that same governance-sandbox report bundle from `report.slug`, open `docs/GOVERNANCE_SANDBOX_REPORT_SLUG_ALIAS_NOTE.md`.
If you need a short note for when one `--report-dir` run should keep named artifacts plus default `report.*` aliases together, open `docs/GOVERNANCE_SANDBOX_REPORT_DIR_ALIAS_NOTE.md`.
If you need a compact PM note for the shorter top-level `report_folder` alias, open `docs/GOVERNANCE_SANDBOX_REPORT_FOLDER_ALIAS_NOTE.md`.
If you need a compact UI review loop for the first governance-sandbox web demo slice, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_UI_REVIEW.md`.
If you want the shortest bridge between governance-sandbox web-demo work and UI/UX review rules, open `docs/GOVERNANCE_SANDBOX_UI_UX_PRO_MAX_BRIDGE.md`.
If you need a metadata-first reopen note after one scenario-file + report-bundle run, open `docs/GOVERNANCE_SANDBOX_REPORT_METADATA_HANDOFF.md`.
If you need a short step ladder for stabilizing browser-demo checkpoints before widening coverage, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_PLAYWRIGHT_LADDER.md`.
If you need a one-line PM check for whether a scenario-file run already produced the minimum report trio, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_STACK_NOTE.md`.
If you need a compact rule for keeping the first governance-sandbox browser proof limited to one scenario form, one result card, and one report-download check, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_CHECKPOINT_RULE.md`.
If you need a short step-by-step checkpoint list before widening that first web demo slice, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_STEP_CHECKLIST.md`.
If you need a compact PM-facing reminder to keep that first governance-sandbox web demo limited to one scenario form, one result card, and one report-download checkpoint, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_UI_SCOPE_BRIEF.md`.
If you need a compact acceptance note for when that first governance-sandbox result card is actually reviewable, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_ACCEPTANCE.md`.
If you need a compact reminder to keep that first result card tied to one believable report-download proof, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_REPORT_DOWNLOAD_NOTE.md`.
If you need a smaller scope note for keeping that same browser slice limited to one form, one result card, and one report download, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_DOWNLOAD_SCOPE_NOTE.md`.

If you need a quick proof loop for scenario alias imports before report handoff, open `docs/GOVERNANCE_SANDBOX_SCENARIO_ALIAS_CHECKLIST.md`.
If you need a compact note for keeping scenario display-name aliases (`name` / `title` / `scenario_name`) aligned with the final report heading, open `docs/GOVERNANCE_SANDBOX_SCENARIO_TITLE_ALIAS_NOTE.md`.
If you need a compact PM note for governance-sandbox scenario files that keep report subject, owner, and audience visible together, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_TRIAGE_NOTE.md`.
If you need the shortest replay start for one scenario file plus one generated bundle that keeps both report owner and audience visible, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_OWNER_AUDIENCE_START_NOTE.md`.
If you need a compact signoff note that keeps Web QA validator PASS coupled to scenario-report freshness, open `docs/WEB_QA_PLAYWRIGHT_SCENARIO_REPORT_SIGNOFF.md`.
If you need a short PM-facing reminder to keep governance-sandbox progress locked to one real scenario file and one report bundle before widening scope, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_PROGRESS_NOTE.md`.
If the workstream is about governance-sandbox web UI proof, use `docs/GOVERNANCE_SANDBOX_WEB_DEMO_PROOF_LOOP.md` so UI work stays anchored to scenario input, report output, and deterministic browser-proof checkpoints.
If you need a compact pass/hold cue before calling that web-demo slice complete, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_SCOPE_CHECK.md`.
If you need a short checklist for proving the scenario form, result card, and report download in one stability-first pass, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_STEP_CHECKLIST.md`.
If you want a short scenario-file-first checklist for governance-sandbox report bundles before wider web-demo work, open `docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_CHECKLIST.md`.
If you need a compact note for scenario files that also carry report output paths, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_PATH_ALIAS_NOTE.md`.
If you need a compact PM note for scenario files wrapped under `scenario_payload`, `scenario_data`, or `scenario_bundle`, open `docs/GOVERNANCE_SANDBOX_SCENARIO_WRAPPER_ALIAS_NOTE.md`.
If you need a compact PM cue for wrapping imported proposal/stakeholder payloads under `scenario_input`, `scenario_document`, or `scenario_manifest`, open `docs/GOVERNANCE_SANDBOX_SCENARIO_INPUT_WRAPPER_NOTE.md`.
If you need the matching PM note for `scenario_package` wrappers before widening scenario-fixture reuse, open `docs/GOVERNANCE_SANDBOX_SCENARIO_PACKAGE_WRAPPER_NOTE.md`.
If you need the matching PM note for a plain top-level `scenario` wrapper before widening fixture reuse, open `docs/GOVERNANCE_SANDBOX_SCENARIO_TOP_LEVEL_WRAPPER_NOTE.md`.
If you need the matching PM note for `scenario_plan` wrappers before widening fixture reuse, open `docs/GOVERNANCE_SANDBOX_SCENARIO_PLAN_WRAPPER_NOTE.md`.
If you need a compact PM cue for wrapping imported proposal/stakeholder payloads under `scenario_input`, `scenario_document`, or `scenario_manifest`, open `docs/GOVERNANCE_SANDBOX_SCENARIO_INPUT_WRAPPER_NOTE.md`.
If you need the matching PM note for `scenario_package` wrappers before widening scenario-fixture reuse, open `docs/GOVERNANCE_SANDBOX_SCENARIO_PACKAGE_WRAPPER_NOTE.md`.
If you need the matching cue for a plural `scenario_inputs` wrapper before wider scenario-fixture reuse, open `docs/GOVERNANCE_SANDBOX_SCENARIO_INPUTS_ALIAS_NOTE.md`.
If you need a short PM-facing cue for compact scenario fixtures that keep stakeholder names mapped directly to presets, open `docs/GOVERNANCE_SANDBOX_PRESET_MAP_ALIAS_NOTE.md`.
If you need the shortest reminder for compact report path fields like `report.md_file` and `report.html_output`, open `docs/GOVERNANCE_SANDBOX_REPORT_PATH_SHORT_ALIASES_NOTE.md`.
If you need the shortest PM note for root-level `report_json_output` + `report_md_output` + `report_html_output` aliases before widening the scenario schema, open `docs/GOVERNANCE_SANDBOX_ROOT_REPORT_OUTPUT_ALIASES_NOTE.md`.
If you need a compact note for keeping `report_tags` compact as one comma-separated or newline-separated string in governance-sandbox fixtures, open `docs/GOVERNANCE_SANDBOX_REPORT_TAG_STRING_NOTE.md`.
If you need a compact reminder that relative CLI report paths should resolve from the scenario-file directory, open `docs/GOVERNANCE_SANDBOX_RELATIVE_REPORT_PATHS_NOTE.md`.
If you need a compact note for authoring stakeholder presets with a YAML/JSON name-to-preset map, open `docs/GOVERNANCE_SANDBOX_SCENARIO_MAP_INPUT_NOTE.md`.
If you need a compact note for the top-level `report_output_directory` alias before widening scenario-to-report wiring, open `docs/GOVERNANCE_SANDBOX_REPORT_OUTPUT_DIRECTORY_ALIAS_NOTE.md`.
If you need a compact note for nested `report.outputs.report_output_directory` / `report.outputs.report_output_dir` aliases before widening scenario-to-report wiring, open `docs/GOVERNANCE_SANDBOX_REPORT_OUTPUT_DIRECTORY_ALIASES_NOTE.md`.
If you need a compact note for keeping `report.outputs.json` / `markdown` / `html` aliases together in one scenario fixture, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_OUTPUTS_ALIAS_NOTE.md`.
If you need the shortest note for nested `scenario.inputs` fixtures before widening governance-sandbox scenario replay coverage, open `docs/GOVERNANCE_SANDBOX_NESTED_SCENARIO_INPUTS_NOTE.md`.
If you need a compact reminder that nested scenario fixtures can also keep report metadata under `inputs.report`, open `docs/GOVERNANCE_SANDBOX_SCENARIO_INPUTS_REPORT_NOTE.md`.
If you need a short PM-facing note for bundle naming driven from `inputs.report.outputs.basename`, open `docs/GOVERNANCE_SANDBOX_INPUTS_REPORT_OUTPUTS_BASENAME_NOTE.md`.
If you need a compact entry bar before expanding the governance-sandbox web demo beyond the first form and result-card slice, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_ENTRY_CHECK.md`.
If you need a compact proof cue for scenario preset aliasing (`preset`/`group`/`trait`/`persona`) plus report summary aliases (`summary`/`brief`/`report_summary`), open `docs/GOVERNANCE_SANDBOX_SCENARIO_ALIAS_PROOF.md`.
If you need a shorter alias-expansion check before widening the governance-sandbox proof loop, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_ALIAS_EXPANSION.md`.
If the web-demo slice specifically changes the scenario form, result cards, or report download proof, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_FORM_PROOF.md`.
If you need a compact check that the first governance-sandbox web demo still makes report download proof visible from the result card, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_RESULT_DOWNLOAD_CHECK.md`.
If you need a PM-facing note for keeping scenario replay, result-card proof, and report-bundle download proof coupled in one slice, open `docs/GOVERNANCE_SANDBOX_REPORT_DOWNLOAD_PROOF_NOTE.md`.
If you need the shortest scenario-file -> result card -> report-download proof path before a wider browser pass, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_RESULT_CARD_DOWNLOAD_START.md`.
If you need a compact reminder to keep that first web-demo slice in a stability-first lane before widening scope, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_STABILITY_LANE.md`.
If you need a compact recovery-first checklist after one web-demo checkpoint regresses, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_RECOVERY_PROOF.md`.
If you need a one-line PM-facing status once that first result-card proof is believable, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_STATUS_LINE_NOTE.md`.
If you need a compact Playwright signoff note before widening that same form-to-card slice, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_PLAYWRIGHT_SIGNOFF_NOTE.md`.
If you need one bridge note that keeps ui-ux-pro-max layout rules and Playwright stability checks coupled for the first governance-sandbox web demo slice, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_UI_UX_PLAYWRIGHT_HANDOFF.md`.
If you need the narrowest web-demo proof that keeps one stable form submit, one result card, and one replay-ready handoff together, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_RESULT_CARD_REPLAY_STACK.md`.
If you need the same bridge condensed into one form-to-card acceptance lane, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_FORM_TO_CARD_ACCEPTANCE.md`.
If you need a one-screen audit before widening that same form-to-card slice, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_RESULT_CARD_AUDIT.md`.
If you want a shorter result-card-only audit before widening the first governance-sandbox web demo, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_RESULT_CARD_AUDIT.md`.
If you need a compact PM note that keeps governance-sandbox work pinned to scenario-file import plus report-bundle proof before wider preset or UI expansion, open `docs/GOVERNANCE_SANDBOX_REPORT_PRIORITY_BUNDLE_NOTE.md`.
If the scenario import workstream adds another stakeholder preset alias (`role` / `persona` / `group`), open `docs/GOVERNANCE_SANDBOX_SCENARIO_ALIAS_ROLE_NOTE.md` so alias-proof scope stays tied to the same report-ready replay flow.
If you need a compact handoff for keeping proposal + stakeholder scenario files aligned with the first preset-backed report bundle, open `docs/GOVERNANCE_SANDBOX_SCENARIO_PRESET_PACK.md`.
If you need a compact note for mapping-style fixtures that keep stable ids outside but human names inside `stakeholder`, open `docs/GOVERNANCE_SANDBOX_SCENARIO_STAKEHOLDER_ALIAS_NOTE.md`.
The JSON metadata also tracks failed-check recovery owners, missing owner coverage, and next-action owner handoff readiness so triage gaps stay visible before merge.
If the validator passes with incomplete signoff coverage, use `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_MISSING_FIELDS.md` to decide whether the artifact is inspection-ready or truly handoff-ready.
If owner coverage is the real blocker after validation passes, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_GAPS.md` before calling the report handoff-ready.
If you need a compact wording note for validator-PASS artifacts that are still not governance-ready, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_GOVERNANCE_NOTE.md`.
If you need a fast last-pass gate for whether unresolved failed checks still block owner-complete handoff, open `docs/WEB_QA_PLAYWRIGHT_OWNER_GAP_EXIT_CHECK.md`.
If you need a compact owner handoff sentence after validation passes, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_HANDOFF.md`.
If you need a 30-second owner/lane/artifact context check before posting that sentence, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_CONTEXT_CHECK.md`.
If you need a 30-second owner-ready signoff brief before that fuller handoff, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_READY_BRIEF.md`.
If you need a compact reminder to keep that owner-ready handoff lane-scoped, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_READY_SCOPE_NOTE.md`.
If you need an even shorter owner-aware signoff sentence that keeps covered versus unresolved failed checks visible, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_SUMMARY_LINE.md`.
If you need a one-line owner summary before writing the fuller handoff, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_SUMMARY_LINE.md` first and expand only if unresolved checks remain.
If you need a faster owner-first cue before writing that sentence, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_CUE.md`.
If you need a compact owner-alias-safe handoff sentence that still keeps unresolved failed checks visible, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_ALIAS_TRIAGE.md`.
If you need a compact signoff-coverage decision card before handoff, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_COVERAGE_CARD.md`.
If you need a 60-second signoff-first scan before a deeper review, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_FIRST_LOOK.md`.
If you need a 60-second replay-readiness review before rerun or handoff, open `docs/WEB_QA_PLAYWRIGHT_REPLAY_READINESS_QUICKCHECK.md`.
If you need a compact reminder to keep scenario fixtures, browser targets, and saved report artifacts stable across reruns, open `docs/WEB_QA_PLAYWRIGHT_REPLAY_INPUT_STABILITY.md`.
If you need a compact bridge for keeping failed checks, stable target refs, and saved artifacts visible on one recovery card before a rerun, open `docs/WEB_QA_PLAYWRIGHT_RESULT_CARD_RECOVERY_BRIDGE.md`.
If hotspot sections tie on replay blockers, open `docs/WEB_QA_PLAYWRIGHT_REPLAY_HOTSPOT_TIEBREAK.md` before flattening the repair lane into a single winner.
If you need a quick rule card for interpreting replay blocker totals before handoff, open `docs/WEB_QA_PLAYWRIGHT_REPLAY_BLOCKER_TOTALS.md`.
If you need a compact owner-routing checklist before handoff, open `docs/WEB_QA_PLAYWRIGHT_OWNER_TRIAGE_CARD.md`.
If you need a shortest-path sequence for turning a validator-clean blocked lane into an owner-ready signoff line, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_SEQUENCE.md`.
If you need a compact step-by-step bridge from validator PASS to a signoff-ready handoff sentence, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_HANDOFF_SEQUENCE.md`.
If you need a compact next-action wording guide before declaring handoff-ready, open `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_HANDOFF.md`.
If you need a compact signoff gate for deciding whether the next action is specific enough to call the artifact handoff-ready, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_NEXT_ACTION_GATE.md`.
If you need a shorter report-scoped wording brief before that handoff sentence, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_REPORT_SCOPE_BRIEF.md`.
If you need safer wording for PASS artifacts that still should not be called signoff-ready, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_BLOCKER_LANGUAGE.md`.
If you need a one-screen matrix for judging whether the next action already has enough target/artifact support for replay, open `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_SUPPORT_MATRIX.md`.
If you need a compact rule for keeping signoff `next_action` tied to the exact failed check or artifact path before claiming handoff-ready replay, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_NEXT_ACTION_ARTIFACT_RULE.md`.
If you need a compact pre-handoff priority check for whether the next-action sentence names the hottest blocked lane and proof target, open `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_PRIORITY_CHECK.md`.
If you need a compact evidence gate for deciding whether the next-action line already names the failed lane, stable target, and proof artifact, open `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_EVIDENCE_GATE.md`.
If you need a one-line status sentence once the next action is already known, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_NEXT_ACTION_STATUS_LINE.md`.
If you need a fast check for whether the next-action line already makes owner routing obvious, open `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_OWNER_CHECK.md`.
If you need a short human-ready wording audit before posting that next-action line, open `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_HUMAN_READY_CHECK.md`.
If you need a shortest-path sequence for turning a passing artifact into an owner-routable next-action sentence, open `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_OWNER_SEQUENCE.md`.
If you need a compact validator-clean versus handoff-ready wording check before signoff, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_HANDOFF_READY_SIGNAL.md`.
If you need a one-screen note for keeping a passing handoff intentionally lane-scoped instead of sounding whole-run ready, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_SCOPE_NOTE.md`.
If you need a one-line status update that keeps the passing handoff scoped to the real rerun boundary, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_SCOPE_STATUS_LINE.md`.
If you need a one-screen check for whether a passing handoff still needs to stay section-scoped instead of sounding whole-run ready, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_SECTION_SCOPE_CHECK.md`.
If you need a compact rule for keeping owner-alias handoffs scoped to the real replay lane instead of sounding whole-run ready, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_ALIAS_SCOPE_RULE.md`.
If you need a compact card for deciding whether the next-action line is rerun-ready enough to hand off, open `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_RERUN_CUE.md`.
If you need a fast scope check before turning a passing artifact into a broader replay request, open `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_SCOPE_TRIM.md`.
If you need a one-screen rerun-versus-repair chooser after validation already passed, open `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_RERUN_DECIDER.md`.
If you need a one-screen rule for keeping a passing report's rerun request narrow instead of drifting into a full replay, open `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_REPLAY_BOUNDARY.md`.
If you need a compact rerun-only handoff checklist after validation already passed, open `docs/WEB_QA_PLAYWRIGHT_RERUN_HANDOFF_CARD.md`.
If you need a quick artifact-specific check before calling that rerun handoff replay-ready, open `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_RERUN_ARTIFACT_CHECK.md`.
If you need a one-line rerun owner handoff after that checklist, open `docs/WEB_QA_PLAYWRIGHT_RERUN_OWNER_STATUS_LINE.md`.
If you need a slightly broader signoff-safe rerun sentence before handoff, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_RERUN_STATUS_LINE.md`.
If you need a compact pass/fail cue for whether a validator-clean artifact is truly ready for a focused rerun handoff, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_RERUN_READY_SIGNAL.md`.
If you need a one-screen rule for deciding whether replay support is strong enough to keep the rerun lane narrow, open `docs/WEB_QA_PLAYWRIGHT_REPLAY_SUPPORT_SCOPE_GATE.md`.
Validator JSON now exposes replay-support states such as `target_and_artifact_refs`, `target_refs_only`, `artifact_refs_only`, and `none`, so downstream handoffs can describe rerun scope without rebuilding that classification.
If you need a fast green/yellow/red cue sheet before calling a failure lane rerun-ready, open `docs/WEB_QA_PLAYWRIGHT_RERUN_READINESS_CUES.md`.
If you need a one-screen retry-versus-repair decision card before choosing the next move, open `docs/WEB_QA_PLAYWRIGHT_RETRY_DECISION_CARD.md`.
If you need a compact hotspot-only rerun brief after strict-plus validation already named the blocked lane, open `docs/WEB_QA_PLAYWRIGHT_HOTSPOT_HANDOFF_CARD.md`.
If you need a compact reproduce-triage-rerun loop before writing the next-action line, open `docs/WEB_QA_PLAYWRIGHT_SCENARIO_RECOVERY_LOOP.md`.
If you need a one-screen lane audit before calling the rerun scope safe, open `docs/WEB_QA_PLAYWRIGHT_REPLAY_LANE_AUDIT.md`.
If you need a 30-second call on whether the next rerun should stay lane-scoped or expand to section scope, open `docs/WEB_QA_PLAYWRIGHT_RERUN_SCOPE_CARD.md`.
If you need a one-screen rule for turning hotspot JSON into the next repair sentence, open `docs/WEB_QA_PLAYWRIGHT_HOTSPOT_NEXT_STEP.md`.
If you need a compact maturity ladder for deciding whether a passing artifact is merely validator-clean or truly handoff-ready, open `docs/WEB_QA_PLAYWRIGHT_HANDOFF_READINESS_LADDER.md`.
If you need a one-screen rule for making `Next action:` cover every failed check id before strict-plus handoff, open `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_ALL_FAILED_REFS.md`.
If you need a quick picker for the isolated strict-plus fail fixtures before replaying a validator error, open `docs/WEB_QA_PLAYWRIGHT_STRICT_PLUS_FAIL_FIXTURE_MAP.md`.
If you need a last-pass review card before declaring a strict web QA report signoff-ready, open `docs/WEB_QA_STRICT_SIGNOFF_CHECKLIST.md`.
If you need a tighter replay handoff for failed strict web QA runs, open `docs/WEB_QA_REPLAY_HANDOFF_CARD.md`.
If you need a compact rerun-versus-repair split card after validation already passed, open `docs/WEB_QA_PLAYWRIGHT_RERUN_REPAIR_SPLIT.md`.
If you need a one-screen decision card for whether a validator-clean blocker should go to focused rerun or wording repair next, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_RERUN_REPAIR_DECIDER.md`.
If you need a compact exit-criteria check before calling a passing artifact signoff-ready, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_EXIT_CRITERIA.md`.
If you need a one-screen rule for deciding whether a validator-clean artifact should stop at signoff or go back through a focused rerun, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_RERUN_SPLIT.md`.
If you need a four-line hotspot-first signoff brief before a rerun handoff, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_HOTSPOT_BRIEF.md`.
If you need a compact escalation sentence when multiple blocked lanes still compete after validation passes, open `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_HOTSPOT_ESCALATION.md`.
If you need a compact rule for choosing which passing-but-still-blocked lane deserves the handoff sentence first, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_PRIORITY_LADDER.md`.
If you need a compact owner-ready reminder for keeping a passing rerun request scoped to a single blocked lane, open `docs/WEB_QA_PLAYWRIGHT_RERUN_OWNER_BOUNDARY.md`.
If you need a quick ladder for choosing checkpoint-vs-lane-vs-section rerun scope after validation already passed, open `docs/WEB_QA_PLAYWRIGHT_RERUN_SCOPE_LADDER.md`.
If you need a compact green/yellow/red cue before calling that rerun request safely scoped, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_RERUN_SCOPE_SIGNAL.md`.
If you need a fast scope-choice check before calling a passing artifact checkpoint-, section-, or whole-run ready, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_REPLAY_SCOPE_CHECK.md`.
If you need a four-choice picker for the narrowest honest handoff label after validation passes, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_SCOPE_PICKER.md`.
If you need a 30-second pass/hold card before calling that scope sentence handoff-ready, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_SCOPE_QUICKCHECK.md`.
If you need copy-ready wording samples for checkpoint-, section-, rerun-, or hold-scoped signoff labels, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_SCOPE_EXAMPLES.md`.
If you need a compact scope ladder before choosing checkpoint-, lane-, section-, or hold-scoped wording, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_SCOPE_LADDER.md`.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Origin and Positioning](#origin-and-positioning)
- [Vision](#vision)
- [Project Direction (2026)](#project-direction-2026)
- [Core Principles](#core-principles)
- [Who This Project Is For](#who-this-project-is-for)
- [What Exists Today](#what-exists-today)
- [What We Are Building Next](#what-we-are-building-next)
- [Architecture and Repository Structure](#architecture-and-repository-structure)
- [How to Install](#how-to-install)
- [How to Use in Real Work](#how-to-use-in-real-work)
- [Quality Standards](#quality-standards)
- [Playwright Interactive Execution Principles](#playwright-interactive-execution-principles)
- [Playwright Interactive Step Verification](#playwright-interactive-step-verification)
- [Playwright Replay Blocker Triage](#playwright-replay-blocker-triage)
- [Playwright Replay Signals](#playwright-replay-signals)
- [Contributing Guide](#contributing-guide)
- [Governance and Decision-Making](#governance-and-decision-making)
- [Compatibility Notes](#compatibility-notes)
- [Roadmap](#roadmap)
- [References](#references)
- [License](#license)

---

## Project Overview

`openclaw-codex-pm-skills` turns PM workflows into skill assets that can be consistently applied in OpenClaw-based agent operations.

It focuses on practical outcomes:

- better discovery quality,
- clearer strategy artifacts,
- faster PRD drafting,
- more transparent prioritization,
- and repeatable outputs in team environments.

This is **not** a prompt dump.
It is a structured, evolving skill system intended for real delivery workflows.

---

## Origin and Positioning

This repository is inspired by the ideas and workflow style of:

- [phuryn/pm-skills](https://github.com/phuryn/pm-skills)

and adapts those concepts for OpenClaw/Codex usage patterns.

### Important scope statement

- This is an **independent community adaptation**, not an official fork.
- We preserve intent (PM rigor and workflow clarity), not runtime-specific behavior.
- We intentionally avoid vendor-locked orchestration semantics.

---

## Vision

Build the most practical open PM skill pack for agent-assisted product development, where outputs are:

1. **actionable** (usable in real planning and execution),
2. **auditable** (clear rationale and traceable assumptions),
3. **collaborative** (easy for multiple contributors to improve),
4. **portable** (usable across OpenClaw/Codex-style setups).

---

## Project Direction (2026)

### Direction A — Practical PM execution

Prioritize skills that directly improve shipping quality:

- discovery
- strategy
- PRD
- prioritization
- risk/assumption management

### Direction B — Shared team standards

Standardize output formats so multiple contributors can collaborate without style drift.

### Direction C — Safe, transparent automation

Support automation with explicit boundaries and predictable outputs, especially in group/chat contexts.

### Direction D — Open contributor ecosystem

Design the project so contributors can add domain packs (B2B SaaS, Web3, infra tools, etc.) with consistent quality.

---

## Core Principles

1. **Portability over lock-in**
2. **Clarity over magic**
3. **Determinism over ambiguity**
4. **Safety over convenience**
5. **Incremental improvement over giant rewrites**

---

## Who This Project Is For

- Product managers using agent-assisted workflows
- Founders who need PM structure in fast-moving build cycles
- AI-native teams shipping iterative product changes
- OSS contributors who want reusable PM skill assets

---

## What Exists Today

Current initial skill packs:

- `pm-discovery-foundations`
- `pm-strategy-canvas`
- `pm-prd-drafting`
- `pm-prioritization-helper`
- `web-qa-playwright` (now includes QA inventory + failure-recovery references for interactive browser testing)

Current docs:

- `docs/INSTALL_OPENCLAW.md`
- `docs/COMPATIBILITY.md`
- `docs/MAPPING_PM_SKILLS.md`
- `docs/PR_MERGE_POLICY.md`
- `docs/WEB_QA_PLAYWRIGHT_REPLAY_PROFILE.md`
- `docs/WEB_QA_PLAYWRIGHT_REPLAY_SIGNALS.md` (defines a deterministic first-look order for section status, hotspot blocker, next step, replay support, and unresolved handoff signals)
- `docs/WEB_QA_PLAYWRIGHT_PRECHECK.md` (adds a 1-minute pre-run stability/reproducibility checklist before the first interactive step)
- `docs/WEB_QA_PLAYWRIGHT_FAILURE_HANDOFF.md`
- `docs/WEB_QA_PLAYWRIGHT_JSON_HANDOFF.md`
- `docs/WEB_QA_PLAYWRIGHT_EXECUTION_LOOP.md` (now explicitly documents Playwright-interactive-style stability, reproducibility, step-by-step verification, and failure-recovery rules)
- `docs/WEB_QA_PLAYWRIGHT_CHECKPOINT_EVIDENCE_LADDER.md` (adds a compact target -> action -> verification -> artifact -> recovery ladder so each interactive checkpoint stays replay-ready)
- `docs/PLAYWRIGHT_FAILURE_RECOVERY_HANDOFF.md` (adds a compact repair-order checklist for target refs -> evidence -> chronology -> recovery prose handoff)
- `docs/PLAYWRIGHT_INTERACTIVE_REPAIR_LOOP.md` (adds a concise rerun playbook for stabilizing the session, repairing one checkpoint at a time, restoring evidence, and confirming recovery before signoff)
- `docs/WEB_QA_PLAYWRIGHT_STEP_TEMPLATE.md` (adds a copyable single-checkpoint template so interactive QA reports keep one action, one verification step, one evidence artifact, and one recovery note per checkpoint)
- `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_LANES.md` (adds a READY-vs-BLOCKED section triage note so operators can choose the next deterministic replay lane directly from strict-plus JSON)
- `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_COVERAGE_CARD.md` (adds a compact validation-clean vs handoff-ready decision card for incomplete signoff coverage)
- `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_QUICKCHECK.md` (adds a 60-second human review order for deciding whether a strict-plus report is validation-clean and handoff-ready)
- `docs/WEB_QA_PLAYWRIGHT_SECTION_STATUS_CARD.md` (adds a copy-ready per-section handoff card so operators can pass `functional` / `visual` / `off_happy` replay status without reopening the full JSON)
- `docs/WEB_QA_PLAYWRIGHT_SECTION_REPAIR_ORDER.md` (adds a compact section-first repair order that maps READY/BLOCKED lanes, hotspot blockers, and first rerun targets into one operator checklist)
- `docs/WEB_QA_PLAYWRIGHT_QA_INVENTORY_RECOVERY.md` (adds a compact repair order for missing `Checks:` mappings, partial QA inventory coverage, and incomplete `Next action:` failed-check handoff)
- `docs/WEB_QA_PLAYWRIGHT_STABILITY_CHECKLIST.md` (condenses the same principles into a fast operator rerun checklist for blocked interactive runs)
- `docs/WEB_QA_PLAYWRIGHT_RECOVERY_EXIT_SIGNALS.md` (adds a compact READY-vs-BLOCKED exit check so operators can confirm failed-check ids, repaired refs, and fresh proof artifacts agree before signoff)
- `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_REPLAY_CARD.md` (adds a copy-ready next-action handoff card so blocked reruns keep failed-check ids, stable refs, artifacts, and verification cues in one deterministic sentence)
- Canonical opt-in traceability example: `examples/web_qa_playwright_strict_plus_with_check_refs_pass.md`
- Deterministic replay validation contract: use `--strict-plus --require-qa-inventory-check-refs --json-out artifacts/validation.json` so CI stores replay-ready metadata (`active_profile_preset`, 5/3/2 counts, QA inventory check refs, QA inventory missing-check coverage, unresolved failed-check coverage, deduplicated next-action failed-check refs, checkpoint target/artifact refs, reused checkpoint refs, per-checkpoint ref coverage counts, and section-level checkpoint timestamp coverage (`functional`/`visual`/`off_happy`) plus per-section replay-readiness blocker counts/coverage for replay triage) as a machine-readable artifact
- Replay triage JSON now also exposes `effective_replay_ready_sections`, `effective_replay_blocked_sections`, and `effective_replay_section_status`, so downstream reruns can instantly split section repair into READY vs BLOCKED lanes without recomputing blocker counts from raw per-section maps.
- Replay triage JSON now also exposes `effective_replay_readiness_hotspot_tied_sections`, `effective_replay_readiness_hotspot_tied_section_labels`, and a copy-ready `effective_replay_readiness_hotspot_tie_summary`, so rerun tooling can keep every section-sharing hotspot lane explicit instead of flattening ties into a single winner.
- Replay triage JSON now also exposes `effective_replay_readiness_hotspot_next_step`, `effective_replay_readiness_hotspot_primary_blocker_summary_by_blocker_key`, giving automation a copy-ready repair instruction per blocker key (`missing_target_refs`, `incomplete_evidence_refs`, etc.) without rebuilding hotspot checkpoint lists downstream.
- Next-action replay metadata now also exposes `next_action_replay_support_dimensions_present` and `next_action_replay_support_missing_dimensions`, so rerun bots can tell whether stable target refs and artifact refs are already present before reconstructing the repair lane from prose.
- Replay triage JSON now also exposes `effective_replay_readiness_hotspot_next_step`, `effective_replay_readiness_hotspot_primary_blocker_summary_by_section`, so rerun tooling can hand the hottest blocked section (`functional`, `visual`, `off_happy`) to an operator with one copy-ready repair sentence instead of reconstructing section/blocker/checkpoint context downstream.
- Replay triage JSON now also exposes `effective_replay_readiness_hotspot_blocker_share_by_key`, so CI can see whether the hotspot is split evenly across blocker classes or dominated by one blocker before choosing the first repair lane.
- Replay triage JSON now also exposes `effective_replay_readiness_hotspot_primary_blocker_key_by_section`, `effective_replay_readiness_hotspot_primary_blocker_checkpoint_ids_by_section`, and `effective_replay_readiness_hotspot_primary_blocker_next_step_by_section`, so tied hotspot sections keep their own first-fix lane without forcing downstream automation to flatten every blocked section into one global blocker queue.
- Replay triage JSON now also exposes structured `effective_replay_readiness_hotspot_primary_blocker` and `effective_replay_readiness_hotspot_primary_blocker_by_section` objects, so rerun tooling can consume the hottest blocker lane (global or per section) without stitching together separate key/count/checkpoint fields.
- Replay triage JSON now also exposes `effective_replay_readiness_hotspot_primary_blocker_summary_by_section`, giving rerun bots a copy-ready `blocker_key: checkpoint ids` sentence per hotspot section without rebuilding section-scoped handoff prose.
- Need a copy-ready scoped PASS note? `docs/WEB_QA_SIGNOFF_SCOPE_STATUS_LINE.md` documents a minimal signoff-scope status line for replay-ready subsets so public handoffs stay honest while broader reruns are still pending.
- Parser-facing QA inventory mapping examples: `docs/WEB_QA_PLAYWRIGHT_REPLAY_PROFILE.md` now includes PASS/FAIL JSON snippets for the opt-in `--require-qa-inventory-check-refs` contract so downstream CI can compare payload shape directly.
- QA inventory triage snippets now cover malformed mappings, partial coverage drift, and recovered PASS payloads side-by-side so machine parsers can distinguish formatting repair from missing-check restoration without replaying the full fixture set.
- Missing-`Checks:` recovery guidance: the replay-profile doc now pairs the isolated FAIL fixture with a count-based recovery checklist (`qa_inventory_check_ref_count` should move from `0` back to `10`) so CI triage can be resolved deterministically.
- Side-by-side PASS/FAIL smoke commands: `docs/WEB_QA_PLAYWRIGHT_REPLAY_PROFILE.md` now keeps paired copy/paste commands for the canonical PASS fixture and the isolated missing-`Checks:` FAIL fixture so replay triage can confirm both validation and recovery paths quickly.
- Replay-profile smoke script now asserts the missing-`Checks:` FAIL fixture still exposes the full 10-item QA universe and 5/3/2 checkpoint split while failing with exactly one mapping error, so CI triage can distinguish coverage drift from mapping-format drift immediately.
- Replay-profile smoke script now also covers isolated missing-artifact-path and status-consistency FAIL fixtures, keeping Playwright-style evidence-capture and step-by-step verification drift parser-visible with a single reusable smoke entrypoint.
- Replay-profile smoke coverage explicitly spans missing target refs, missing artifact paths, missing timestamps, and status-consistency-only drift so deterministic replay triage can be regression-checked without opening the full markdown fixtures first.
- Partial QA-inventory drift now has an explicit landing-page triage cue: if `qa_inventory_check_ref_count` is non-zero but `qa_inventory_missing_check_ref_count` stays above `0`, treat it as incomplete coverage drift (for the isolated fixture: `9 mapped / 1 missing`), not malformed `Checks:` syntax.
- Replay-profile smoke now also asserts the parser-facing coverage-rate split (`1.0` for malformed-but-complete mappings vs `0.9` for partial coverage drift), so CI can distinguish syntax repair from missing-check recovery without recomputing ratios.
- Replay triage JSON now exposes `qa_inventory_check_ref_coverage_rate` and `next_action_failed_check_coverage_rate` so CI can spot partial mapping/handoff drift without recomputing ratios downstream.
- Signoff metadata JSON now also exposes `signoff_field_values`, `signoff_field_status`, `present_signoff_fields`, `missing_signoff_fields`, and `signoff_field_coverage_rate`, so CI replay gates can tell which closure fields are already machine-readable vs still missing without reparsing markdown bullets.
- Failure handoff JSON now also groups both referenced and unresolved failed check ids by classification (`next_action_failed_check_ids_by_classification`, `unresolved_failed_check_ids_by_classification`) so follow-up reruns can route selector/runtime/product fixes without rebuilding that map downstream.
- Failure handoff JSON now also exposes per-classification follow-up coverage (`next_action_failed_check_coverage_rate_by_classification`, `unresolved_failed_check_coverage_rate_by_classification`) so CI can tell whether selector/runtime/product failures were fully handed off vs left unresolved without recomputing ratios downstream.
- Failure handoff JSON now also mirrors recovery owners for both referenced and unresolved failed checks (`next_action_failed_check_recovery_owners`, `unresolved_failed_check_recovery_owners`) so rerun routing can go straight to the right owner without reparsing markdown blocks.
- Failure handoff JSON now also exposes `unresolved_failed_check_handoff_summary`, a compact `F1: product -> checkout-team` string so replay operators and bots can paste the first missing recovery lane without stitching together id/classification/owner fields downstream.
- Failure handoff JSON now also groups failed checks by recovery owner (`failed_check_ids_by_recovery_owner`, `next_action_failed_check_ids_by_recovery_owner`, `unresolved_failed_check_ids_by_recovery_owner`) so rerun triage can route the whole owner lane in one lookup instead of rebuilding owner -> check maps downstream.
- Failure handoff JSON now also emits direct classification maps for the checks named in `Next action:` and the checks still left unresolved (`next_action_failed_check_classifications_by_id`, `unresolved_failed_check_classifications_by_id`) so replay automation can branch by selector/runtime/product without reconstructing it from grouped arrays.
- Checkpoint replay metadata now includes `missing_checkpoint_target_ref_ids` and `missing_checkpoint_artifact_ref_ids`, letting CI distinguish “checkpoint exists but lacks stable ref/artifact evidence” from ordering/count drift without re-parsing the markdown.
- Replay JSON now also exposes `checkpoint_evidence_ref_ids` plus `checkpoint_evidence_ref_coverage_rate`, so CI can see which checkpoints already carry both a stable UI target ref and an artifact path before triggering a replay.
- Section-based evidence triage is now documented end-to-end: the smoke script asserts missing/reused evidence coverage by `functional` / `visual` / `off_happy`, and `docs/WEB_QA_PLAYWRIGHT_JSON_HANDOFF.md` explains how to repair those sections in a deterministic order.
- Replay JSON now also exposes `missing_checkpoint_timestamp_count_by_section` and `missing_checkpoint_timestamp_coverage_rate_by_section`, so deterministic rerun triage can see which section still lacks timestamped checkpoints before replaying the full report.
- An isolated strict-plus missing-timestamp fixture (`examples/web_qa_playwright_strict_fail_missing_timestamp_only.md`) now keeps chronology repair reproducible without mixing it with monotonic-order drift.

Current examples:

- discovery prompt example
- strategy prompt example
- PRD prompt example
- prioritization prompt example
- web QA Playwright sample interactive run (`examples/web_qa_playwright_sample_run.md`)
- web QA Playwright strict-fail fixture for duplicate checkpoints (`examples/web_qa_playwright_strict_fail_duplicate_checkpoint.md`)
- web QA Playwright strict-fail fixture for missing failure evidence (`examples/web_qa_playwright_strict_fail_missing_evidence.md`)
- web QA Playwright strict-fail fixture for missing failure classification (`examples/web_qa_playwright_strict_fail_missing_classification.md`)
- web QA Playwright strict-fail fixture for malformed failure breakdown summary (`examples/web_qa_playwright_strict_fail_malformed_failure_breakdown.md`)
- web QA Playwright strict-fail fixture for missing `## 3) Execution log` header (`examples/web_qa_playwright_strict_fail_missing_execution_log_header.md`)
- web QA Playwright strict-plus combined fail fixture (duplicate checkpoints + missing failure metadata in one report) (`examples/web_qa_playwright_strict_plus_combined_fail.md`)
- web QA Playwright strict-plus pass fixture (deterministic replay gates all satisfied, including replay readiness signoff) (`examples/web_qa_playwright_strict_plus_pass.md`)
- web QA Playwright strict-plus pass fixture with explicit QA inventory `Checks:` mappings for opt-in traceability validation (`examples/web_qa_playwright_strict_plus_with_check_refs_pass.md`)
- web QA Playwright strict-plus isolated missing-`Checks:` fail fixture for QA inventory mapping triage (`examples/web_qa_playwright_strict_fail_missing_check_refs_only.md`)
- web QA Playwright strict-plus partial-coverage fail fixture for incomplete QA inventory mapping drift (`examples/web_qa_playwright_strict_fail_partial_check_refs_only.md`)
- web QA Playwright strict-plus isolated artifact-ref reuse fail fixture for CI triage (`examples/web_qa_playwright_strict_fail_artifact_ref_reuse_only.md`)
- web QA Playwright strict-plus isolated monotonic-timestamp fail fixture for replay-order triage (`examples/web_qa_playwright_strict_fail_monotonic_timestamp_only.md`)
- web QA Playwright strict-plus isolated missing-timestamp fail fixture for chronology-field triage (`examples/web_qa_playwright_strict_fail_missing_timestamp_only.md`)
- web QA Playwright strict-plus isolated status-consistency fail fixture for checkpoint/check drift triage (`examples/web_qa_playwright_strict_fail_status_inconsistency_only.md`)
- web QA Playwright strict-plus isolated missing-artifact-path fail fixture for evidence-capture triage (`examples/web_qa_playwright_strict_fail_missing_artifact_paths_only.md`)
- web QA Playwright strict-plus isolated missing-recovery-owner fail fixture for explicit owner-handoff triage (`examples/web_qa_playwright_strict_fail_missing_recovery_owner_only.md`)

---

## Playwright Replay Signals

If you need the shortest possible operator-first triage order for a blocked strict-plus report, open `docs/WEB_QA_PLAYWRIGHT_REPLAY_SIGNALS.md`.
If you need a quick artifact-only check before reopening the full markdown report, open `docs/WEB_QA_PLAYWRIGHT_JSON_OUT_ARTIFACT_CHECK.md`.
If you need a compact report-safety check before trusting generated HTML headings in a replay artifact, open `docs/WEB_QA_PLAYWRIGHT_HTML_HEADING_ESCAPE_CHECK.md`.
It keeps the first scan deterministic: section lane -> hotspot blocker -> copy-ready next step -> next-action replay support -> unresolved failed-check handoff.
If you need the isolated strict-plus fixtures in a repair-first order before opening the full report, open `docs/WEB_QA_PLAYWRIGHT_REPLAY_FIXTURE_SEQUENCE.md`.

## What We Are Building Next

Near-term priorities:

1. stronger skill specifications (inputs/outputs/evaluation criteria),
2. review checklist per skill PR,
3. domain-specific extensions,
4. compatibility matrix across OpenClaw runtime patterns,
5. starter integration recipes for real product teams.

---

## Architecture and Repository Structure

```text
openclaw-codex-pm-skills/
├─ skills/                      # Core and extension skill packs
│  ├─ pm-discovery-foundations/
│  ├─ pm-strategy-canvas/
│  ├─ pm-prd-drafting/
│  └─ pm-prioritization-helper/
├─ docs/
│  ├─ INSTALL_OPENCLAW.md       # Installation and activation guidance
│  ├─ COMPATIBILITY.md          # Runtime compatibility and constraints
│  └─ MAPPING_PM_SKILLS.md      # Upstream concept mapping
├─ examples/                    # Real prompt usage examples
├─ scripts/
│  ├─ install_local.sh          # Local installation helper
│  └─ validate_web_qa_report.py # Fixed-count QA report validator (5/3/2)
└─ .github/workflows/ci.yml     # Minimal structural validation
```

---

## How to Install

```bash
git clone https://github.com/sonwr/openclaw-codex-pm-skills.git
cd openclaw-codex-pm-skills
./scripts/install_local.sh
```

By default this installs to `~/.openclaw/skills`.

For custom location:

```bash
./scripts/install_local.sh /path/to/skills
```

Then ensure your OpenClaw configuration allows these skills for your target agent.

---

## How to Use in Real Work

### 1) Discovery sprint
Use `pm-discovery-foundations` to produce:

- problem framing
- assumption ranking
- low-cost experiments
- decision recommendation

### 2) Strategy alignment
Use `pm-strategy-canvas` to produce:

- target segment
- strategic bets
- risk mitigation plan
- measurable checkpoints

### 3) Build planning
Use `pm-prd-drafting` to produce:

- one-page PRD
- scope boundaries
- acceptance criteria

### 4) Prioritization session
Use `pm-prioritization-helper` to produce:

- weighted rankings
- exclusion rationale
- revisit triggers

### 5) Browser QA signoff discipline
Use `web-qa-playwright` and validate the final markdown run artifact:

```bash
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_sample_run.md --strict
```

For machine-readable CI output, add `--json` (stdout) or `--json-out <path>` (artifact file).

For a reusable explanation of deterministic replay expectations and failure-recovery discipline, see `docs/WEB_QA_PLAYWRIGHT_REPLAY_PROFILE.md`.
For a 1-minute pre-run checklist that freezes target/profile/evidence before the first click, see `docs/WEB_QA_PLAYWRIGHT_PRECHECK.md`.
That note now also documents a stepwise replay recovery order: restore stable target refs first, replay evidence second, checkpoint chronology third, and human recovery notes last.
For a faster blocked-run triage workflow focused on `report_metadata`, owner handoff, and failed-check reruns, see `docs/WEB_QA_PLAYWRIGHT_FAILURE_HANDOFF.md`.
For machine-readable CI contracts and JSON artifact routing, see `docs/WEB_QA_PLAYWRIGHT_JSON_HANDOFF.md`.
For reviewer-facing merge rules and copy-paste PASS/blocked-run commands, see `docs/PR_MERGE_POLICY.md`.
For a concise execution loop that mirrors Playwright-interactive principles (inventory -> bootstrap -> verify -> recover), see `docs/WEB_QA_PLAYWRIGHT_EXECUTION_LOOP.md`.

Practical rule of thumb for browser automation signoff:
- lock one reproducible preset/profile for the whole run,
- verify each meaningful UI transition before moving on,
- capture evidence in the exact state being signed off,
- and write failure owner + next action before widening reruns.
For a shorter operator handoff that freezes profile/refs before reruns, see `docs/WEB_QA_PLAYWRIGHT_STABILITY_CHECKLIST.md`.
For a JSON-first READY-vs-BLOCKED triage note that tells operators which replay lane to repair next, see `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_LANES.md`.
For a shorter “which blocker do I repair first?” operator note, see `docs/WEB_QA_PLAYWRIGHT_BLOCKER_PRIORITY.md`.
For a compact repair-order ladder that turns blocked replay metadata into one first-fix decision, see `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_PRIORITY_LADDER.md`.
For hotspot-first section repair when replay metadata points at one blocked lane, see `docs/WEB_QA_PLAYWRIGHT_SECTION_HOTSPOT_REPAIR.md`.
For a shorter copy/paste rerun note driven directly by the hotspot JSON lane, see `docs/WEB_QA_PLAYWRIGHT_REPAIR_LANE_CARD.md`.
The blocker-priority note now keeps the replay repair order explicit: target refs -> artifact evidence -> chronology -> state consistency -> owner handoff.

Recommended operator loop before every interactive rerun:

1. lock the replay preset (`--playwright-interactive-profile` / `--strict-plus`) and keep the same target refs/artifact naming scheme,
2. validate one isolated drift fixture before broad reruns,
3. repair only the failing invariant (selector, evidence, ordering, or status consistency),
4. rerun the canonical PASS fixture to prove recovery before updating docs/CI handoff text.

This keeps browser QA changes aligned with Playwright-interactive priorities: stability first, reproducible evidence, step-by-step verification, and explicit failure recovery.

`--strict` adds reproducibility gates aligned with Playwright-interactive principles:

- deterministic preconditions (URL, viewport, test account)
- deterministic check labeling (F1..F5 / V1..V3 / O1..O2)
- screenshot evidence density for visual checks (at least one inline shot per V-check)
- normalized status tokens on every check row (`PASS`/`FAIL`)
- explicit signoff fields (regression count + merge recommendation)
- signoff-check consistency (reported regression count must equal checklist `FAIL` line count)
- section summary ratio consistency (`x/y pass`) vs detailed PASS/FAIL lines
- step-by-step execution log checkpoints for all fixed check ids (F1..F5, V1..V3, O1..O2) in deterministic order
- failure recovery traceability for failed checks (`Expected`/`Observed`/`First failure timestamp`/`Retry`)

Optional hardening flags:

- `--strict-plus`: enable `--strict` and all hardening flags below as a single CI preset for deterministic replay and failure recovery.
- `--playwright-interactive-profile`: apply a Playwright-interactive reliability preset (strict-plus equivalent) to prioritize stability, reproducibility, step verification, and failure recovery in one flag.

Playwright-interactive operating principles reflected in this preset and fixture set:

1. **Stability first** — require explicit checkpoint timestamps/status tokens/target refs so repeated runs stay comparable.
2. **Reproducibility first** — keep deterministic replay artifacts (`--json-out`, isolated fail fixtures, PASS fixture) available for CI and triage.
3. **Step-by-step verification** — enforce execution-log shape plus QA inventory/checkpoint accounting instead of trusting free-form prose.
4. **Failure recovery** — require artifact paths, failure classification, and recovery owner/plan metadata so broken runs remain actionable.
5. **Explicit handoff (opt-in)** — enable `--require-next-action` when you want a concrete `Next action:` signoff line for the next deterministic rerun.
6. **Failure-traceable handoff (opt-in)** — add `--require-next-action-failed-check-ref` when blocked runs must point the next owner to a failed check id such as `F2` or `V1`.
- `--deterministic-replay-profile`: alias for `--playwright-interactive-profile` for teams that prefer deterministic replay wording in CI policies.
- `--strict-replay-profile`: alias for `--playwright-interactive-profile` for teams that want explicit strict replay wording in CI presets.
- `--ci-replay-profile`: alias for `--playwright-interactive-profile` for teams that prefer shorter replay-policy naming in CI jobs.
  - CI now smoke-tests all three aliases against the same PASS fixture so downstream policy names cannot silently drift.
- `--enforce-checkpoint-format`: require each checkpoint line to use `action -> verification` format for clearer step-level reproducibility.
- `--require-checkpoint-timestamps`: require each checkpoint line to include an ISO-8601 UTC timestamp (`YYYY-MM-DDTHH:MM:SSZ`) for deterministic replay timelines.
- `--enforce-monotonic-checkpoint-timestamps`: require checkpoint timestamps to be monotonic in execution-log order, making replay order drift visible in CI.
- `--enforce-checkpoint-status-tokens`: require each checkpoint line to include explicit `PASS`/`FAIL` token for parser-safe replay traces.
- `--require-visual-checkpoint-evidence`: require each visual checkpoint line (`V1..V3`) to include an inline screenshot path for reproducible visual proof.
- `--require-checkpoint-artifact-paths`: require every checkpoint line to include at least one inline artifact path (screenshot/video/log/trace) for post-failure replay and evidence auditing.
- `--require-checkpoint-target-refs`: require every checkpoint line to include a stable target reference token (`ref=<id>`) so interactive replay can bind actions to deterministic UI targets.
- `--enforce-checkpoint-target-ref-uniqueness`: require each checkpoint target ref to map to exactly one checkpoint, so replay selectors stay stable and unambiguous across retries.
- `--enforce-checkpoint-artifact-ref-uniqueness`: require each inline artifact path to appear in only one checkpoint line, reducing ambiguous replay evidence mapping.
- `--require-failure-evidence-artifact-paths`: require failed checks to include an inline artifact path on the `Evidence:` line, so triage links are machine-verifiable.
- `--require-failure-recovery-plan`: require failed checks to include a `Recovery plan:` line with deterministic next-step recovery instructions.
- `--require-failure-recovery-owner`: require failed checks to include a `Recovery owner:` line so ownership is explicit for follow-up recovery.
- `--require-next-action`: require signoff to include a `Next action:` line so replay handoff remains explicit even on PASS runs.
- `--require-next-action-failed-check-ref`: when regressions are present, require `Next action:` to mention at least one failed check id so the next rerun owner knows exactly which check to recover first.
- `--enforce-failure-timestamp-order`: require failed-check `First failure timestamp` values to be monotonic in checklist order, preventing chronology drift in failure triage.
- `--enforce-checkpoint-to-check-status-consistency`: require each checkpoint line to include `PASS`/`FAIL` and match the checklist status for that same check id (prevents replay-log/checklist drift).
- `--require-failure-classification-summary`: require a signoff line in the form `Failure breakdown: selector=<n>, runtime=<n>, product=<n>` and validate it against failed-check classifications.
- `--require-execution-log-step-count-match`: require the execution log to contain only checkpoint bullets and exactly 10 checkpoint lines (F1..F5, V1..V3, O1..O2), which tightens deterministic replay step accounting.
- `--require-qa-inventory-section`: require the report to include a `## QA inventory` section with explicit environment/tool metadata for replayable incident audits.
- `--require-qa-inventory-check-refs --require-qa-inventory-full-coverage`: tighten QA inventory mapping so every checklist id is referenced at least once and stdout explicitly reports the full-coverage gate when enabled.

The validator always enforces the fixed structure rule (5 functional / 3 visual / 2 off-happy-path checks).

Troubleshooting fixture commands:

```bash
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_duplicate_checkpoint.md --strict
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_missing_evidence.md --strict
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_missing_classification.md --strict
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_missing_execution_log_header.md --strict
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_malformed_failure_breakdown.md --strict --require-failure-classification-summary
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_monotonic_timestamp_only.md --strict-plus
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_missing_artifact_paths_only.md --strict-plus
```

Expected outcomes:
- duplicate-checkpoint fixture: `FAIL` with `duplicate checkpoint ids` error.
- missing-evidence fixture: `FAIL` with `failed check ... must include an Evidence: line` error.
- missing-classification fixture: `FAIL` with `failed check ... must include a Failure classification: line` error.
- malformed-failure-breakdown fixture: `FAIL` with failure-classification-summary mismatch when `--require-failure-classification-summary` is enabled.
- missing-execution-log-header fixture: `FAIL` with strict-mode `Execution log` section-header error.
- missing-target-refs fixture: `FAIL` with exactly one strict-plus `checkpoint target refs` error for selector traceability triage.
- missing-artifact-paths-only fixture: `FAIL` with exactly one strict-plus `checkpoint artifact paths` error for evidence-capture triage.
- monotonic-timestamp-only fixture: `FAIL` with exactly one `checkpoint timestamp order` error under `--strict-plus`.

### Strict-plus isolated triage matrix

Use these deterministic fixtures to isolate one replay drift at a time:

- `web_qa_playwright_strict_fail_artifact_ref_reuse_only.md` → artifact mapping drift (`checkpoint artifact refs`)
- `web_qa_playwright_strict_fail_monotonic_timestamp_only.md` → replay-order drift (`checkpoint timestamp order`)
- `web_qa_playwright_strict_fail_status_inconsistency_only.md` → checklist/log state drift (`status consistency`)
- `web_qa_playwright_strict_fail_missing_target_refs.md` → selector-target traceability drift (`checkpoint target refs`)
- `web_qa_playwright_strict_fail_target_ref_reuse_only.md` → selector alias drift (`target ref uniqueness`)
- `web_qa_playwright_strict_fail_missing_artifact_paths_only.md` → evidence-capture drift (`checkpoint artifact paths`)

Copy-paste recovery commands:

```bash
# Artifact mapping drift
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_artifact_ref_reuse_only.md --strict-plus --json-out .tmp/web-qa-artifact-ref-reuse.json

# Replay-order drift
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_monotonic_timestamp_only.md --strict-plus --json-out .tmp/web-qa-monotonic-only.json

# Checklist/log status drift
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_status_inconsistency_only.md --strict-plus --json-out .tmp/web-qa-status-inconsistency.json

# Selector traceability drift
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_missing_target_refs.md --strict-plus --json-out .tmp/web-qa-missing-target-refs.json

# Selector alias drift
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_target_ref_reuse_only.md --strict-plus --json-out .tmp/web-qa-target-ref-reuse.json

# Evidence capture drift
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_missing_artifact_paths_only.md --strict-plus --json-out .tmp/web-qa-missing-artifact-paths.json
```

This mirrors Playwright-interactive-style recovery: isolate a single failing invariant, verify it deterministically, then fix only that layer before broad reruns.

CI now includes a negative-fixture guard: each strict-fail fixture must fail validation so policy regressions are caught early.
CI now also smoke-tests the isolated target-ref-uniqueness fixture so selector alias drift cannot silently bypass replay-policy coverage.
Need a quick alias smoke check? `docs/WEB_QA_PLAYWRIGHT_REPLAY_PROFILE.md` now includes copy-paste commands that run the same PASS fixture through `--playwright-interactive-profile`, `--deterministic-replay-profile`, `--strict-replay-profile`, and `--ci-replay-profile` so CI owners can confirm alias parity without inventing new fixtures.
Need an executable repo-local smoke check? Run `scripts/smoke_replay_profile_examples.sh` to verify all replay-profile aliases against the replay-ready PASS fixture, the isolated missing-`Checks:` / partial-coverage QA inventory FAIL fixtures, and every strict-plus one-invariant replay fixture in the triage matrix. For owner-based repair sequencing before the rerun, open `docs/WEB_QA_PLAYWRIGHT_RECOVERY_OWNER_SORT.md`.
The replay metadata now also exposes `next_action_replay_handoff_card`, a compact `checks=...; targets=...; artifacts=...; rerun=...` string for CI bots that need a single deterministic replay cue without reconstructing the richer JSON summary fields.
The smoke script now also emits an explicit malformed-vs-partial QA inventory triage assertion, so recovery automation can tell apart `10 mapped / 0 missing` format drift from `9 mapped / 1 missing` coverage drift without replaying fixtures by hand.
It also locks the full Playwright-interactive recovery loop in one place: isolate exactly one failing invariant, confirm the parser-facing error stays singular, then repair only that layer before broader reruns.
CI also snapshots a strict-plus PASS fixture to JSON and asserts the downstream parser-facing payload shape (`status`, enabled gates, and fixed `counts`).
- JSON payloads now include `validation_schema_version` so CI parsers can detect contract changes explicitly.
- JSON payloads also include `active_profile_preset` so downstream CI can tell which replay preset produced the result without inferring from multiple booleans. Replay metadata also separates first-seen checkpoint refs from `checkpoint_reused_target_refs` / `checkpoint_reused_artifact_refs` so strict handoff jobs can detect evidence reuse without recomputing it downstream. It also emits `missing_checkpoint_evidence_dimensions_by_id` / `missing_checkpoint_evidence_dimensions_by_section` plus aggregate `missing_checkpoint_evidence_dimension_counts`, so replay queues can see whether a checkpoint is blocked by a missing target ref, artifact ref, timestamp, or a combination of them before opening the markdown report. Reused evidence is now also grouped per checkpoint via `checkpoint_reused_target_refs_by_id` / `checkpoint_reused_artifact_refs_by_id`, which makes follow-up reruns immediately traceable to the duplicated checkpoint instead of forcing CI to reverse-map shared refs. Replay metadata now also exposes `has_signoff_section`, `reported_regressions`, `merge_recommendation`, `replay_readiness`, `replay_readiness_reference_regressions`, `replay_readiness_consistent_with_failed_checks`, `replay_readiness_blockers`, `replay_readiness_blocker_keys`, `replay_readiness_blocker_counts`, `effective_replay_readiness_blocker_keys`, `effective_replay_readiness_blocker_counts`, `effective_replay_readiness_blocker_count`, `replay_readiness_blocker_keys_by_section`, `effective_replay_readiness_added_blocker_keys_by_section`, `effective_replay_readiness_blocker_delta_by_section`, `missing_signoff_fields`, `missing_signoff_field_count`, `signoff_field_coverage_rate`, `has_next_action`, and raw `next_action_text`, so handoff jobs can distinguish missing closure, contradictory READY/BLOCKED signoff, and partially filled signoff blocks before parsing free-form markdown.

Parser-facing JSON snippets for downstream CI contracts:

```json
{
  "status": "PASS",
  "validation_schema_version": 1,
  "active_profile_preset": "strict-plus",
  "counts": {"functional": 5, "visual": 3, "off_happy_path": 2},
  "report_metadata": {
    "qa_inventory_check_refs": ["F1", "F2", "F3", "F4", "F5", "V1", "V2", "V3", "O1", "O2"],
    "failed_check_ids": [],
    "failed_check_classifications_by_id": {},
    "failed_check_classification_counts": {"selector": 0, "runtime": 0, "product": 0},
    "missing_failed_check_classification_ids": [],
    "next_action_failed_check_refs": []
  }
}
```

```json
{
  "status": "FAIL",
  "validation_schema_version": 1,
  "errors": [
    "qa inventory check refs: every QA inventory bullet must include 'Checks:' mapping"
  ],
  "report_metadata": {
    "qa_inventory_check_refs": [],
    "failed_check_ids": [],
    "failed_check_classifications_by_id": {},
    "failed_check_classification_counts": {"selector": 0, "runtime": 0, "product": 0},
    "missing_failed_check_classification_ids": [],
    "next_action_failed_check_refs": []
  }
}
```

---

## Quality Standards

A skill should be merged only if it is:

- **Clear**: purpose and when-to-use are explicit.
- **Structured**: includes deterministic output sections.
- **Testable**: has at least one realistic usage example.
- **Safe**: no hidden destructive instructions.
- **Maintainable**: concise, readable, and versionable.

For browser automation and interactive QA work, this repository also follows a local Playwright-interactive operating loop:

- stabilize the target before acting,
- verify each action step-by-step,
- capture evidence on the same checkpoint,
- classify failures for deterministic recovery,
- and hand off the next action clearly for replay.

Primary reference: `docs/PLAYWRIGHT_INTERACTIVE_EXECUTION_PRINCIPLES.md`

---

## Playwright Interactive Execution Principles

If you are updating web QA prompts, fixtures, or report validation rules, read:

- `docs/PLAYWRIGHT_INTERACTIVE_EXECUTION_PRINCIPLES.md`
- `docs/WEB_QA_PLAYWRIGHT_REPLAY_PROFILE.md`
- `docs/WEB_QA_PLAYWRIGHT_STABILITY_CHECKLIST.md`
- `docs/WEB_QA_PLAYWRIGHT_FAILURE_HANDOFF.md`

- `docs/WEB_QA_PLAYWRIGHT_SECTION_RERUN_CHECKLIST.md` (adds a section-by-section rerun order so operators repair one blocked lane at a time before widening replay scope)
- `docs/WEB_QA_PLAYWRIGHT_BLOCKED_SECTION_HANDOFF.md` (adds a minimal section-scoped handoff pattern so blocked `functional` / `visual` / `off_happy` lanes can be copied straight from strict-plus JSON into the next rerun)
These docs keep browser automation work aligned with deterministic replay, step-by-step verification, and failure-recovery handoff expectations.

---

## Playwright Replay Blocker Triage

If a report is technically valid but still hard to replay, use `docs/WEB_QA_PLAYWRIGHT_REPLAY_BLOCKER_TRIAGE.md` to group blocker-heavy failures by cause, owner, and smallest trustworthy rerun.

## Contributing Guide

We welcome contributors.

### Contribution flow

1. Fork and create a branch
2. Add or improve one focused skill/doc change
3. Include an example in `examples/` if behavior changed
4. Open a PR with:
   - purpose,
   - before/after behavior,
   - sample output format,
   - compatibility notes

### Commit style

- `feat:` new capability
- `fix:` correctness/safety improvement
- `docs:` documentation improvements
- `chore:` maintenance tasks

### PR review checklist (required)

- [ ] Scope is clear and narrow
- [ ] Output format is explicit
- [ ] Example is included/updated
- [ ] No vendor-locked assumptions hidden in skill text
- [ ] Compatibility implications are documented

---

## Governance and Decision-Making

This repository currently follows a maintainer-driven model with transparent rationale in PRs.

As contributor volume grows, governance will evolve to:

- lightweight RFCs for major changes,
- domain maintainers for extension packs,
- release notes with migration guidance.

---

## Compatibility Notes

- Works well for file-based skill execution patterns.
- Requires adaptation for assistant-specific slash-command engines.
- This repository intentionally avoids hard dependencies on a single vendor runtime.

See full details in `docs/COMPATIBILITY.md`.

---

## Roadmap

### v0.2

- richer skill specs
- contributor checklist hardening
- additional examples

### v0.3

- domain extension packs
- stronger compatibility documentation
- quality scoring for skill submissions

### v0.4

- reusable "skill test scenarios" for regression checks
- release process for community contributions

### v1.0

Stable, community-supported PM skill framework for OpenClaw/Codex-style teams.

---

## References

- Upstream inspiration: [phuryn/pm-skills](https://github.com/phuryn/pm-skills)
- This project: adaptation for OpenClaw + Codex-style workflows

---

## License

MIT

## Playwright Interactive Step Verification

Need a compact handoff for step-by-step browser proof loops? Open `docs/PLAYWRIGHT_INTERACTIVE_STEP_VERIFICATION.md` for the minimum stable sequence: lock one replay preset, verify each checkpoint before advancing, and hand off the first repeated blocker with the smallest rerun command.
Need a short recovery checklist after one checkpoint fails? Open `docs/PLAYWRIGHT_INTERACTIVE_RECOVERY_CHECKLIST.md` for the smallest repair order: freeze scope, rerun one checkpoint, restore evidence, and only then continue the proof loop.


## Governance + UI proof handoff

For governance-heavy web work, pair `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_GOVERNANCE_NOTE.md` with `docs/WEB_QA_PLAYWRIGHT_STABILITY_CHECKLIST.md` so scenario intent, replay stability, and blocker wording stay aligned in one proof loop.

If you need a compact owner-handoff note after validating replay support, open `docs/WEB_QA_PLAYWRIGHT_FAILURE_OWNER_LANE.md`.
If you need a shortest-path note for scenario-file-first work that must land as JSON + Markdown + HTML artifacts, open `docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_REPORT_TRIAD_NOTE.md
- `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_ARTIFACT_ALIAS_NOTE.md` — Treat `report.outputs.artifacts` as the same report-files bundle contract as `report.outputs.files` so scenario-driven JSON/Markdown/HTML output stays reviewable.
`.

If you need a compact note on keeping long-running ACP repo work inside one durable Discord thread, open `docs/DISCORD_THREAD_ACP_SESSION_NOTE.md`.
If you need a compact governance-sandbox handoff for one scenario file plus one shared JSON/Markdown/HTML bundle, open `docs/GOVERNANCE_SANDBOX_REPORT_BUNDLE_NOTE.md`.
If you need a compact PM note for keeping one scenario file, one markdown/html/json report bundle, and one reusable stakeholder preset pack visible together, open `docs/GOVERNANCE_SANDBOX_SCENARIO_PRESET_REPORT_BUNDLE_NOTE.md`.

If you need a tiny PM-facing note for keeping stdin-driven scenario import tied to the same markdown/html/json report bundle, open `docs/GOVERNANCE_SANDBOX_STDIN_SCENARIO_REPORT_NOTE.md`.
If you need a compact reminder to keep an `inputs.source` alias visible when stdin drives the same governance-sandbox report bundle, open `docs/GOVERNANCE_SANDBOX_INPUTS_SOURCE_ALIAS_NOTE.md`.

If you need a compact governance-sandbox handoff for `report_author` / `report_authors` owner aliases, open `docs/GOVERNANCE_SANDBOX_REPORT_AUTHOR_ALIAS_NOTE.md`.
If you need a compact governance-sandbox handoff for a singular `report.reviewer` audience alias that still renders the same markdown/html/json report bundle, open `docs/GOVERNANCE_SANDBOX_REPORT_REVIEWER_ALIAS_NOTE.md`.
If you need a compact PM note for keeping one scenario-input wrapper tied to one report-output basename before a wider governance-sandbox replay, open `docs/GOVERNANCE_SANDBOX_SCENARIO_INPUTS_REPORT_OUTPUTS_NOTE.md`.

If you need a compact note for keeping one reviewer-facing report subtitle tied to the same governance-sandbox artifact bundle, open `docs/GOVERNANCE_SANDBOX_REPORT_SUBTITLE_NOTE.md`.
If you need a compact alias note for scenario files that prefer `report.headline` while keeping the same JSON/Markdown/HTML bundle contract, open `docs/GOVERNANCE_SANDBOX_REPORT_HEADLINE_ALIAS_NOTE.md`.

If you need a compact recovery note for keeping one governance-sandbox result card tied to one downloadable report bundle after a failed interaction, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_RESULT_CARD_RECOVERY_NOTE.md`.
If you need a compact proof note for keeping one governance-sandbox result card tied to one visible report bundle before widening the browser flow, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_RESULT_CARD_PROOF_NOTE.md`.

If you need a compact reminder to anchor the next action to the exact failed checks before widening the replay lane, open `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_FAILED_REFS_NOTE.md`.
If you need a shorter note for replaying one Playwright report bundle within the same stable scope, open `docs/WEB_QA_PLAYWRIGHT_REPORT_REPLAY_SCOPE.md`.
If you need one compact owner-facing handoff for one validated Playwright report bundle, open `examples/web_qa_playwright_report_bundle_owner_handoff.md`.
If you need one bridge note that keeps UI/UX-first demo shaping tied to replayable Playwright proof, open `docs/GOVERNANCE_SANDBOX_WEB_DEMO_UI_UX_PLAYWRIGHT_BRIDGE.md`.

If you need a tiny handoff note for keeping scenario-file report urgency visible in the rendered memo lane, open `docs/GOVERNANCE_SANDBOX_REPORT_PRIORITY_LANE_NOTE.md`.

If you need a shortest-path PM note for pairing one scenario review fixture with one named markdown/html/json bundle replay, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REVIEW_PACK_NOTE.md`.

If you need a compact PM reminder that governance-sandbox work stays ordered as scenario-file input -> markdown/html/json report bundle -> presets -> web demo -> demo GIF, open `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_PRIORITY_NOTE.md`.

If you need a compact note for governance-sandbox scenario-sheet wrapper aliases before widening report flows, open `docs/GOVERNANCE_SANDBOX_SCENARIO_SHEET_NOTE.md`.

If you need a compact PM note for scenario files that use `stakeholder_trait_map` / `trait_map` while keeping one imported fixture tied to one JSON/Markdown/HTML report bundle, open `docs/GOVERNANCE_SANDBOX_SCENARIO_TRAIT_MAP_NOTE.md`.
If you need a compact PM note for `scenario_sheet_bundle` wrappers that should keep one imported scenario plus one report-ready bundle path together, open `docs/GOVERNANCE_SANDBOX_SCENARIO_SHEET_BUNDLE_NOTE.md`.

If you need a compact PM note for keeping one report audience phrased as watchers while the same governance-sandbox scenario/report bundle stays stable, open `docs/GOVERNANCE_SANDBOX_REPORT_WATCHERS_NOTE.md`.
- Governance sandbox scenario/report bundle review note: `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_BUNDLE_REVIEW.md`

If you need a compact PM reminder to keep every active repo update gated by local validation before push, open `docs/PM_VALIDATE_THEN_PUSH_ACTIVE_REPOS_NOTE.md`.

If you need a compact PM cue for treating commented JSONC scenario files as the same scenario-file-first proof lane, open `docs/GOVERNANCE_SANDBOX_SCENARIO_JSONC_REPORT_START_NOTE.md`.

If you need a compact PM reminder to validate the phase-one scenario-file/report pair before push, open `docs/GOVERNANCE_SANDBOX_PRIORITY_PAIR_VALIDATE_THEN_PUSH_NOTE.md`.

- `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_STARTER_NOTE.md` — keep scenario-file imports tied to a visible JSON/Markdown/HTML report bundle start.
