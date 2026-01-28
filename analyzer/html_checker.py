import re

def html_ratio(body: str):
    html_tags = re.findall(r"<[^>]+>", body)
    text_only = re.sub(r"<[^>]+>", "", body)

    if not body.strip():
        return 0, "Empty email body"

    ratio = len("".join(html_tags)) / max(len(body), 1)

    if ratio > 0.7:
        return 20, "High HTML to text ratio"

    return 0, None
