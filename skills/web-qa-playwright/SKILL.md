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
4. Capture evidence:
   - screenshots for visual/critical states,
   - concise execution log for each check.
5. Report results in a structured format.

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

## Use the fixed template

Read and fill `references/checklist-template.md` for every QA run.
