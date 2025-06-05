import json
from datetime import datetime

REQUIRED_FIELDS = {
    "event_type": str,
    "amount": int,
    "currency": str,
    "timestamp": str
}


def process_json(content: bytes):
    anomalies = []

    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        return {"valid": False, "anomalies": ["Invalid JSON format"]}

    for key, expected_type in REQUIRED_FIELDS.items():
        if key not in data:
            anomalies.append(f"Missing field: {key}")
        else:
            if not isinstance(data[key], expected_type):
                anomalies.append(
                    f"Incorrect type for {key}: Expected {expected_type.__name__}, got {type(data[key]).__name__}")

    # Extra validations
    if "amount" in data and isinstance(data["amount"], (int, float)) and data["amount"] <= 0:
        anomalies.append("Amount must be greater than 0")

    if "timestamp" in data:
        try:
            datetime.fromisoformat(data["timestamp"].replace("Z", "+00:00"))
        except ValueError:
            anomalies.append("Invalid timestamp format")

    return {
        "valid": len(anomalies) == 0,
        "anomalies": anomalies
    }
