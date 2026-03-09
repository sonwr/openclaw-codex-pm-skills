# Web QA Playwright Precheck

A short pre-run checklist for interactive browser QA before the first click.

This note translates the repository's Playwright-interactive principles into a **1-minute precheck** that helps operators avoid unstable runs and produce reproducible evidence.

## Why this exists

Interactive browser QA often fails *before* the actual product check starts:

- the wrong profile/tab gets attached,
- refs are regenerated mid-run,
- baseline context is not captured,
- evidence paths are invented after failure,
- or reruns start without a clear recovery owner.

A lightweight precheck reduces those avoidable failures.

## 1-minute precheck

1. **Freeze the environment**
   - confirm target URL, environment, account, and feature flag state
   - note the browser profile / relay mode you intend to use
2. **Capture stable selectors/refs early**
   - take the first snapshot before interacting
   - reuse the same target/tab whenever possible
3. **Declare the evidence route**
   - decide where screenshots, logs, traces, or HAR files will be written
   - keep artifact names deterministic enough for a rerun to match them
4. **Verify the first step before chaining more**
   - do one action, then confirm the expected UI state
   - prefer small state transitions over long unverified scripts
5. **Prepare failure ownership**
   - if the run blocks, assign the next action and recovery owner immediately
   - distinguish selector/runtime/product failures before escalating

## Precheck prompts

Use these prompts before execution:

- What exact page/state am I validating first?
- Which browser/tab/profile must stay stable for this run?
- What evidence file(s) will prove the result?
- What is the first observable success signal?
- If this step fails, who owns the next recovery action?

## Recommended pairing

- Detailed replay contract: `docs/WEB_QA_PLAYWRIGHT_REPLAY_PROFILE.md`
- Failure handoff rules: `docs/WEB_QA_PLAYWRIGHT_FAILURE_HANDOFF.md`
- Machine-readable artifact routing: `docs/WEB_QA_PLAYWRIGHT_JSON_HANDOFF.md`
- Fast rerun checklist: `docs/WEB_QA_PLAYWRIGHT_STABILITY_CHECKLIST.md`
- Loop-oriented execution flow: `docs/WEB_QA_PLAYWRIGHT_EXECUTION_LOOP.md`

## One-line rule

**Before interactive QA starts, freeze profile + target + evidence path + first verification signal.**
