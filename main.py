import os
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from analyzer.score_engine import analyze_email
from ai.rewrite import rewrite_email
from openai import OpenAI


load_dotenv()  # loads .env

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not set")

client = OpenAI(api_key=api_key)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
