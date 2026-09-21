<div align="center">

# <img src="https://cdn.simpleicons.org/googleassistant" width="32" height="32"/> AURA

### AI-Driven Disease Prediction & Solution Platform

**Predict • Understand • Prevent**

A full-stack health companion that analyzes symptoms using **Machine Learning** and enriches predictions with **Google Gemini AI** to provide prevention guidance, home remedies, risk levels, and specialist recommendations.

<br/>

<a href="https://disease-predictor-tan.vercel.app/">
  <img src="https://img.shields.io/badge/Live%20Demo-Visit%20AURA-111827?style=for-the-badge&logo=vercel&logoColor=white"/>
</a>
<a href="https://github.com/manisha999404/Disease_Predictor">
  <img src="https://img.shields.io/badge/Source%20Code-GitHub-111827?style=for-the-badge&logo=github&logoColor=white"/>
</a>

<br/><br/>

<img src="https://img.shields.io/badge/React%2019-20232A?style=flat-square&logo=react&logoColor=61DAFB"/>
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"/>
<img src="https://img.shields.io/badge/Tailwind%20CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white"/>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white"/>
<img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white"/>
<img src="https://img.shields.io/badge/Google%20Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white"/>
<img src="https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white"/>
<img src="https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=111827"/>

</div>

---

## ◈ Overview

**AURA** is an AI-powered disease prediction platform designed to turn a user's symptoms into actionable health information.

The system combines a **TF-IDF + Cosine Similarity machine-learning pipeline** with **Google Gemini AI** to produce ranked disease predictions and contextual recommendations.

At the center of the experience is an interactive **AURA assistant**, rendered on HTML Canvas with cursor-tracking eyes, animated blobs, and a lightweight 30 FPS render loop.

> **Note:** AURA is intended for educational and informational purposes only. It is **not a substitute for professional medical diagnosis, treatment, or emergency care.**

---

## ◇ What Makes AURA Different?

<table>
<tr>
<td width="50%">

### ◉ Intelligent Prediction

Analyze multiple symptoms and return the **top 3 disease matches** ranked by similarity.

</td>
<td width="50%">

### ◉ AI-Powered Guidance

Gemini enriches predictions with contextual health information and recommendations.

</td>
</tr>

<tr>
<td width="50%">

### ◉ Interactive Assistant

AURA reacts to the user's cursor through a custom canvas-rendered animated character.

</td>
<td width="50%">

### ◉ Full-Stack Architecture

React frontend + Flask REST API + ML pipeline + Gemini AI deployed across Vercel and Render.

</td>
</tr>
</table>

---

# ⌁ Core Features

### 01 — Symptom-Based Disease Prediction

Users enter symptoms such as:

```text
fever, cough, fatigue
```

The backend then:

```text
User Symptoms
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Cosine Similarity
      │
      ▼
Disease-Symptom Dataset
      │
      ▼
Top 3 Predictions
```

Each prediction includes a calculated probability score.

---

### 02 — Gemini AI Health Insights

Every predicted disease is passed to the **Google Gemini API**, which generates contextual information including:

* Prevention tips
* Home remedies
* Risk level
* Recommended specialist
* Additional contextual guidance

This creates a two-stage pipeline:

```text
Machine Learning
      │
      │ Disease Prediction
      ▼
Top 3 Diseases
      │
      │ Context Enrichment
      ▼
Google Gemini
      │
      ▼
Actionable Health Information
```

---

### 03 — Interactive AURA Assistant

The frontend contains a custom animated assistant built using **HTML Canvas**.

Key interactions include:

```text
Cursor Tracking
      ↓
Eye Movement
      ↓
Animated Blob
      ↓
Ambient Background Effects
      ↓
30 FPS Optimized Rendering
```

The render loop is throttled to maintain a smooth interface while reducing unnecessary computation.

---

### 04 — Responsive Interface

Built with:

<img src="https://cdn.simpleicons.org/react" width="18"/> **React 19** <img src="https://cdn.simpleicons.org/typescript" width="18"/> **TypeScript** <img src="https://cdn.simpleicons.org/vite" width="18"/> **Vite** <img src="https://cdn.simpleicons.org/tailwindcss" width="18"/> **Tailwind CSS**

