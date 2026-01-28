import re

def analyze_body(body: str):
    score = 0
    issues = []

    links = re.findall(r'https?://\S+', body)

    if len(links) > 3:
        score += 20
        issues.append("Too many links")

    short_links = [l for l in links if "bit.ly" in l or "tinyurl" in l]

    if short_links:
        score += 15
        issues.append("Shortened URL detected")

    if body.count("!") > 5:
        score += 10
        issues.append("Too many exclamation marks")

    return min(score, 100), issues
