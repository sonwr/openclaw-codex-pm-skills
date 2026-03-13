# Repo 4 + Repo 5 phase-one validation command note

Keep repo 4 and repo 5 active together on every pass while governance-sandbox stays anchored to scenario-file input plus generated report artifacts.

The smallest believable repo-4/repo-5 pair is:

1. update one repo-4 preset or handoff artifact that keeps the same governance web-demo lane readable,
2. rerun one repo-5 scenario-file input plus generated report artifacts proof,
3. only then write the short five-line status with repo 4 plus repo 5 visible on every pass.

Recommended validation-first handoff:

```bash
python3 -m unittest tests/test_validate_web_qa_report.py tests/test_validate_web_qa_report_cli.py
```

Use this note when you want one PM-facing reminder that the repo-4/repo-5 phase-one pair still ends at validation before commit/push.
