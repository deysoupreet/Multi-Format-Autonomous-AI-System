import re
from tika import parser
from app.utils.logger import get_logger

logger = get_logger(__name__)

def extract_text_from_pdf(content: bytes) -> str:
    parsed = parser.from_buffer(content)
    text = parsed.get("content", "") or ""
    logger.debug(f"Extracted PDF text length: {len(text)}")
    return text.lower()

def extract_currency_values(text: str) -> list[float]:
    matches = re.findall(r"[₹$]?\s?([\d,]+\.\d{2})", text)
    currency_values = []
    for m in matches:
        try:
            value = float(m.replace(",", ""))
            currency_values.append(value)
        except ValueError:
            logger.warning(f"ValueError converting {m} to float")
            continue
    logger.debug(f"Currency values extracted: {currency_values}")
    return currency_values

def check_compliance_keywords(text: str, keywords=None) -> list[str]:
    if keywords is None:
        keywords = ["gdpr", "fda", "hipaa", "iso"]
    found = [kw.upper() for kw in keywords if kw in text]
    logger.debug(f"Compliance keywords found: {found}")
    return found
