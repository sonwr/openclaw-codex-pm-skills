from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_readme_mentions_governance_sandbox_small_slice_rule() -> None:
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')

    assert 'docs/GOVERNANCE_SANDBOX_SMALL_SLICE_RULE.md' in readme
    assert (ROOT / 'docs' / 'GOVERNANCE_SANDBOX_SMALL_SLICE_RULE.md').exists()
