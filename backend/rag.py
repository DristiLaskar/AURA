"""Grounded disease enrichment via a small LangChain RAG chain.

The disease's own Mayo-Clinic-derived text is retrieved (in ml.context_for)
and passed as context, so Gemini writes advice grounded in real source text
instead of hallucinating from just the name. Results persist to disk, so the
cache survives restarts (the old in-memory dict was wiped on every restart).
"""
import os
import json
import logging
from functools import lru_cache

log = logging.getLogger("aura.rag")

CACHE_FILE = os.path.join("Databases", "enrichment_cache.json")
CHAT_MODEL = "gemini-2.5-flash"

DEFAULT = {
    "prevention": ["Consult a healthcare professional for personalized guidance."],
    "remedies": ["Rest and stay hydrated while monitoring your symptoms."],
    "specialist": "General Physician",
    "risk": "Moderate",
}


def _api_key():
    return os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")


def _load_cache():
    try:
        with open(CACHE_FILE) as f:
            return json.load(f)
    except Exception:
        return {}


def _save_cache(cache):
    try:
        with open(CACHE_FILE, "w") as f:
            json.dump(cache, f)
    except Exception as e:
        log.warning("cache write failed: %s", e)


_CACHE = _load_cache()


@lru_cache(maxsize=1)
def _chain():
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import JsonOutputParser

    llm = ChatGoogleGenerativeAI(
        model=CHAT_MODEL, google_api_key=_api_key(), temperature=0.2
    )
    prompt = ChatPromptTemplate.from_template(
        "You are a medical assistant. Using the reference context, give safe, "
        "general guidance for the condition. Reply with ONLY valid JSON (no "
        "markdown), keys exactly: prevention (3-5 short tips), remedies (2-4 "
        "safe home remedies for mild symptoms), specialist (one doctor type), "
        "risk (exactly one of Mild, Moderate, Severe).\n\n"
        "Condition: {disease}\nReference context:\n{context}\n"
    )
    return prompt | llm | JsonOutputParser()


def enrich(disease, context=""):
    """Return grounded {prevention, remedies, specialist, risk} for a disease."""
    if disease in _CACHE:
        return _CACHE[disease]
    if not _api_key():
        return DEFAULT
    try:
        data = _chain().invoke({"disease": disease, "context": (context or disease)[:2000]})
        risk = data.get("risk")
        out = {
            "prevention": list(data.get("prevention") or [])[:5] or DEFAULT["prevention"],
            "remedies": list(data.get("remedies") or [])[:4] or DEFAULT["remedies"],
            "specialist": str(data.get("specialist") or "General Physician"),
            "risk": risk if risk in ("Mild", "Moderate", "Severe") else "Moderate",
        }
    except Exception as e:
        log.warning("enrich failed for %s: %s", disease, e)
        out = DEFAULT
    _CACHE[disease] = out
    _save_cache(_CACHE)
    return out
