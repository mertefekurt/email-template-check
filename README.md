# Email Template Check

Lint transactional email templates for unsafe links and missing unsubscribe language. In practice it is a narrow guardrail for support, sales, product analytics, and documentation hygiene: one command, a concrete report, and very little ceremony.

<img src="assets/readme-cover.svg" alt="Email Template Check cover" width="100%" />

## Review checklist

- [ ] insecure link detected (`insecure-link`, high)
- [ ] unsubscribe language missing (`missing-unsubscribe`, medium)
- [ ] support contact missing (`missing-support`, low)

## Command path

```bash
git clone https://github.com/mertefekurt/email-template-check.git
cd email-template-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
email-template-check examples/sample.txt
email-template-check examples/sample.txt --json
```

## Fixture worth keeping

```text
reset password link http://example.com unsubscribe missing support none
```

## Files I look at first

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
