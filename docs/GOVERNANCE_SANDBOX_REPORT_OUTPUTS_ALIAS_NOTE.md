# Governance Sandbox report.outputs alias note

When a governance-sandbox scenario grows beyond one default bundle, keep the authoring surface small by grouping report file targets under `report.outputs`.

PM check:
- keep one scenario file as the source of truth,
- keep one report basename for the review bundle,
- keep JSON, Markdown, and HTML paths explicit when a reviewer needs predictable artifact locations.

Suggested shape:

```yaml
report:
  outputs:
    directory: exports/bundles
    output_name: delegate-readiness-pack
    json: exports/files/delegate-readiness-pack.json
    markdown: exports/files/delegate-readiness-pack.md
    html: exports/files/delegate-readiness-pack.html
```

Use this when scenario-file replay and named report artifacts need to stay coupled in the same proof slice.
