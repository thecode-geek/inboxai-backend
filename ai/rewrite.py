import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def rewrite_email(email_body: str):
    prompt = f"""
Rewrite the following email to reduce spam risk.
Make it natural, professional and inbox-safe.
Avoid aggressive CTA and spam words.

Email:
{email_body}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content
