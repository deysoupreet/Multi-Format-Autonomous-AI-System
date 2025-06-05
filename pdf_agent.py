import re
from tika import parser

def process_pdf(content: bytes):
    parsed = parser.from_buffer(content)
    text = parsed.get("content", "").lower()

    # print("Parsed Text:\n", text)

    flags = []
    extracted = {}

    # Extract all currency-looking values
    matches = re.findall(r"[₹$]?\s?([\d,]+\.\d{2})", text)
    currency_values = []
    for m in matches:
        try:
            currency_values.append(float(m.replace(",", "")))
        except ValueError:
            continue

    if currency_values:
        last_total = currency_values[-1]
        extracted["invoice_total"] = last_total
        if last_total > 10000:
            flags.append("High invoice total")

    # Compliance keyword check
    compliance_keywords = ["gdpr", "fda", "hipaa", "iso"]
    found = [kw.upper() for kw in compliance_keywords if kw in text]
    if found:
        flags.append(f"Compliance keyword found: {', '.join(found)}")

    return {
        "agent": "pdf_agent",
        "flags": flags,
        "extracted": extracted,
        "status": "completed"
    }


