# 🛡️ AI-Based Fake Identity Document Screening System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green?logo=fastapi)
![React](https://img.shields.io/badge/React-18-61DAFB?logo=react)
![PyTorch](https://img.shields.io/badge/PyTorch-2.3-EE4C2C?logo=pytorch)
![License](https://img.shields.io/badge/License-MIT-yellow)

**An AI-powered system to detect forged/fake Indian identity documents using Deep Learning, OCR, and rule-based validation.**

</div>

---

## 📄 Supported Documents
| Document | Fields Extracted |
|----------|-----------------|
| 🪪 Aadhaar Card | Name, DOB, Gender, Aadhaar No., Address |
| 💳 PAN Card | Name, Father's Name, DOB, PAN No. |
| 🛂 Passport | Name, Passport No., DOB, Expiry, MRZ |
| 🚗 Driving License | Name, DOB, DL No., Validity, Vehicle Class |
| 🗳️ Voter ID | Name, Relation Name, DOB, Voter ID No. |

---

## 👥 Team & Work Division

| Member | Role | Owns |
|--------|------|------|
| **Sumit Kumar Barnwal** | Team Lead · Backend Lead · ML Co-Lead | Backend core, Auth, Admin API, Storage, Forgery Detection ML, Docker/CI |
| **Ansh** | Backend Dev · ML Co-Lead | Screening API, Celery tasks, Tests, OCR pipeline, Document Classifier ML |
| **Mohit Trivedi** | Frontend Dev | Dashboard page, Results page, Charts |
| **Abhilash Jha** | Frontend Dev | Auth pages, Admin panel, Routing, State |
| **Shubham Kumar** | Frontend Dev | Landing page, Upload page, History page |

---

## 📁 Project Structure

> 📌 **Folder ownership is marked with `← [Name]`** — when you clone, go directly to your folder.

```
AI-Based-Fake-Identity-Document-Screening-System/
│
├── 📂 backend/                          ← Sumit + Ansh
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   │       ├── auth.py              ← Sumit  (Register, Login, JWT)
│   │   │       ├── documents.py         ← Sumit  (Upload, List, Delete)
│   │   │       ├── admin.py             ← Sumit  (User mgmt, System stats)
│   │   │       └── screening.py         ← Ansh   (Analyze, Results, History)
│   │   ├── core/
│   │   │   ├── config.py               ← Sumit  (All env/settings)
│   │   │   ├── security.py             ← Sumit  (JWT, bcrypt, auth dependency)
│   │   │   └── database.py             ← Sumit  (Async SQLAlchemy, get_db)
│   │   ├── models/
│   │   │   ├── user.py                 ← Sumit  (User ORM model)
│   │   │   ├── document.py             ← Sumit  (Document ORM model)
│   │   │   └── screening_result.py     ← Sumit  (ScreeningResult ORM model)
│   │   ├── services/
│   │   │   ├── ml_service.py           ← Sumit  (ML pipeline orchestrator)
│   │   │   ├── ocr_service.py          ← Ansh   (OCR wrapper for API)
│   │   │   └── storage_service.py      ← Sumit  (File save/delete, local/S3)
│   │   └── main.py                     ← Sumit  (FastAPI app, startup, CORS)
│   ├── tests/                           ← Ansh   (pytest unit + integration)
│   ├── requirements.txt
│   └── Dockerfile
│
├── 📂 ml/                               ← Sumit + Ansh
│   ├── models/
│   │   ├── forgery_detector/            ← Sumit
│   │   │   ├── model.py                (CNN/ViT architecture)
│   │   │   ├── train.py                (Training pipeline)
│   │   │   └── evaluate.py             (Metrics: AUC, F1, confusion matrix)
│   │   ├── ocr_pipeline/               ← Ansh
│   │   │   ├── extractor.py            (EasyOCR text extraction per doc type)
│   │   │   └── validator.py            (Regex + checksum field validation)
│   │   └── document_classifier/        ← Ansh
│   │       ├── classifier.py           (MobileNetV3 doc type classifier)
│   │       └── train.py                (Training script)
│   ├── data/
│   │   ├── preprocessing/              ← Sumit  (Augmentation, normalization)
│   │   └── datasets/                   (gitignored — add your own data here)
│   ├── notebooks/                       ← Sumit + Ansh
│   │   ├── exploration.ipynb
│   │   ├── model_training.ipynb
│   │   └── evaluation.ipynb
│   ├── saved_models/                    (gitignored — model weights go here)
│   └── requirements.txt
│
├── 📂 frontend/                         ← Mohit + Abhilash + Shubham
│   └── src/
│       ├── components/
│       │   ├── dashboard/              ← Mohit    (StatsCard, FraudChart, ActivityFeed)
│       │   ├── results/                ← Mohit    (ResultCard, ConfidenceGauge, FraudIndicators)
│       │   ├── auth/                   ← Abhilash (LoginForm, RegisterForm, ProtectedRoute)
│       │   ├── admin/                  ← Abhilash (UserTable, DocumentsTable, SystemStats)
│       │   ├── common/                 ← Abhilash (Navbar, Sidebar, Toast)
│       │   ├── upload/                 ← Shubham  (FileDropzone, DocTypeSelector, ImagePreview)
│       │   ├── history/                ← Shubham  (HistoryTable, StatusBadge, FilterBar)
│       │   └── home/                   ← Shubham  (HeroSection, FeatureGrid, HowItWorks)
│       ├── pages/                      (assembled from components above)
│       ├── services/                   (API calls to backend)
│       ├── store/                      ← Abhilash (Zustand/Redux state management)
│       └── utils/
│
├── 📂 docs/
│   ├── API.md                          (REST API reference)
│   ├── ML_PIPELINE.md                  (ML architecture guide)
│   ├── SETUP.md                        (Local dev setup guide)
│   └── WORK_DIVISION.md                (Full file-level ownership table)
│
├── docker-compose.yml                  ← Sumit  (Full stack: API + DB + Redis + Celery)
├── .github/workflows/ci.yml            ← Sumit  (GitHub Actions CI)
├── .gitignore
└── README.md
```

---

## 🧠 ML Pipeline Architecture

```
         📄 Document Image
               │
               ▼
  ┌─────────────────────────┐
  │   Document Classifier   │  ← Ansh  (MobileNetV3)
  │  Aadhaar/PAN/Passport/  │
  │  DL / Voter ID          │
  └─────────────────────────┘
               │
     ┌─────────┴──────────┐
     ▼                    ▼
┌──────────┐      ┌──────────────────┐
│   OCR    │      │ Forgery Detector │
│ Pipeline │      │   CNN / ViT      │
│          │      │                  │
│ • Extract│      │ • Photo tamper   │
│   fields │      │ • Text tampering │
│ • Regex  │      │ • Seal forgery   │
│   validate│     │ • Font anomaly   │
│  (Ansh)  │      │   (Sumit)        │
└──────────┘      └──────────────────┘
     │                    │
     └─────────┬──────────┘
               ▼
  ┌─────────────────────────┐
  │   Result Aggregator     │  ← Sumit  (ml_service.py)
  │  confidence_score       │
  │  verdict: authentic /   │
  │           suspicious /  │
  │           fake          │
  └─────────────────────────┘
               │
               ▼
          API Response
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 20+
- PostgreSQL 15+
- Redis 7+

### 1. Clone the repo
```bash
git clone https://github.com/sumitkumarbarnwal/AI-Based-Fake-Identity-Document-Screening-System.git
cd AI-Based-Fake-Identity-Document-Screening-System
```

### 2. Create your feature branch
```bash
# Replace <name> and <module> with yours
git checkout -b feature/<name>-<module>
# Examples:
# git checkout -b feature/sumit-backend
# git checkout -b feature/ansh-ml
# git checkout -b feature/mohit-frontend
```

### 3. Backend Setup (Sumit / Ansh)
```bash
cd backend
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac/Linux
pip install -r requirements.txt
cp .env.example .env           # fill in your DB/Redis credentials
uvicorn app.main:app --reload
```
API runs at: **http://localhost:8000**  
Swagger docs: **http://localhost:8000/docs**

### 4. ML Setup (Sumit / Ansh)
```bash
cd ml
pip install -r requirements.txt
jupyter notebook                # open notebooks/exploration.ipynb to start
```

### 5. Frontend Setup (Mohit / Abhilash / Shubham)
```bash
cd frontend
npm install
npm run dev
```
App runs at: **http://localhost:3000**

### 6. Full Stack with Docker
```bash
docker-compose up --build
```

---

## 🔀 Git Workflow

```
main  (protected — PRs only)
 └── develop  (integration branch — merge your features here)
       ├── feature/sumit-backend
       ├── feature/sumit-ml
       ├── feature/ansh-backend
       ├── feature/ansh-ml
       ├── feature/mohit-frontend
       ├── feature/abhilash-frontend
       └── feature/shubham-frontend
```

**Rules:**
- ✅ Always branch off `develop`, never `main`
- ✅ PR into `develop` when your feature is ready
- ✅ Commit format: `feat(auth): add login endpoint` / `fix(ocr): handle Hindi text`
- ❌ Never push directly to `main` or `develop`

---

## 📅 Sprint Plan

| Week | Goal |
|------|------|
| **Week 1** | Repo setup · DB schema · Auth API · ML dataset research · Frontend boilerplate |
| **Week 2** | Upload API · OCR pipeline · Document classifier · Upload UI · Auth UI |
| **Week 3** | Forgery detection model · Screening API · Dashboard UI · Results UI |
| **Week 4** | ML → API integration · Admin panel · History page |
| **Week 5** | Testing · Docker · Bug fixes |
| **Week 6** | Deployment · Docs · Final demo |

---

## 📚 API Endpoints

| Method | Endpoint | Owner | Description |
|--------|----------|-------|-------------|
| `POST` | `/api/v1/auth/register` | Sumit | Register new user |
| `POST` | `/api/v1/auth/login` | Sumit | Login, get JWT |
| `GET` | `/api/v1/auth/me` | Sumit | Current user profile |
| `POST` | `/api/v1/documents/upload` | Sumit | Upload identity document |
| `GET` | `/api/v1/documents/` | Sumit | List user's documents |
| `DELETE` | `/api/v1/documents/{id}` | Sumit | Delete document |
| `POST` | `/api/v1/screening/analyze` | Ansh | Run ML screening |
| `GET` | `/api/v1/screening/result/{id}` | Ansh | Get screening result |
| `GET` | `/api/v1/screening/history` | Ansh | Screening history |
| `GET` | `/api/v1/screening/stats` | Ansh | Dashboard statistics |
| `GET` | `/api/v1/admin/users` | Sumit | All users (admin) |
| `GET` | `/api/v1/admin/stats` | Sumit | System stats (admin) |

---

<div align="center">
Made with ❤️ by Sumit · Ansh · Mohit · Abhilash · Shubham
</div>
