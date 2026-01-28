from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from analyzer.score_engine import analyze_email
from ai.rewrite import rewrite_email

app = FastAPI(title="InboxAI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://inboxai.space",
        "https://www.inboxai.space"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "InboxAI backend running"}

@app.post("/analyze")
def analyze(data: dict):
    subject = data.get("subject", "")
    body = data.get("body", "")

    result = analyze_email(subject, body)
    return result

@app.post("/rewrite")
def rewrite(data: dict):
    body = data.get("body", "")
    rewritten = rewrite_email(body)

    return {"rewritten_email": rewritten}
