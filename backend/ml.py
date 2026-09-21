"""Symptom -> disease matching.

Strong baseline: semantic search over Google embeddings + a FAISS index.
Fallback: cleaned TF-IDF + cosine, so the app still runs without an API key
(and can be tested offline). The FAISS store also serves as the RAG retriever.
"""
import os
import re
import logging
from ast import literal_eval
from functools import lru_cache

import pandas as pd

log = logging.getLogger("aura.ml")

DATA_CSV = os.path.join("Databases", "final_diseases_with_symptoms_enhanced.csv")
INDEX_DIR = os.path.join("Databases", "faiss_index")
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"  # local, no API quota


def _api_key():
    return os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")


# Sentences that are scraped page-chrome (forms, newsletters, privacy notices),
# not symptoms. ~39% of rows contained this noise and it poisoned the vocabulary.
_JUNK = re.compile(
    r"problem with|information submitted|review/update|sign up|unsubscribe|"
    r"email field|valid email|privacy practices|mayo clinic|newsletter|"
    r"receive the latest|opt out|we use the data|try again|errorinclude|erroremail",
    re.I,
)


def _clean(symptoms):
    """Keep short symptom-like lines; drop boilerplate, headers and paragraphs."""
    out, seen = [], set()
    for s in symptoms:
        s = re.sub(r"\s+", " ", str(s)).strip()
        if not s or _JUNK.search(s):
            continue
        if s.endswith(":"):            # section headers ("Symptoms may include:")
            continue
        if len(s.split()) > 25:        # long narrative = description, not a symptom
            continue
        if not re.search(r"[a-zA-Z]", s):
            continue
        s = s.rstrip(".").lower()
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out


@lru_cache(maxsize=1)
def _frame():
    df = pd.read_csv(DATA_CSV)
    df["Symptoms"] = df["Symptoms"].apply(
        lambda x: literal_eval(x) if isinstance(x, str) else []
    )
    df["clean"] = df["Symptoms"].apply(_clean)
    df["text"] = df.apply(
        lambda r: f"{r['Disease Name']}. symptoms: " + "; ".join(r["clean"]), axis=1
    )
    return df.reset_index(drop=True)


def documents():
    """One LangChain Document per disease — powers the vector store and RAG."""
    from langchain_core.documents import Document

    return [
        Document(
            page_content=r["text"],
            metadata={
                "disease": r["Disease Name"],
                "url": r.get("URL", ""),
                "is_rare": int(r.get("IsRare", 0) or 0),
            },
        )
        for _, r in _frame().iterrows()
    ]


@lru_cache(maxsize=1)
def _store():
    """Load/build the local FAISS index. TF-IDF fallback if embeddings unavailable."""
    try:
        from langchain_community.vectorstores import FAISS
        from langchain_huggingface import HuggingFaceEmbeddings

        emb = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    except Exception as e:
        log.warning("local embeddings unavailable, using TF-IDF fallback: %s", e)
        return None
    if os.path.isdir(INDEX_DIR):
        return FAISS.load_local(INDEX_DIR, emb, allow_dangerous_deserialization=True)
    log.info("Building FAISS index (first run, one-time)...")
    store = FAISS.from_documents(documents(), emb)
    store.save_local(INDEX_DIR)
    return store


@lru_cache(maxsize=1)
def _tfidf():
    from sklearn.feature_extraction.text import TfidfVectorizer

    vec = TfidfVectorizer()
    mat = vec.fit_transform(_frame()["text"])
    return vec, mat


def build_index():
    """Explicit one-time build (used by build_index.py)."""
    _store.cache_clear()
    return _store() is not None


def predict(symptoms, top_n=3):
    """Return [(disease, score in 0..1, is_rare)] best matches."""
    query = ", ".join(symptoms)
    store = _store()
    if store is not None:
        hits = store.similarity_search_with_score(query, k=top_n)  # (doc, L2 dist)
        return [
            (d.metadata["disease"], 1.0 / (1.0 + float(dist)), d.metadata.get("is_rare", 0))
            for d, dist in hits
        ]
    # Fallback: cleaned TF-IDF + cosine
    from sklearn.metrics.pairwise import cosine_similarity

    df, (vec, mat) = _frame(), _tfidf()
    sims = cosine_similarity(vec.transform([query]), mat).flatten()
    idx = sims.argsort()[::-1][:top_n]
    return [
        (df.iloc[i]["Disease Name"], float(sims[i]), int(df.iloc[i].get("IsRare", 0) or 0))
        for i in idx
    ]


def context_for(disease):
    """RAG retrieval step: grounding text for a disease."""
    store = _store()
    if store is not None:
        docs = store.similarity_search(disease, k=1)
        if docs:
            return docs[0].page_content
    df = _frame()
    row = df[df["Disease Name"] == disease]
    return row.iloc[0]["text"] if len(row) else disease
