import re

def analyze_subject(subject: str):
    score = 0
    issues = []

    if subject.isupper():
        score += 20
        issues.append("All caps subject")

    if "!!!" in subject:
        score += 10
        issues.append("Too many exclamation marks")

    if len(subject) > 60:
        score += 10
        issues.append("Subject too long")

    if re.search(r"[🔥🚀💰]", subject):
        score += 10
        issues.append("Emoji detected in subject")

    return min(score, 100), issues
