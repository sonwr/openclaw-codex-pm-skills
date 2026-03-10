# Web QA Playwright Signoff Owner Handoff

Use this note when validation already passed, but the handoff still needs a clear owner sentence before the artifact can be called signoff-ready.

## When to use it

Open this guide when all of the following are true:

- the validator is green,
- the artifact already has replay evidence,
- owner coverage is present but still awkward to summarize,
- and the reviewer needs one compact handoff sentence.

## Owner handoff template

```text
Owner handoff: <owner> closes <scope> by checking <evidence>, then confirms <exit signal> before signoff.
```

## Minimum fields

Keep the sentence anchored to four facts:

1. named owner,
2. concrete scope,
3. evidence source,
4. exit signal.

## Good example

```text
Owner handoff: QA on-call closes checkout replay blockers by reviewing trace.zip and screenshot paths, then confirms all failed sections rerun clean before signoff.
```

## Bad example

```text
Owner handoff: Team should review and follow up later.
```

The bad version fails because it hides the owner, proof source, and exit condition.
