def redact_data(text, sensitive_segments):
    # Simple redaction example (replace with robust masking)
    for label, idx in sensitive_segments:
        text = text.replace(label, "[REDACTED]")
    return text
