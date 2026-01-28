from analyzer.spam_words import detect_spam_words
from analyzer.subject_checker import analyze_subject
from analyzer.body_checker import analyze_body
from analyzer.html_checker import html_ratio

def analyze_email(subject: str, body: str):
    total_score = 0
    issues = []

    spam_score, spam_words = detect_spam_words(subject + " " + body)
    total_score += spam_score
    if spam_words:
        issues.append(f"Spam words detected: {', '.join(spam_words)}")

    subject_score, subject_issues = analyze_subject(subject)
    total_score += subject_score
    issues.extend(subject_issues)

    body_score, body_issues = analyze_body(body)
    total_score += body_score
    issues.extend(body_issues)

    html_score, html_issue = html_ratio(body)
    total_score += html_score
    if html_issue:
        issues.append(html_issue)

    final_score = min(total_score, 100)

    risk = (
        "Low Risk" if final_score <= 30 else
        "Medium Risk" if final_score <= 60 else
        "High Spam Risk"
    )

    return {
        "score": final_score,
        "risk": risk,
        "issues": issues
    }
