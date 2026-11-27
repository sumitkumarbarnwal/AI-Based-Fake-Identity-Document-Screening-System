# Team Work Division & Ownership Matrix

## AI-Based Fake Identity Document Screening System

This document outlines the detailed breakdown of responsibilities and file-level ownership for each team member.

---

## 👥 Executive Ownership Matrix

| Team Member | Module | Responsibilities | Relevant Files |
| :--- | :--- | :--- | :--- |
| **Abhilash Jha** | **Frontend (Auth, Admin, Routing, State, Common UI)** | • Authentication UI (Login and Registration pages)<br>• Application routing, path synchronization, and navigation guards<br>• Admin panel UI, user administration, and system metrics view<br>• Frontend global state management architecture<br>• Shared/common UI components (Navbar, Footer, Sidebar, Toast system)<br>• Frontend-to-backend API integration for assigned views | `frontend/src/App.jsx`<br>`frontend/src/components/common/Navbar.jsx`<br>`frontend/src/components/common/Footer.jsx`<br>`frontend/src/components/common/Sidebar.jsx`<br>`frontend/src/components/common/Toast.jsx`<br>`frontend/src/components/auth/`<br>`frontend/src/components/admin/`<br>`frontend/src/components/dashboard/`<br>`frontend/src/store/` |
| **Shubham Kumar** | **Frontend (Landing, Upload, History, Results UI)** | • Landing/Home page layout, interactive feature showcases, and hero UI<br>• Document Upload UI, drag-and-drop file dropzone, and image preview<br>• Document History page, status badges, search bar, and filter controls<br>• Screening result inspection modal & detail audit views<br>• Client-side neural screening simulator and offline history persistence | `frontend/src/pages/HomePage.jsx`<br>`frontend/src/pages/UploadPage.jsx`<br>`frontend/src/pages/HistoryPage.jsx`<br>`frontend/src/components/home/HeroSection.jsx`<br>`frontend/src/components/home/FeatureGrid.jsx`<br>`frontend/src/components/home/DocTypesShowcase.jsx`<br>`frontend/src/components/home/HowItWorks.jsx`<br>`frontend/src/components/upload/FileDropzone.jsx`<br>`frontend/src/components/upload/DocTypeSelector.jsx`<br>`frontend/src/components/upload/ImagePreview.jsx`<br>`frontend/src/components/upload/ScreeningResultModal.jsx`<br>`frontend/src/components/history/HistoryTable.jsx`<br>`frontend/src/components/history/FilterBar.jsx`<br>`frontend/src/components/history/HistoryDetailModal.jsx`<br>`frontend/src/components/history/StatusBadge.jsx`<br>`frontend/src/components/results/`<br>`frontend/src/services/documentService.js`<br>`frontend/src/services/mockData.js` |
| **Mohit Trivedi** | **Database (MongoDB Layer)** | • **MongoDB database setup, configuration, and environment connectivity**<br>• Database architecture and NoSQL schema design<br>• Collection design, indexing strategies, and data organization<br>• Database models, data validation schemas, and consistency constraints<br>• Database integration support with FastAPI backend services<br>• Database technical documentation and query optimization | `backend/app/core/database.py`<br>`backend/app/models/user.py`<br>`backend/app/models/document.py`<br>`backend/app/models/screening_result.py`<br>`backend/.env.example`<br>`docs/WORK_DIVISION.md`<br>`docs/SETUP.md` |
| **Sumit Kumar Barnwal** | **Backend Lead / ML Developer** | • Backend architecture, configuration, and FastAPI application entrypoint<br>• Authentication and authorization backend (OAuth2, JWT tokens, bcrypt)<br>• Admin APIs for user administration and platform monitoring<br>• Secure document storage handling (local disk & S3-ready service)<br>• Deep learning forgery detection model (CNN/ViT)<br>• Machine learning pipeline orchestrator service (`ml_service.py`)<br>• Docker containerization and GitHub Actions CI infrastructure | `backend/app/main.py`<br>`backend/app/core/config.py`<br>`backend/app/core/security.py`<br>`backend/app/api/routes/auth.py`<br>`backend/app/api/routes/documents.py`<br>`backend/app/api/routes/admin.py`<br>`backend/app/services/ml_service.py`<br>`backend/app/services/storage_service.py`<br>`ml/models/forgery_detector/model.py`<br>`ml/data/preprocessing/`<br>`ml/notebooks/`<br>`docker-compose.yml`<br>`.github/workflows/ci.yml` |
| **Ansh** | **Backend / ML Developer** | • Screening APIs (analysis trigger, result retrieval, history, statistics)<br>• Document type classification model (MobileNetV3 / CLIP)<br>• OCR extraction pipeline (EasyOCR / Tesseract bilingual text reader)<br>• Field validation and algorithmic checksum verification (Verhoeff, ICAO 9303, PAN regex)<br>• Celery background task workers for asynchronous inference<br>• Backend unit testing and integration testing with pytest | `backend/app/api/routes/screening.py`<br>`backend/app/services/ocr_service.py`<br>`backend/tests/`<br>`ml/models/document_classifier/classifier.py`<br>`ml/models/ocr_pipeline/extractor.py`<br>`ml/models/ocr_pipeline/validator.py`<br>`ml/notebooks/` |

