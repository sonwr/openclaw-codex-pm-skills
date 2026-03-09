# Playwright Interactive Execution Principles

This note adapts the core ideas from the OpenAI Playwright interactive skill into a repository-local checklist for web QA work in `openclaw-codex-pm-skills`.

Use it when a task involves browser automation, interactive validation, or replay-oriented failure triage.

## Why this exists

The existing validator and examples already enforce deterministic replay structure.
This document turns that into an explicit operating loop contributors can follow before they write or review a QA report.

## Core operating loop

1. **Stabilize the target before interacting**
   - Confirm URL, viewport, account, and known preconditions.
   - Prefer stable refs and deterministic checkpoints over visually guessed clicks.

2. **Change one thing at a time**
   - Run one intentional action.
   - Verify the UI state immediately after the action.
   - Record a checkpoint that maps action -> verification.

3. **Capture evidence at each critical branch**
   - Save the screenshot/log/trace artifact on the same step where the state changes.
   - Keep artifact refs unique so replay triage can identify the exact failing step.

4. **Treat failures as recoverable states, not just red outputs**
   - Classify the failure (`selector`, `runtime`, or `product`).
   - Record the first failure timestamp, recovery owner, and next action.
   - Preserve enough evidence for the next run to retry deterministically.

5. **Prefer replayable reports over clever summaries**
   - A useful report lets another contributor rerun the same flow without guessing.
   - If a checkpoint cannot be replayed, tighten the report before expanding coverage.

## Review heuristics

Before merging browser-QA-related changes, ask:

- Can another person replay the same flow from the report alone?
- Does every checkpoint include stable evidence and a target ref when required?
- Do failed checks clearly describe expected vs observed behavior?
- Is the next action explicit enough for the next 10-minute improvement run?

## Mapping to repository assets

- Validator: `scripts/validate_web_qa_report.py`
- Replay profile guide: `docs/WEB_QA_PLAYWRIGHT_REPLAY_PROFILE.md`
- Stability checklist: `docs/WEB_QA_PLAYWRIGHT_STABILITY_CHECKLIST.md`
- Failure handoff guide: `docs/WEB_QA_PLAYWRIGHT_FAILURE_HANDOFF.md`
- Execution loop: `docs/WEB_QA_PLAYWRIGHT_EXECUTION_LOOP.md`

## Suggested contributor habit

When changing Playwright-related validation logic:

- update or add a focused fixture,
- add a test that proves the intended replay behavior,
- run the targeted CLI/unit test slice,
- and document any new handoff rule in the relevant guide.
