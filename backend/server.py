"""AURA FastAPI backend — same /predict contract as the old Flask app."""
import os
import time
import logging
from collections import defaultdict

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

import ml
import rag

load_dotenv()
logging.basicConfig(level=logging.INFO)

app = FastAPI(title="AURA backend")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in os.getenv("ALLOWED_ORIGINS", "*").split(",")],
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)


class SymptomsIn(BaseModel):
    symptoms: str


# Tiny per-IP rate limit — /predict can trigger paid LLM calls.
_HITS = defaultdict(list)


def _rate_ok(ip, limit=20, window=60):
    now = time.time()
    _HITS[ip] = [t for t in _HITS[ip] if now - t < window]
    if len(_HITS[ip]) >= limit:
        return False
    _HITS[ip].append(now)
    return True


@app.get("/")
def index():
    return {"status": "ok", "message": "AURA backend running"}


@app.post("/predict")
def predict(body: SymptomsIn, request: Request):
    if not _rate_ok(request.client.host if request.client else "anon"):
        raise HTTPException(429, "Too many requests, please slow down.")
    symptoms = [s.strip().lower() for s in body.symptoms.split(",") if s.strip()]
    if not symptoms:
        raise HTTPException(400, "Please provide at least one symptom.")
    results = []
    for disease, score, _ in ml.predict(symptoms, top_n=3):
        details = rag.enrich(disease, ml.context_for(disease))
        results.append({"disease": disease, "probability": f"{score * 100:.1f}%", **details})
    return results
