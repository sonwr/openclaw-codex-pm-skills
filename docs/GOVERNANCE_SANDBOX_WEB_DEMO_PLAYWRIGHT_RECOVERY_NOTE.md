# Governance sandbox web demo Playwright recovery note

Keep the first governance-sandbox web demo narrow and replayable: one stable scenario form, one obvious simulate action, and one result-card state that can be recovered after a failure.

- Prefer one canonical scenario fixture before adding alternate entry paths.
- Keep visible output proof limited to the recommendation, stakeholder mix, and report export targets.
- Re-run the same browser steps after each UI change so failure recovery stays reproducible.
- Treat selector drift, runtime flakiness, and product regressions as separate recovery lanes in the demo QA log.
