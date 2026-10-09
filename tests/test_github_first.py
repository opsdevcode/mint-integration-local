from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
CI = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")

WHEEL = "sha256:591e1b3ebdd7e4f9373996e0cdeafa62d8fea39d2640ded8270ff2e59c68094d"
MANIFEST = "sha256:cde4adf9e5f4c9e0b127cd11e6e977d25857d4a72602702ffe8a57223b05100e"


def test_readme_is_github_first() -> None:
    assert "GitHub Releases are canonical" in README
    assert WHEEL in README
    assert MANIFEST in README
    assert "SHA256SUMS" in README
    assert "pip install ./" in README
    assert "pypi.org/project/mint-integration-local" not in README
    assert "not on PyPI" in README
    assert "mint apply" in README


def test_ci_verifies_recorded_github_release() -> None:
    assert "GitHub Release assets" in CI
    assert WHEEL.replace("sha256:", "") in CI
    assert "v0.2.0-alpha.1" in CI
    assert "pypi.org/project/mint-integration-local" not in CI
    assert "gh release create" not in CI
    assert "git tag" not in CI
