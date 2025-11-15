def classify_sensitive_data(text):
    # Dummy sensitive data classifier (replace with spaCy/BERT code)
    results = []
    if "email" in text: results.append(("email", text.find("email")))
    if "phone" in text: results.append(("phone", text.find("phone")))
    return results