---

## 📂 Detailed File-by-File Ownership Reference

### 1. Frontend Layer (`frontend/`)

| File / Folder | Primary Owner | Description & Scope |
| :--- | :--- | :--- |
| `frontend/src/App.jsx` | **Abhilash Jha** (with Shubham Kumar) | Application shell, path/hash routing synchronization, layout mounting |
| `frontend/src/components/auth/` | **Abhilash Jha** | User login form, registration form, and protected route wrapper |
| `frontend/src/components/admin/` | **Abhilash Jha** | Admin user table, document administration, and system health status |
| `frontend/src/components/common/Navbar.jsx` | **Abhilash Jha** | Responsive navigation bar with route switching and badge counters |
| `frontend/src/components/common/Footer.jsx` | **Abhilash Jha** | Application footer with quick links and copyright information |
| `frontend/src/components/common/Sidebar.jsx` | **Abhilash Jha** | Collapsible navigation sidebar for dashboard views |
| `frontend/src/components/common/Toast.jsx` | **Abhilash Jha** | Global Toast notification provider and animated alert component |
| `frontend/src/store/` | **Abhilash Jha** | Global state management (Zustand/Redux/Context) |
| `frontend/src/components/dashboard/` | **Abhilash Jha** / Shared | Analytics cards, system usage charts, and activity feeds |
| `frontend/src/pages/HomePage.jsx` | **Shubham Kumar** | Platform showcase landing page |
| `frontend/src/pages/UploadPage.jsx` | **Shubham Kumar** | Document submission, progress bar, and instant verification page |
| `frontend/src/pages/HistoryPage.jsx` | **Shubham Kumar** | Audit log table, search filters, detail inspection, and CSV exporter |
| `frontend/src/components/home/HeroSection.jsx` | **Shubham Kumar** | Animated hero banner with quick call-to-actions |
| `frontend/src/components/home/FeatureGrid.jsx` | **Shubham Kumar** | Grid highlighting AI forgery detection, OCR, and checksum features |
| `frontend/src/components/home/DocTypesShowcase.jsx` | **Shubham Kumar** | Interactive showcase of supported Indian government IDs |
| `frontend/src/components/home/HowItWorks.jsx` | **Shubham Kumar** | 4-step interactive pipeline explainer |
| `frontend/src/components/upload/FileDropzone.jsx` | **Shubham Kumar** | Drag-and-drop file upload zone with format validation |
| `frontend/src/components/upload/DocTypeSelector.jsx` | **Shubham Kumar** | Document type selector with Auto-Detect option |
| `frontend/src/components/upload/ImagePreview.jsx` | **Shubham Kumar** | Uploaded image visual preview with remove/replace controls |
| `frontend/src/components/upload/ScreeningResultModal.jsx` | **Shubham Kumar** | Detailed modal displaying authenticity verdicts, scores, and indicators |
| `frontend/src/components/history/HistoryTable.jsx` | **Shubham Kumar** | Paginated history table with sortable columns |
| `frontend/src/components/history/FilterBar.jsx` | **Shubham Kumar** | Filter bar supporting doc type, risk level, and date range filters |
| `frontend/src/components/history/HistoryDetailModal.jsx` | **Shubham Kumar** | Modal for in-depth inspection of historical screening audits |
| `frontend/src/components/history/StatusBadge.jsx` | **Shubham Kumar** | Color-coded status badge component (Authentic/Suspicious/Fake) |
| `frontend/src/components/results/` | **Shubham Kumar** / Shared | Dedicated results presentation components |
| `frontend/src/services/documentService.js` | **Shubham Kumar** | API service layer with built-in client-side neural screening simulator |
| `frontend/src/services/mockData.js` | **Shubham Kumar** | Realistic Indian identity document mock datasets and schemas |
| `frontend/vite.config.js` | **Shubham Kumar** / Team | Vite dev server configuration and API proxy rules |
| `frontend/package.json` | **Frontend Team** | NPM package dependencies and scripts |

---

### 2. Database Layer

