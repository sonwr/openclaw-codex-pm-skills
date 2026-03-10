# Web QA Playwright owner triage card

Use this quick card when a validated report still needs a clean handoff owner summary.

## What to check first

1. Run the local smoke test:
   ```bash
   python3 -m unittest tests/test_validate_web_qa_report.py tests/test_validate_web_qa_report_cli.py
   ```
2. Confirm the JSON output includes failed checks, `recovery_owner_summary`, and next-action handoff fields.
3. Open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_MISSING_FIELDS.md` if the report passes validation but still looks incomplete for human review.

## Fast triage prompts

- Which failed checks still have no clear owner?
- Does the summary separate blocker ownership from inspection-only notes?
- Can the next operator tell who should act first without reading the full artifact?

## Ready-to-merge signal

The report is handoff-ready when blocker ownership, missing-field gaps, and next-action owner routing are all visible in the top-level summary.