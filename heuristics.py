# heuristics.py
from urllib.parse import urlparse
import re

def heuristic_score_and_reasons(url: str):
    """
    Analyze the URL using simple heuristics.
    Returns a dict with score, reasons, and verdict.
    Score scale:
      0–2: Legitimate
      3–5: Suspicious
      6+: Phishing Likely
    """
    reasons = []
    score = 0

    try:
        parsed = urlparse(url)
    except Exception:
        return {"score": 0, "reasons": [("error", "Invalid URL format")], "verdict": "Invalid URL"}

    # Heuristic 1: Presence of '@'
    if "@" in url:
        score += 2
        reasons.append(("warn", "Contains '@' — may redirect to fake site"))

    # Heuristic 2: Very long URL
    if len(url) > 75:
        score += 1
        reasons.append(("warn", f"URL is long ({len(url)} chars)"))

    # Heuristic 3: HTTPS usage
    if parsed.scheme != "https":
        score += 1
        reasons.append(("warn", "Not using HTTPS"))

    # Heuristic 4: IP address in domain
    if re.match(r'\d+\.\d+\.\d+\.\d+', parsed.netloc):
        score += 2
        reasons.append(("warn", "IP address used instead of domain"))

    # Heuristic 5: Hyphen in domain
    if "-" in parsed.netloc:
        score += 1
        reasons.append(("info", "Hyphen found in domain"))

    # Final verdict
    if score >= 6:
        verdict = "Phishing Likely"
    elif 3 <= score < 6:
        verdict = "Suspicious"
    else:
        verdict = "Legitimate"

    return {"score": score, "reasons": reasons, "verdict": verdict}

