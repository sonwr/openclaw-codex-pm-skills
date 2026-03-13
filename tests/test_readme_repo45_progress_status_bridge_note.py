from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_readme_mentions_repo45_progress_status_bridge_note() -> None:
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    assert 'docs/OPENCLAW_PM_REPO45_PROGRESS_STATUS_BRIDGE_NOTE.md' in readme
    assert (ROOT / 'docs' / 'OPENCLAW_PM_REPO45_PROGRESS_STATUS_BRIDGE_NOTE.md').exists()
