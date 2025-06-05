import re

def extract_sender_from_email(text):
    # Simple regex to find sender email in headers
    match = re.search(r"From:\s*(.*)", text)
    return match.group(1).strip() if match else None

def extract_urgency(text):
    keywords = ["urgent", "immediately", "asap"]
    for kw in keywords:
        if kw.lower() in text.lower():
            return "high"
    return "normal"
