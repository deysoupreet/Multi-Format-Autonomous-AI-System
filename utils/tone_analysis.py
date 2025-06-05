from textblob import TextBlob

def analyze_tone(text: str) -> str:
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity < -0.3:
        return "angry"
    elif polarity > 0.3:
        return "positive"
    else:
        return "neutral"

def detect_urgency(text: str) -> str:
    urgent_keywords = ["urgent", "immediately", "asap", "now"]
    if any(word in text.lower() for word in urgent_keywords):
        return "high"
    return "normal"
