from __future__ import annotations

from email_template_check.models import Rule

PROJECT_NAME = 'email-template-check'
SUMMARY = (
              'Lint transactional email templates for unsafe links and missing unsubscr'
              'ibe language.'
          )
SAMPLE_RISK = 'reset password link http://example.com unsubscribe missing support none'
SAMPLE_CLEAN = (
                   'reset password link https://example.com unsubscribe included support hel'
                   'p@example.com'
               )
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='insecure-link',
        severity='high',
        pattern='http://',
        message='insecure link detected',
        recommendation='use HTTPS links',
    ),
    Rule(
        code='missing-unsubscribe',
        severity='medium',
        pattern='unsubscribe\\s+(missing|none|unknown)',
        message='unsubscribe language missing',
        recommendation='add unsubscribe where required',
    ),
    Rule(
        code='missing-support',
        severity='low',
        pattern='support\\s+(none|missing|unknown)',
        message='support contact missing',
        recommendation='add support contact',
    ),
)
