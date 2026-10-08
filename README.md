# mint-integration-local

Public `local.sandbox.ensure_marker` reference integration for Mint.

Phases: describe, validate, observe, plan, verify, evidence. `execute` is
refused. No network, credentials, or `mint apply`.

```bash
python scripts/run_conformance.py
# After the language discovery PR is on main:
# mint integrations test --local .
```

Pin with `mint integrations add --project DIR --local mint-integration.json`.
`add` does not pip-install or execute this integration. Release Please owns
prerelease tags. This package is public preview, not 1.0.
