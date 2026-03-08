# Web QA Playwright — Strict Fail Fixture (Duplicate Checkpoint)

## Scope
- URL: `https://example.test/login`
- Viewport: `1366x768`
- Test account: `qa.user@example.test`

## 1) Requirement-to-check mapping
- R1 (successful login) -> F1, F2
- R2 (validation states) -> F3
- R3 (keyboard accessibility) -> F4
- R4 (logout safety) -> F5
- R5 (visual integrity) -> V1, V2, V3
- R6 (off-happy-path handling) -> O1, O2

## 2) Checklist execution summary
- Functional checks (5/5 pass)
  - F1: PASS
  - F2: PASS
  - F3: PASS
  - F4: PASS
  - F5: PASS
- Visual checks (3/3 pass)
  - V1: PASS `shots/v1.png`
  - V2: PASS `shots/v2.png`
  - V3: PASS `shots/v3.png`
- Off-happy-path checks (2/2 pass)
  - O1: PASS
  - O2: PASS

## 3) Execution log
- F1 checkpoint: URL changed to `/dashboard`, user avatar visible
- F2 checkpoint: Inline error panel rendered and focus moved to form alert
- F3 checkpoint: Required-field validation blocked form submit
- F4 checkpoint: Pressing Enter on password field triggered submit
- F5 checkpoint: Logout redirected to `/login`
- V1 checkpoint: Captured baseline layout screenshot
- V2 checkpoint: Captured error-state screenshot
- V3 checkpoint: Captured dashboard screenshot
- O1 checkpoint: Wrong-password path stayed on `/login`
- O2 checkpoint: Empty-password path showed client-side validation
- O2 checkpoint: Duplicate checkpoint line to trigger strict-mode failure

## 4) Signoff
- Regressions: 0
- Merge recommendation: **APPROVE**
