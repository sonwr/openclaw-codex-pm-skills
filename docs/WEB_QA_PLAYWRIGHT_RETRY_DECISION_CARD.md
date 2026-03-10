# WEB_QA_PLAYWRIGHT_RETRY_DECISION_CARD

Use this card after strict validation already ran and you only need to decide whether the next move is rerun, repair, or handoff.

## Decision order

1. If required checkpoint evidence is missing, repair the report before any rerun request.
2. If failed checks already include target refs, artifact refs, and recovery owners, queue the rerun.
3. If the report is green but signoff language is vague, tighten the handoff text instead of rerunning.

## Fast output phrases

- `repair_evidence_first` — replay support is incomplete; add refs and owner handoff details first.
- `rerun_ready` — replay support is complete enough to request a focused rerun.
- `handoff_ready` — validation passed and the report can move to human signoff without another run.
