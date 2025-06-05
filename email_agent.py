from textblob import TextBlob

def process_email(content: bytes) -> dict:
    text = content.decode("utf-8", errors="ignore")
    lines = text.splitlines()

    sender = ""
    subject = ""
    body_lines = []

    for line in lines:
        if line.lower().startswith("from:"):
            sender = line.split(":", 1)[1].strip()
        elif line.lower().startswith("subject:"):
            subject = line.split(":", 1)[1].strip()
        elif line.strip() != "":
            body_lines.append(line.strip())

    body = " ".join(body_lines)

    full_text = subject + " " + body
    blob = TextBlob(full_text)
    polarity = blob.sentiment.polarity

    # Tone classification
    if polarity < -0.3:
        tone = "angry"
    elif polarity > 0.3:
        tone = "positive"
    else:
        # Fallback: check for anger keywords if TextBlob is neutral
        anger_keywords = ["unacceptable", "angry", "furious", "complaint", "legal", "issue", "frustrated"]
        if any(word in full_text.lower() for word in anger_keywords):
            tone = "angry"
        else:
            tone = "neutral"

    # Urgency detection
    urgency_keywords = ["urgent", "immediately", "asap", "now", "important", "help", "escalate"]
    urgency = "high" if any(word in full_text.lower() for word in urgency_keywords) else "normal"

    # Action
    if tone == "angry" and urgency == "high":
        action = "escalate"
    elif tone == "angry":
        action = "follow_up"
    else:
        action = "log"

    return {
        "agent": "email_agent",
        "sender": sender,
        "subject": subject,
        "tone": tone,
        "urgency": urgency,
        "action": action,
        "polarity_score": polarity,
        "status": "completed"
    }