The interface adapts to both **desktop and mobile** screens.

---

### 05 — Production-Ready REST API

The Flask backend provides a simple prediction API with:

* CORS support
* Lazy model loading
* Environment-based configuration
* Gunicorn WSGI deployment
* JSON-based request/response handling

---

# ⚙ Technology Stack

<div align="center">

| Layer                | Technologies                                                                                                                                                                                                                                                                                                   |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Frontend**         | <img src="https://cdn.simpleicons.org/react" width="18"/> React 19 · <img src="https://cdn.simpleicons.org/typescript" width="18"/> TypeScript · <img src="https://cdn.simpleicons.org/vite" width="18"/> Vite · <img src="https://cdn.simpleicons.org/tailwindcss" width="18"/> Tailwind CSS · TanStack Start |
| **Backend**          | <img src="https://cdn.simpleicons.org/python" width="18"/> Python · <img src="https://cdn.simpleicons.org/flask" width="18"/> Flask · Flask-CORS · Gunicorn                                                                                                                                                    |
| **Machine Learning** | <img src="https://cdn.simpleicons.org/scikitlearn" width="18"/> Scikit-learn · TF-IDF · Cosine Similarity · <img src="https://cdn.simpleicons.org/pandas" width="18"/> Pandas                                                                                                                                  |
| **Data Processing**  | <img src="https://cdn.simpleicons.org/beautifulsoup" width="18"/> BeautifulSoup · CSV Dataset                                                                                                                                                                                                                  |
| **Generative AI**    | <img src="https://cdn.simpleicons.org/googlegemini" width="18"/> Google Gemini API                                                                                                                                                                                                                             |
| **Deployment**       | <img src="https://cdn.simpleicons.org/vercel" width="18"/> Vercel · <img src="https://cdn.simpleicons.org/render" width="18"/> Render                                                                                                                                                                          |

</div>

---

# ⌘ System Architecture

```text
                         ┌─────────────────────┐
                         │       USER          │
                         │  Enters Symptoms    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   React Frontend    │
                         │   TypeScript + UI   │
                         └──────────┬──────────┘
                                    │
                              HTTP POST
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Flask API        │
                         │     /predict        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                    ┌──────────────────────────────┐
                    │      ML Prediction Engine    │
                    │                              │
                    │   TF-IDF Vectorization       │
                    │            +                 │
                    │   Cosine Similarity          │
                    └──────────────┬───────────────┘
                                   │
                              Top 3 Diseases
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │       Google Gemini          │
                    │                              │
                    │ Prevention                   │
                    │ Home Remedies                │
                    │ Risk Level                   │
                    │ Specialist Recommendation   │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                         ┌─────────────────────┐
                         │     AURA UI         │
                         │ Prediction + Advice │
                         └─────────────────────┘
```

---

# ◫ Project Structure

```text
Disease_Predictor/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── AuraAssistant
│   │   │   ├── BackgroundEffects
│   │   │   └── UI Components
│   │   │
│   │   ├── routes/
│   │   │   └── index.tsx
│   │   │
│   │   └── lib/
│   │       ├── API helpers
│   │       └── utilities
│   │
│   └── .env
│
└── backend/
    ├── server.py
    ├── gemini_helper.py
    │
    ├── Databases/
    │   └── Disease-Symptom Datasets
    │
    ├── requirements.txt
    └── .env
```

---

# ⇢ How It Works

### Step 1 — Enter Symptoms

The user enters a natural list of symptoms through the AURA interface.

```text
"fever, cough, fatigue"
```

### Step 2 — Send Request

The frontend sends the symptoms to:

```http
POST /predict
```

### Step 3 — Vectorize Symptoms

The backend converts the symptom text into numerical vectors using **TF-IDF**.

### Step 4 — Calculate Similarity

The input vector is compared against disease-symptom records using:

```text
Cosine Similarity
```

### Step 5 — Rank Predictions

The system selects the **top 3 matching diseases** and calculates their similarity-based probability scores.

