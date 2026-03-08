---
name: web-qa-playwright
description: Run iterative web service QA using Playwright-style workflow with persistent session habits, explicit functional/visual/off-happy-path coverage, and evidence capture. Use when developing or reviewing web UI features, validating post-change behavior, and preparing merge-ready QA artifacts.
---

# Web QA Playwright

Define and execute deterministic QA before signoff.

## Execute this workflow

1. Build a QA inventory from:
   - requested requirements,
   - implemented user-facing behavior,
   - claims to include in final report.
2. Convert inventory into fixed checks:
   - Functional checks: exactly 5
   - Visual checks: exactly 3
   - Off-happy-path checks: exactly 2
3. Execute checks with Playwright-based browser flow.
   - Prefer stable selectors (role/label/test-id) over brittle CSS/XPath.
   - Validate each step before advancing (URL/state/assertion checkpoint).
4. Capture evidence:
   - screenshots for visual/critical states,
   - concise execution log for each check.
5. Report results in a structured format.
6. If a check fails, run failure recovery once:
   - decide reload vs relaunch based on change scope (renderer-only => reload, startup/runtime ownership change => relaunch),
   - re-run the same step with the same target and selectors,
   - if still failing, isolate whether issue is selector/runtime/product behavior,
   - record reproducible failure notes for handoff.

## Required output format

- Feature checks (5): pass/fail + one-line evidence
- Visual checks (3): pass/fail + screenshot references
- Off-happy checks (2): pass/fail + observed behavior
- Regression summary: explicit regression count
- Merge recommendation: allow/block with reason

## Hard gates

- Keep regression count at 0 for merge-ready status.
- If any regression exists, block merge and list exact failing checks.
- Never claim visual quality without screenshot evidence.
- Keep one browser session per run unless process ownership changed (relaunch only when needed).

## Stability and reproducibility rules

- Use deterministic preconditions (fixed URL, viewport, test account/data).
- Separate functional and visual passes; do not merge evidence streams.
- Normalize check result tokens to uppercase `PASS` or `FAIL` for parser-safe replay.
- Keep section summary ratios (`x/y pass`) consistent with detailed PASS/FAIL lines.
- Log step checkpoints for every fixed check id (F1..F5, V1..V3, O1..O2) in an execution log.
- Keep signoff `Regressions` count exactly equal to checklist `FAIL` line count.
- Keep merge recommendation consistent with regressions: `APPROVE` only when regressions are 0; otherwise `BLOCK`.
- Keep checkpoint IDs unique and reject unknown IDs to preserve deterministic replay evidence.
- If a checklist item is `FAIL`, the matching checkpoint line for that check id must also be explicitly marked `FAIL`.
- Log each failure with: step/check id, expected, observed, first failure timestamp (UTC, `YYYY-MM-DDTHH:MM:SSZ`), retry outcome, failure classification (`selector|runtime|product`), and one evidence pointer (screenshot/video/log/trace path).
- Prefer one controlled retry over repeated blind retries.

## Use the fixed template

Read and fill both templates for every QA run:
- `references/qa-inventory-template.md`
- `references/checklist-template.md`

For structure/quality baseline, mirror the reporting style in:
- `../../examples/web_qa_playwright_sample_run.md`

Optional automation guard after report generation:
- `../../scripts/validate_web_qa_report.py --file <report.md> --strict`
- `../../scripts/validate_web_qa_report.py --file <report.md> --strict --json` (CI-friendly machine output)
- `../../scripts/validate_web_qa_report.py --file <report.md> --strict --json-out artifacts/web-qa-validation.json` (persist machine output as CI artifact)
- `../../scripts/validate_web_qa_report.py --file <report.md> --strict-plus` (deterministic replay hardening preset)
- `../../scripts/validate_web_qa_report.py --file <report.md> --strict --enforce-checkpoint-format --require-checkpoint-timestamps --enforce-monotonic-checkpoint-timestamps --enforce-checkpoint-status-tokens --enforce-checkpoint-to-check-status-consistency --require-visual-checkpoint-evidence --require-checkpoint-artifact-paths --require-checkpoint-target-refs --require-failure-evidence-artifact-paths --require-failure-recovery-plan --enforce-failure-timestamp-order --require-execution-log-step-count-match` (deterministic replay hardening + timestamp ordering + normalized PASS/FAIL checkpoint traces + checklist/log status consistency + visual checkpoint screenshot proof + artifact-path traceability + stable target refs for interactive replay + failure recovery-plan enforcement + failed-check chronology consistency + exact execution-log step accounting)
