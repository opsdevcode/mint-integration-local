# mint-integration-local

Public `local.sandbox.ensure_marker` reference integration for Mint.

Phases: describe, validate, observe, plan, verify, evidence. `execute` is
refused. No network, credentials, or `mint apply`.

```bash
python scripts/run_conformance.py
mint integrations test --local .
```

GitHub Releases are canonical. This version is not on PyPI. There is no
`latest` tag and no PyPI token. Download the immutable prerelease, check
`SHA256SUMS`, then install the local wheel:

```bash
curl -fsSL -O https://github.com/opsdevcode/mint-integration-local/releases/download/v0.2.0-alpha.1/SHA256SUMS
curl -fsSL -O https://github.com/opsdevcode/mint-integration-local/releases/download/v0.2.0-alpha.1/mint_integration_local-0.2.0a1-py3-none-any.whl
shasum -a 256 -c SHA256SUMS
pip install ./mint_integration_local-0.2.0a1-py3-none-any.whl
```

Recorded wheel digest
`sha256:591e1b3ebdd7e4f9373996e0cdeafa62d8fea39d2640ded8270ff2e59c68094d`.
Tagged `mint-integration.json` digest
`sha256:cde4adf9e5f4c9e0b127cd11e6e977d25857d4a72602702ffe8a57223b05100e`.

Pin with `mint integrations add --project DIR --local mint-integration.json`.
`add` does not pip-install or execute this integration. Release Please owns
prerelease tags. Public preview, not 1.0.

GitHub Releases are canonical (`opsdevcode.release/v0`). PyPI publication stays deferred.
