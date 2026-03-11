# Governance Sandbox report.name alias note

When a governance-sandbox scenario file already carries review-ready report metadata, prefer setting `report.name` for the default `--report-dir` artifact bundle basename.

Use it when you want:
- stable JSON / Markdown / HTML filenames across reruns
- human-readable bundle names in PRs or review threads
- scenario-driven artifact naming without repeating CLI flags

Example:

```yaml
report:
  title: Treasury confidence rehearsal memo
  name: treasury-confidence-rehearsal
```

This keeps the memo title readable while the generated files stay short and replayable.