### Step 6 — Enrich With Gemini

Each prediction is passed to Gemini to generate:

```text
Prevention
Home Remedies
Risk Level
Specialist Type
```

### Step 7 — Display Results

The final information is presented through the AURA interface alongside the animated assistant.

---

# ⇄ API Reference

## `POST /predict`

### Request

```json
{
  "symptoms": "fever, cough, fatigue"
}
```

### Response

```json
[
  {
    "disease": "Influenza",
    "probability": "78.3%",
    "risk": "Moderate",
    "prevention": [
      "Stay hydrated",
      "Rest adequately"
    ],
    "remedies": [
      "Ginger tea",
      "Steam inhalation"
    ],
    "specialist": "General Physician"
  }
]
```

---

# ⌬ Deployment

| Service                                                               | Responsibility   | Configuration               |
| --------------------------------------------------------------------- | ---------------- | --------------------------- |
| <img src="https://cdn.simpleicons.org/vercel" width="18"/> **Vercel** | Frontend hosting | `FLASK_API_URL`             |
| <img src="https://cdn.simpleicons.org/render" width="18"/> **Render** | Backend hosting  | `GEMINI_API_KEY` + Gunicorn |

### Production Flow

```text
                    Internet
                       │
                       ▼
              ┌────────────────┐
              │     Vercel     │
              │ React Frontend │
              └───────┬────────┘
                      │
                      ▼
              ┌────────────────┐
              │     Render     │
              │  Flask + ML    │
              └───────┬────────┘
                      │
              ┌───────┴────────┐
              ▼                ▼
        ML Prediction      Gemini API
```

---

# ▶ Getting Started

## Prerequisites

* **Node.js 18+**
* **Python 3.10+**
* Google Gemini API key

---

## Backend Setup

```bash
cd backend

pip install -r requirements.txt

# Create .env
echo "GEMINI_API_KEY=your_key_here" > .env

uvicorn server:app --host 0.0.0.0 --port 5000
```

Backend:

```text
http://127.0.0.1:5000
```

---

## Frontend Setup

```bash
cd frontend

npm install

# Create .env
echo "FLASK_API_URL=http://127.0.0.1:5000" > .env

npm run dev
```

Frontend:

```text
http://localhost:3000
```

---

# ◈ Example

### Input

```text
Fever
Cough
Fatigue
```

### AURA Pipeline

```text
Symptoms
   ↓
TF-IDF
   ↓
Cosine Similarity
   ↓
Top 3 Disease Predictions
   ↓
Gemini AI
   ↓
Prevention + Remedies + Risk + Specialist
```

### Output

```text
Influenza
Probability: 78.3%
Risk: Moderate

Prevention:
• Stay hydrated
• Rest adequately

Home Remedies:
• Ginger tea
• Steam inhalation

Specialist:
General Physician
```

---

# ◇ Future Scope

Potential extensions for AURA include:

```text
Voice-based symptom input
        ↓
Multi-language support
        ↓
Medical knowledge retrieval
        ↓
Personalized health history
        ↓
Symptom timeline tracking
        ↓
Doctor / specialist discovery
        ↓
Wearable health-data integration
```

---

# ⊙ Contributing

Contributions, suggestions, and improvements are welcome.

```bash
git clone https://github.com/manisha999404/Disease_Predictor.git
cd Disease_Predictor
```

Create a feature branch, make your changes, and submit a pull request.

---

# ▣ Project Links

<div align="center">

<a href="https://disease-predictor-tan.vercel.app/">
  <img src="https://img.shields.io/badge/%E2%96%B6%20LIVE%20DEMO-111827?style=for-the-badge"/>
</a>

<a href="https://github.com/manisha999404/Disease_Predictor">
  <img src="https://img.shields.io/badge/%E2%8C%98%20GITHUB%20REPOSITORY-111827?style=for-the-badge&logo=github&logoColor=white"/>
</a>

</div>

---

<div align="center">

### Built with React, Python, Machine Learning & Gemini

**AURA — Turning symptoms into understandable health insights.**

</div>
