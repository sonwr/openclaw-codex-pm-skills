# Web QA Playwright — Strict-Plus Missing Artifact Paths Only FAIL Fixture

## 1) QA inventory
- Browser/runtime: Playwright Chromium (headless) | Checks: F1, F2, F3, F4, F5, V1, V2, V3, O1, O2
- Build/version under test: app@2026.03.08-2 | Checks: F1, V1, V2, V3
- Test account: `qa.user@example.test` | Checks: F1, F2, O1, O2
- Deterministic replay profile: strict-plus | Checks: F1, F2, F3, F4, F5, V1, V2, V3, O1, O2
- Planned coverage map: login success, validation recovery, and evidence capture are pre-mapped before execution | Checks: F1, F2, F3, F4, F5, V1, V2, V3, O1, O2

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
  - V1: PASS `artifacts/v1-layout.png`
  - V2: PASS `artifacts/v2-error.png`
  - V3: PASS `artifacts/v3-dashboard.png`
- Off-happy-path checks (2/2 pass)
  - O1: PASS
  - O2: PASS

## 3) Execution log
- F1 checkpoint: [2026-03-08T06:10:01Z] PASS (ref=login.submit): Click login submit -> Redirect to `/dashboard` and avatar appears `artifacts/f1.trace`
- F2 checkpoint: [2026-03-08T06:10:04Z] PASS (ref=login.error): Submit invalid password -> Inline error banner appears and form focus moves to alert `artifacts/f2.trace`
- F3 checkpoint: [2026-03-08T06:10:08Z] PASS (ref=login.required): Submit empty required field -> Client validation blocks submit with required-field message
- F4 checkpoint: [2026-03-08T06:10:12Z] PASS (ref=login.enter-key): Press Enter on password field -> Submit triggers and request is sent once `artifacts/f4.trace`
- F5 checkpoint: [2026-03-08T06:10:16Z] PASS (ref=menu.logout): Click logout menu action -> Redirect to `/login` with session cleared `artifacts/f5.trace`
- V1 checkpoint: [2026-03-08T06:10:20Z] PASS (ref=dashboard.hero): Capture dashboard baseline screenshot -> Hero/header layout matches baseline `artifacts/v1-layout.png`
- V2 checkpoint: [2026-03-08T06:10:24Z] PASS (ref=login.error-banner): Capture invalid-login screenshot -> Error banner color and spacing match baseline `artifacts/v2-error.png`
- V3 checkpoint: [2026-03-08T06:10:28Z] PASS (ref=dashboard.cards): Capture dashboard cards screenshot -> Card grid spacing and typography match baseline `artifacts/v3-dashboard.png`
- O1 checkpoint: [2026-03-08T06:10:32Z] PASS (ref=login.rate-limit): Retry wrong password path -> Stay on `/login` with throttling message after repeated failures `artifacts/o1.trace`
- O2 checkpoint: [2026-03-08T06:10:36Z] PASS (ref=login.empty-password): Submit empty password path -> Submit is blocked and password-required hint appears `artifacts/o2.trace`

## 4) Signoff
- Regressions: 0
- Failure breakdown: selector=0, runtime=0, product=0
- Merge recommendation: **APPROVE**
- Replay readiness: **READY**
