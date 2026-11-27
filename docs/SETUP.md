# Local Development Setup Guide

## AI-Based Fake Identity Document Screening System

This guide outlines how to set up, configure, and run each service in the repository locally.

---

## 📋 Prerequisites

Before getting started, make sure you have the following installed on your machine:

- **Python 3.11+**
- **Node.js 18+ or 20+ LTS** (with `npm`)
- **MongoDB 6.0+** (Local Community Server or MongoDB Atlas cluster)
- **Redis 7.0+** (Optional, required for background Celery tasks)
- **Docker & Docker Compose** (Optional, for containerized run)
- **Git**

---

## 📁 Repository Setup

```bash
git clone https://github.com/sumitkumarbarnwal/AI-Based-Fake-Identity-Document-Screening-System.git
cd AI-Based-Fake-Identity-Document-Screening-System
```

---

## ⚙️ 1. Backend Setup

> **Owners:** Sumit Kumar Barnwal (Core/Auth/Storage) & Ansh (Screening/Tests) & Mohit Trivedi (Database)

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   # Windows (PowerShell)
   python -m venv venv
   .\venv\Scripts\Activate.ps1

   # Linux / macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   ```bash
   cp .env.example .env
   ```
   Open `.env` and verify your MongoDB URI and application secrets:
   ```env
   APP_NAME="AI Fake Document Screening System"
   SECRET_KEY="your-secret-key-here"
   MONGODB_URI="mongodb://localhost:27017"
   MONGODB_DB_NAME="screening_db"
   ```

5. Launch the FastAPI development server:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
   - API endpoints: `http://localhost:8000`
   - Interactive Swagger docs: `http://localhost:8000/docs`
   - ReDoc alternative docs: `http://localhost:8000/redoc`

---

## 🗄️ 2. Database Setup (MongoDB)

> **Owner:** Mohit Trivedi (Database Developer)

1. **Option A: Local MongoDB Community Service**
   Ensure MongoDB service is running:
   ```bash
   # Linux (systemd)
   sudo systemctl status mongod
   sudo systemctl start mongod

   # Windows
   net start MongoDB
   ```

2. **Option B: MongoDB via Docker**
   ```bash
   docker run -d --name mongodb -p 27017:27017 -e MONGO_INITDB_DATABASE=screening_db mongo:6.0
   ```

3. **Option C: MongoDB Atlas (Cloud)**
   - Create a free cluster on [MongoDB Atlas](https://www.mongodb.com/atlas).
   - Obtain your connection URI and place it in `backend/.env`:
     ```env
     MONGODB_URI="mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority"
     MONGODB_DB_NAME="screening_db"
     ```

---

## 🎨 3. Frontend Setup

> **Owners:** Abhilash Jha (Auth/Admin/Routing/Common) & Shubham Kumar (Home/Upload/History/Services)

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Launch the Vite development server:
   ```bash
   npm run dev
   ```
   - Access the web interface at: `http://localhost:3000`

> 💡 **Client Simulation Mode:**  
> If the backend is not running, the frontend automatically activates a high-fidelity client-side neural screening simulator in `frontend/src/services/documentService.js`. You can upload and test all document workflows without needing the backend or ML server online!

---

## 🧠 4. Machine Learning & OCR Setup

> **Owners:** Sumit Kumar Barnwal (Forgery Model) & Ansh (Classifier & OCR Pipeline)

1. Navigate to the `ml/` directory:
   ```bash
   cd ml
   ```

2. Activate your virtual environment and install ML requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch Jupyter for exploration and model training:
   ```bash
   jupyter notebook
   ```

---

## 🐳 5. Full Stack Run via Docker Compose

> **Owner:** Sumit Kumar Barnwal

To spin up the entire ecosystem in one command:
```bash
docker-compose up --build
```
This starts:
- `backend` on `http://localhost:8000`
- `frontend` on `http://localhost:3000`
- `db` on `localhost:5432` / `mongodb` on `localhost:27017`
- `redis` on `localhost:6379`
- `celery_worker` for background asynchronous ML processing

To stop the containers:
```bash
docker-compose down
```

---

## 🧪 6. Running Tests

```bash
# Backend unit & integration tests
cd backend
pytest tests/ -v

# Frontend production build validation
cd frontend
npm run build
```
