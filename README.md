# email-template-check

> Lint transactional email templates for unsafe links and missing unsubscribe language.

## Runbook Overview

Lint transactional email templates for unsafe links and missing unsubscribe language. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts email template. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
email-template-check examples/sample.txt
email-template-check examples/sample.txt --json --fail-on medium
python -m email_template_check --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `insecure-link` | high | insecure link detected |
| `missing-unsubscribe` | medium | unsubscribe language missing |
| `missing-support` | low | support contact missing |

## Validation Notes

```bash
ruff check .
pytest
python -m email_template_check --help
```

Example risky input:

```text
reset password link http://example.com unsubscribe missing support none
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
