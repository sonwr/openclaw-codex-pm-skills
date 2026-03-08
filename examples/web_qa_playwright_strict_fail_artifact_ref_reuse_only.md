# Web QA Playwright — Strict-Plus artifact-ref reuse only FAIL Fixture

## 1) QA inventory
- Browser/runtime: Playwright Chromium (headless)
- Build/version under test: checkout@2026.03.08-1
- Test account: `qa.checkout@example.test`
- Deterministic replay profile: strict-plus

## Scope
- URL: `https://example.test/checkout`
- Viewport: `1440x900`
- Test account: `qa.checkout@example.test`

## 2) Checklist execution summary
- Functional checks (5/5 pass)
  - F1: PASS
  - F2: PASS
  - F3: PASS
  - F4: PASS
  - F5: PASS
- Visual checks (3/3 pass)
  - V1: PASS `artifacts/checkout/v1-cart.png`
  - V2: PASS `artifacts/checkout/v2-address.png`
  - V3: PASS `artifacts/checkout/v3-confirmation.png`
- Off-happy-path checks (2/2 pass)
  - O1: PASS
  - O2: PASS

## 3) Execution log
- F1 checkpoint: [2026-03-08T08:00:00Z] PASS (ref=checkout.login-form): Sign in with seeded QA account -> Session established and checkout flow unlocked `artifacts/checkout/f1-login.trace`
- F2 checkpoint: [2026-03-08T08:00:08Z] PASS (ref=checkout.cart-drawer): Open cart drawer -> Discount line item and subtotal render correctly `artifacts/checkout/f2-cart.trace`
- F3 checkpoint: [2026-03-08T08:00:15Z] PASS (ref=checkout.shipping-step): Submit shipping form -> Saved address advances to payment step `artifacts/checkout/f3-shipping.trace`
- F4 checkpoint: [2026-03-08T08:00:24Z] PASS (ref=checkout.payment-step): Render payment step -> Saved card radio is preselected and payable total matches summary `artifacts/checkout/shared-proof.png`
- F5 checkpoint: [2026-03-08T08:00:31Z] PASS (ref=checkout.review-step): Open review step -> Tax, shipping, and total summary remain stable `artifacts/checkout/f5-review.trace`
- V1 checkpoint: [2026-03-08T08:00:38Z] PASS (ref=checkout.cart-layout): Capture cart screenshot -> Cart line items and sidebar spacing match baseline `artifacts/checkout/v1-cart.png`
- V2 checkpoint: [2026-03-08T08:00:45Z] PASS (ref=checkout.address-layout): Capture address screenshot -> Form field spacing and CTA alignment match baseline `artifacts/checkout/v2-address.png`
- V3 checkpoint: [2026-03-08T08:00:52Z] PASS (ref=checkout.confirmation-layout): Capture confirmation screenshot -> Confirmation header and receipt card match baseline `artifacts/checkout/shared-proof.png`
- O1 checkpoint: [2026-03-08T08:00:59Z] PASS (ref=checkout.invalid-card-error): Submit invalid card -> Stay on payment step with inline card error and no navigation `artifacts/checkout/o1-invalid-card.trace`
- O2 checkpoint: [2026-03-08T08:01:07Z] PASS (ref=checkout.expired-session-modal): Force expired session -> Re-auth modal appears before order placement `artifacts/checkout/o2-session.trace`

## 4) Signoff
- Regressions: 0
- Failure breakdown: selector=0, runtime=0, product=0
- Merge recommendation: **APPROVE**
