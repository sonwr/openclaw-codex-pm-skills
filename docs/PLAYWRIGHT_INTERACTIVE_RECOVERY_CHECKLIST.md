# Playwright interactive recovery checklist

Use this when one browser-proof checkpoint fails and you need the smallest stable recovery loop.

1. Freeze the scope to one preset, one page, and one failing checkpoint.
2. Re-run only that checkpoint before touching later steps.
3. Restore the missing artifact (screenshot, HTML, trace, or note) before retrying the wider flow.
4. Confirm the repaired checkpoint passes once in isolation.
5. Resume the next checkpoint only after the repaired state is reproducible.
