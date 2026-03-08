# Sample

## Scope
- URL: `https://example.test/login`
- Viewport: `1366x768`
- Test account: `qa.user@example.test`

## 2) Checklist execution summary
- Functional checks (4/5 pass)
  - F1: PASS
  - F2: FAIL
    - Expected: Login success toast appears within 2 seconds
    - Observed: Spinner persisted for 10 seconds
    - First failure timestamp: 2026-03-07T04:10:00Z
    - Retry: FAIL
    - Evidence: `artifacts/f2-failure.png`
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
- F2 checkpoint: Inline error panel missing after submit
- F3 checkpoint: Required-field validation blocked form submit
- F4 checkpoint: Pressing Enter on password field triggered submit
- F5 checkpoint: Logout redirected to `/login`
- V1 checkpoint: Captured baseline layout screenshot
- V2 checkpoint: Captured error-state screenshot
- V3 checkpoint: Captured dashboard screenshot
- O1 checkpoint: Wrong-password path stayed on `/login`
- O2 checkpoint: Empty-password path showed client-side validation

## 4) Signoff
- Regressions: 1
- Merge recommendation: **BLOCK**
