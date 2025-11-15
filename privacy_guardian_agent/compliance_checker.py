def check_compliance(segments):
    # Dummy rule: If more than 2 items, warn user.
    if len(segments) > 2:
        return "Warning: File contains multiple PII types."
    else:
        return "Compliant with privacy standards."
