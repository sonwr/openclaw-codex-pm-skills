# openclaw-codex-pm-skills

A community-driven adaptation layer for applying PM skill frameworks (inspired by [phuryn/pm-skills](https://github.com/phuryn/pm-skills)) to **OpenClaw + Codex-style** workflows.

This project is designed for teams who want practical, reusable product-management skills that are:

- portable across environments,
- easy to audit,
- safe for collaborative use,
- and realistic to maintain in open source.

## Fast validation

Use the repository smoke check before proposing README, example, or validator changes:

```bash
python3 -m unittest tests/test_validate_web_qa_report.py tests/test_validate_web_qa_report_cli.py
```

This keeps documentation tweaks and validation-rule changes tied to the same replay-readiness contract.
For broader validator or fixture rewrites, run `python3 -m unittest discover -s tests` before opening the PR so the full replay-readiness surface stays green.
If the workstream touches governance-sandbox scenario files or markdown/html report proof, use `docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_PROOF_LOOP.md` before merging so scenario-input evidence and report-output evidence stay coupled.
The JSON metadata also tracks failed-check recovery owners, missing owner coverage, and next-action owner handoff readiness so triage gaps stay visible before merge.
If the validator passes with incomplete signoff coverage, use `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_MISSING_FIELDS.md` to decide whether the artifact is inspection-ready or truly handoff-ready.
If owner coverage is the real blocker after validation passes, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_GAPS.md` before calling the report handoff-ready.
If you need a compact wording note for validator-PASS artifacts that are still not governance-ready, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_GOVERNANCE_NOTE.md`.
If you need a fast last-pass gate for whether unresolved failed checks still block owner-complete handoff, open `docs/WEB_QA_PLAYWRIGHT_OWNER_GAP_EXIT_CHECK.md`.
If you need a compact owner handoff sentence after validation passes, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_HANDOFF.md`.
If you need a 30-second owner/lane/artifact context check before posting that sentence, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_CONTEXT_CHECK.md`.
If you need a 30-second owner-ready signoff brief before that fuller handoff, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_READY_BRIEF.md`.
If you need an even shorter owner-aware signoff sentence that keeps covered versus unresolved failed checks visible, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_SUMMARY_LINE.md`.
If you need a one-line owner summary before writing the fuller handoff, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_SUMMARY_LINE.md` first and expand only if unresolved checks remain.
If you need a faster owner-first cue before writing that sentence, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_CUE.md`.
If you need a compact owner-alias-safe handoff sentence that still keeps unresolved failed checks visible, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_ALIAS_TRIAGE.md`.
If you need a compact signoff-coverage decision card before handoff, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_COVERAGE_CARD.md`.
If you need a 60-second signoff-first scan before a deeper review, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_FIRST_LOOK.md`.
If you need a 60-second replay-readiness review before rerun or handoff, open `docs/WEB_QA_PLAYWRIGHT_REPLAY_READINESS_QUICKCHECK.md`.
If hotspot sections tie on replay blockers, open `docs/WEB_QA_PLAYWRIGHT_REPLAY_HOTSPOT_TIEBREAK.md` before flattening the repair lane into a single winner.
If you need a quick rule card for interpreting replay blocker totals before handoff, open `docs/WEB_QA_PLAYWRIGHT_REPLAY_BLOCKER_TOTALS.md`.
If you need a compact owner-routing checklist before handoff, open `docs/WEB_QA_PLAYWRIGHT_OWNER_TRIAGE_CARD.md`.
If you need a shortest-path sequence for turning a validator-clean blocked lane into an owner-ready signoff line, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_SEQUENCE.md`.
If you need a compact step-by-step bridge from validator PASS to a signoff-ready handoff sentence, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_HANDOFF_SEQUENCE.md`.
If you need a compact next-action wording guide before declaring handoff-ready, open `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_HANDOFF.md`.
If you need a compact signoff gate for deciding whether the next action is specific enough to call the artifact handoff-ready, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_NEXT_ACTION_GATE.md`.
If you need safer wording for PASS artifacts that still should not be called signoff-ready, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_BLOCKER_LANGUAGE.md`.
If you need a one-screen matrix for judging whether the next action already has enough target/artifact support for replay, open `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_SUPPORT_MATRIX.md`.
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
If you need a one-screen rerun-versus-repair chooser after validation already passed, open `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_RERUN_DECIDER.md`.
If you need a one-screen rule for keeping a passing report's rerun request narrow instead of drifting into a full replay, open `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_REPLAY_BOUNDARY.md`.
If you need a compact rerun-only handoff checklist after validation already passed, open `docs/WEB_QA_PLAYWRIGHT_RERUN_HANDOFF_CARD.md`.
If you need a quick artifact-specific check before calling that rerun handoff replay-ready, open `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_RERUN_ARTIFACT_CHECK.md`.
If you need a one-line rerun owner handoff after that checklist, open `docs/WEB_QA_PLAYWRIGHT_RERUN_OWNER_STATUS_LINE.md`.
If you need a slightly broader signoff-safe rerun sentence before handoff, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_RERUN_STATUS_LINE.md`.
If you need a compact pass/fail cue for whether a validator-clean artifact is truly ready for a focused rerun handoff, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_RERUN_READY_SIGNAL.md`.
If you need a one-screen rule for deciding whether replay support is strong enough to keep the rerun lane narrow, open `docs/WEB_QA_PLAYWRIGHT_REPLAY_SUPPORT_SCOPE_GATE.md`.
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
