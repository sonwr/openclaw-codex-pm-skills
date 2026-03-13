# Governance sandbox report downloads alias PM note

When governance-sandbox is in the scenario-file -> report-bundle phase, treat `report.outputs.downloads` as the same proof surface as `report.outputs.files` for JSON/Markdown/HTML artifacts.

PM loop:

1. validate the smallest scenario replay
2. confirm the generated download paths are still explicit
3. only then widen any web-demo or result-card copy

This keeps report-generation work aligned with download-oriented UI handoffs without skipping validation.