| File / Module | Primary Owner | Description & Scope |
| :--- | :--- | :--- |
| `backend/app/core/database.py` | **Mohit Trivedi** (Database Lead) *(with Sumit)* | MongoDB connection client, async session handling, and database initialization |
| `backend/app/models/user.py` | **Mohit Trivedi** (Database Lead) *(with Sumit)* | User account database schema, roles, and validation rules |
| `backend/app/models/document.py` | **Mohit Trivedi** (Database Lead) *(with Sumit)* | Document metadata schema, storage references, and upload status |
| `backend/app/models/screening_result.py` | **Mohit Trivedi** (Database Lead) *(with Sumit)* | ScreeningResult schema (verdicts, confidence scores, OCR fields, fraud indicators) |
| MongoDB Collections Design | **Mohit Trivedi** | NoSQL schema architecture for `users`, `documents`, `screening_results`, and `audit_logs` |
| Database Indexing & Optimization | **Mohit Trivedi** | Compound indexes, unique constraints, and query performance tuning |

> 📌 **Database Scope Clarification:**  
> Mohit Trivedi owns the MongoDB database tier. Backend business logic, API routing, authentication handlers, and machine learning orchestration remain owned by Sumit and Ansh.

---

### 3. Backend & API Layer (`backend/`)

| File / Folder | Primary Owner | Description & Scope |
| :--- | :--- | :--- |
| `backend/app/main.py` | **Sumit Kumar Barnwal** | FastAPI ASGI app initialization, CORS middleware, router registration, health endpoints |
| `backend/app/core/config.py` | **Sumit Kumar Barnwal** | Centralized application settings via Pydantic BaseSettings and `.env` parsing |
| `backend/app/core/security.py` | **Sumit Kumar Barnwal** | JWT creation/decoding, Bcrypt password hashing, OAuth2 user extraction dependencies |
| `backend/app/api/routes/auth.py` | **Sumit Kumar Barnwal** | Authentication endpoints: `/register`, `/login`, `/refresh`, and `/me` |
| `backend/app/api/routes/documents.py` | **Sumit Kumar Barnwal** | Document management endpoints: upload, list, get by ID, and delete |
| `backend/app/api/routes/admin.py` | **Sumit Kumar Barnwal** | Admin management: user list/update, document list, flagged docs, system metrics |
| `backend/app/api/routes/screening.py` | **Ansh** | Screening endpoints: `/analyze`, `/result/{id}`, `/history`, and `/stats` |
| `backend/app/services/ml_service.py` | **Sumit Kumar Barnwal** | Machine learning orchestrator connecting classification, OCR, and forgery detection |
| `backend/app/services/ocr_service.py` | **Ansh** | OCR service wrapper converting extraction outputs into structured responses |
| `backend/app/services/storage_service.py` | **Sumit Kumar Barnwal** | Local disk and S3-compatible file storage manager |
| `backend/tests/` | **Ansh** | Pytest automated test suites for routes, auth, and validation logic |
| `backend/requirements.txt` | **Sumit Kumar Barnwal** | Python backend dependency specifications |
| `backend/.env.example` | **Mohit Trivedi + Sumit** | Environment variables configuration template |

---

### 4. Machine Learning & Computer Vision (`ml/`)

| File / Folder | Primary Owner | Description & Scope |
| :--- | :--- | :--- |
| `ml/models/forgery_detector/model.py` | **Sumit Kumar Barnwal** | Deep CNN / Vision Transformer architecture for forensic image tampering detection |
| `ml/models/document_classifier/classifier.py` | **Ansh** | MobileNetV3 multi-class classifier identifying the 5 document types |
| `ml/models/ocr_pipeline/extractor.py` | **Ansh** | Bilingual EasyOCR/Tesseract text extraction tailored for Indian IDs |
| `ml/models/ocr_pipeline/validator.py` | **Ansh** | Algorithmic checksum validator (Verhoeff for Aadhaar, ICAO 9303 for Passport, PAN regex) |
| `ml/data/preprocessing/` | **Sumit Kumar Barnwal** | Image augmentation, Error Level Analysis (ELA), and contrast normalization |
| `ml/notebooks/` | **Sumit + Ansh** | Jupyter notebooks for EDA, model training, and performance benchmarking |
| `ml/requirements.txt` | **Sumit + Ansh** | PyTorch, Torchvision, EasyOCR, and computer vision dependencies |

---

### 5. DevOps & Infrastructure

| File | Primary Owner | Description & Scope |
| :--- | :--- | :--- |
| `docker-compose.yml` | **Sumit Kumar Barnwal** | Multi-container orchestration (FastAPI backend, React frontend, MongoDB/Postgres, Redis, Celery) |
| `.github/workflows/ci.yml` | **Sumit Kumar Barnwal** | GitHub Actions automated continuous integration (backend tests, frontend build) |
| `.gitignore` | **Sumit Kumar Barnwal** | Exclusions for virtual environments, node_modules, datasets, and ML weights |
