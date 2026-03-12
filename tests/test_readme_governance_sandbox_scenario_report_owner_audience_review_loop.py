from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / 'README.md'
NOTE = ROOT / 'docs' / 'GOVERNANCE_SANDBOX_SCENARIO_REPORT_OWNER_AUDIENCE_REVIEW_LOOP.md'


def test_readme_mentions_governance_sandbox_scenario_report_owner_audience_review_loop() -> None:
    readme = README.read_text(encoding='utf-8')
    assert 'docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_OWNER_AUDIENCE_REVIEW_LOOP.md' in readme
    assert 'scenario source, owner/audience routing, and the generated JSON/Markdown/HTML bundle' in readme


def test_owner_audience_review_loop_keeps_report_bundle_scope_small() -> None:
    note = NOTE.read_text(encoding='utf-8')
    assert 'scenario source path' in note
    assert 'report owner and audience routing' in note
    assert 'generated JSON/Markdown/HTML bundle paths' in note
