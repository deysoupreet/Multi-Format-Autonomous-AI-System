def classify_input(filename, content):
    format = "PDF" if filename.endswith(".pdf") else "Email" if filename.endswith(".txt") else "JSON"
    # Simple keyword matching for now
    intent = "Invoice" if b"Total" in content else "Complaint" if b"issue" in content else "Unknown"
    return {
        "format": format,
        "intent": intent,
        "source": filename
    }
