# 🛡️ AI-Based Fake Identity Document Screening System

An AI-powered system to detect forged/fake identity documents using Deep Learning (CNN/ViT), OCR, and rule-based validation.

## 📄 Supported Documents
- Aadhaar Card
- PAN Card
- Passport
- Driving License
- Voter ID Card

## 👥 Team

| Name | Role | Branch |
|------|------|--------|
| **Sumit Kumar Barnwal** | Team Lead · Backend Lead · ML Co-Lead | `feature/sumit-*` |
| **Ansh** | Backend Dev · ML Co-Lead | `feature/ansh-*` |
| **Mohit Trivedi** | Frontend Dev (Dashboard + Results) | `feature/mohit-frontend` |
| **Abhilash Jha** | Frontend Dev (Auth + Admin) | `feature/abhilash-frontend` |
| **Shubham Kumar** | Frontend Dev (Upload + History + Home) | `feature/shubham-frontend` |

## 🏗️ Project Structure

```
├── backend/      ← FastAPI (Sumit + Ansh)
├── ml/           ← ML Pipeline (Sumit + Ansh)
├── frontend/     ← React (Mohit + Abhilash + Shubham)
├── docs/         ← Documentation
└── docker-compose.yml
```

## 🚀 Quick Start

```bash
# Backend
cd backend && pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend
cd frontend && npm install && npm run dev

# ML Notebooks
cd ml && pip install -r requirements.txt && jupyter notebook
```

## 📚 Docs
- [API Documentation](docs/API.md)
- [ML Pipeline](docs/ML_PIPELINE.md)
- [Setup Guide](docs/SETUP.md)
- [Team Work Division](docs/WORK_DIVISION.md)
