"""Public API for email-template-check."""

from email_template_check.core import audit_records, read_records
from email_template_check.models import AuditReport, Finding, Rule

__all__ = ["AuditReport", "Finding", "Rule", "audit_records", "read_records"]
__version__ = "0.1.0"
