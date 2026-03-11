# Governance Sandbox report metadata handoff

Use this note when a governance-sandbox task already has scenario-file support and report bundle output, but the human handoff still needs a compact metadata-first reminder.

## Goal

Keep one replayable sentence visible:

- which scenario file drove the run,
- where the JSON/Markdown/HTML report bundle landed,
- and which audience or memo title the report is optimized for.

## Compact handoff shape

```text
Scenario file: <path> → Report bundle: <dir>/<basename>.json|md|html → Audience/title: <audience or title>
```

## Why this matters

- Scenario-driven report work stays reproducible.
- Humans can reopen the right artifact bundle without reading the whole log.
- Follow-up UI/demo work has one stable report anchor.

## When to use it

- after `--scenario-file` + `--report-dir` runs,
- before a browser-demo or reviewer handoff,
- when a task needs a metadata-first status line instead of a long explanation.
