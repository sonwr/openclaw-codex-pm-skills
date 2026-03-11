# governance-sandbox playwright artifact stability note

Keep the first browser-proof slice narrow and reproducible: one scenario input, one rendered result card, and one report bundle that can be regenerated without guessing hidden state.

## PM rule

- Reuse the same scenario file when replaying a flaky checkpoint.
- Keep the browser checkpoint tied to the same JSON/Markdown/HTML report bundle.
- If the browser proof drifts, recover the deterministic scenario/report path first, then rerun the UI checkpoint.
- Prefer one stable pass with visible artifacts over a wider but flaky demo sweep.
