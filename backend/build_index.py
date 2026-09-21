"""One-time FAISS index build. Run after setting GEMINI_API_KEY:  python build_index.py"""
from dotenv import load_dotenv
load_dotenv()

import ml

if __name__ == "__main__":
    print("Index ready." if ml.build_index() else "No API key set - index not built (using TF-IDF fallback).")