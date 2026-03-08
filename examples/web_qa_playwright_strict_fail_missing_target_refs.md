# Web QA Playwright Strict-Plus Missing Target Refs Only Fixture

## 1) QA inventory
- Claim: Valid login reaches dashboard -> Checks: F1, F4
- Claim: Validation errors stay on login -> Checks: F2, F3, O1, O2
- Claim: Visual coverage captures baseline, error, and dashboard states -> Checks: V1, V2, V3
- Tooling: Playwright interactive run with deterministic replay policy

## Scope
- URL: `https://example.test/login`
- Viewport: `1366x768`
- Test account: `qa.user@example.test`

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
- F1 checkpoint: PASS - Submit valid credentials -> URL changed to `/dashboard` and user avatar visible @ 2026-03-07T05:00:01Z `artifacts/f1.log`
- F2 checkpoint: PASS - Submit invalid credentials -> inline error panel rendered and focus moved to form alert @ 2026-03-07T05:00:02Z `artifacts/f2.log`
- F3 checkpoint: PASS - Submit empty required fields -> required-field validation blocked form submit @ 2026-03-07T05:00:03Z `artifacts/f3.log`
- F4 checkpoint: PASS - Press Enter on password field -> submit triggered @ 2026-03-07T05:00:04Z `artifacts/f4.log`
- F5 checkpoint: PASS - Click logout -> redirected to `/login` @ 2026-03-07T05:00:05Z `artifacts/f5.log`
- V1 checkpoint: PASS - Capture baseline layout screenshot -> image stored in artifacts @ 2026-03-07T05:00:06Z `shots/v1.png`
- V2 checkpoint: PASS - Capture error-state screenshot -> image stored in artifacts @ 2026-03-07T05:00:07Z `shots/v2.png`
- V3 checkpoint: PASS - Capture dashboard screenshot -> image stored in artifacts @ 2026-03-07T05:00:08Z `shots/v3.png`
- O1 checkpoint: PASS - Submit wrong password -> stayed on `/login` @ 2026-03-07T05:00:09Z `artifacts/o1.trace`
- O2 checkpoint: PASS - Submit empty password -> client-side validation shown @ 2026-03-07T05:00:10Z `artifacts/o2.trace`

## 4) Signoff
- Regressions: 0
- Merge recommendation: **APPROVE**
- Replay readiness: **READY**
- Failure breakdown: selector=0, runtime=0, product=0
