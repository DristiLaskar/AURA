# Backend rebuild — what changed

The backend was migrated from Flask to **FastAPI** and the ML layer was
reworked. The `/predict` request/response contract is **unchanged**, so the
existing frontend works without any edits.

## New layout
| File | Purpose |
|------|---------|
| `server.py` | FastAPI app (`/` and `/predict`). CORS, input validation, rate limiting. |
| `ml.py` | Data cleaning + semantic matching (Google embeddings + FAISS) with a cleaned TF-IDF fallback. Also the RAG retriever. |
| `rag.py` | LangChain RAG chain — grounds Gemini on retrieved context; disk-cached. |
| `build_index.py` | One-time FAISS index builder. |

## Key improvements
1. **Data cleaning** — ~39% of rows had scraped page boilerplate (form errors,
   newsletter/privacy text) inside the symptom lists. It's now stripped before
   anything is embedded or vectorized.
2. **Strong baseline** — TF-IDF bag-of-words replaced by **semantic search**
   (Google `embedding-001` + FAISS). Synonyms like "high temperature" ≈ "fever"
   now match. TF-IDF remains only as an offline/no-key fallback.
3. **RAG (LangChain)** — for each predicted disease, its own Mayo-Clinic-derived
   text is retrieved and passed to Gemini as grounding context, instead of Gemini
   answering from the disease name alone.
4. **Honest scores** — `probability` now reflects real similarity and is no
   longer artificially normalized to sum to 100%.
5. **Bug fixes** — CORS restricted via `ALLOWED_ORIGINS`; input validation
   (400/422); per-IP rate limit (429); enrichment cache persisted to disk
   (survives restarts); `logging` instead of `print`; FAISS index cached to disk.

## Run locally
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env          # add your GEMINI_API_KEY
python build_index.py         # one-time: builds the FAISS index (needs the key)
uvicorn server:app --host 0.0.0.0 --port 5000
```
Without a `GEMINI_API_KEY` the app still runs using the TF-IDF fallback and
returns placeholder enrichment — useful for local dev.

## Deploy (Render)
Start command:
```bash
uvicorn server:app --host 0.0.0.0 --port $PORT
```
Set `GEMINI_API_KEY` and `ALLOWED_ORIGINS` (your Vercel URL) as env vars.
