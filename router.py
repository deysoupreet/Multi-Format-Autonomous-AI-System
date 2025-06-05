from app.email_agent import process_email
from app.json_agent import process_json
from app.pdf_agent import process_pdf
import requests

def route_action(metadata, content):
    format_type = metadata["format"].lower()

    if format_type == "email":
        data = process_email(content)

        # Simulate POST if escalation needed
        if data["tone"] == "angry" and data["urgency"] == "high":
            escalate_response = requests.post("http://httpbin.org/post", json={"escalate": True})
            data["escalation_result"] = escalate_response.json()

        return data

    elif format_type == "json":
        return process_json(content)

    elif format_type == "pdf":
        return process_pdf(content)

    return {"error": "Unsupported format"}
