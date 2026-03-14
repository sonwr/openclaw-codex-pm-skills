# Governance Sandbox web UI UX + Playwright bridge note

When repo 5 work moves from scenario-file/report-first CLI slices into a web demo, keep the handoff disciplined:

- Apply UI/UX-first structure before widening flows: intro-first framing, one primary form, one clear result card.
- Keep Playwright proof limited to one stable replay path: load scenario input -> submit once -> review one result card.
- Treat JSON/YAML scenario-file support and Markdown/HTML report artifacts as the first believable proof before adding wider browser automation.
- If browser validation flakes, recover by replaying the smallest deterministic path instead of widening selectors or page coverage.
- Short five-repo reports should keep repo 4 and repo 5 visible as a paired lane: preset/web-demo support in repo 4, scenario/report support in repo 5.
