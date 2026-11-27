# REST API Specifications & Reference

## AI-Based Fake Identity Document Screening System

The backend exposes RESTful API endpoints organized under the `/api/v1` namespace.

---

## 🔐 Authentication & Identity Endpoints

> **Owner:** Sumit Kumar Barnwal  
> **Route File:** `backend/app/api/routes/auth.py`

### 1. Register User
- **Method:** `POST`
- **Path:** `/api/v1/auth/register`
- **Access:** Public
- **Request Body:**
  ```json
  {
    "email": "user@example.com",
    "username": "user123",
    "full_name": "Aditya Sharma",
    "password": "SecurePassword123"
  }
  ```
- **Response:** `201 Created`
  ```json
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "user@example.com",
    "username": "user123",
    "full_name": "Aditya Sharma",
    "role": "user",
    "is_active": true
  }
  ```

### 2. Login & Token Issue
- **Method:** `POST`
- **Path:** `/api/v1/auth/login`
- **Access:** Public
- **Content-Type:** `application/x-www-form-urlencoded`
- **Request Body:** `username=user@example.com&password=SecurePassword123`
- **Response:** `200 OK`
  ```json
  {
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIs...",
    "token_type": "bearer"
  }
  ```

### 3. Refresh Access Token
- **Method:** `POST`
- **Path:** `/api/v1/auth/refresh`
- **Request Body:**
  ```json
  {
    "refresh_token": "eyJhbGciOiJIUzI1NiIs..."
  }
  ```
- **Response:** `200 OK` (New access + refresh token pair)

### 4. Current User Profile
- **Method:** `GET`
- **Path:** `/api/v1/auth/me`
- **Headers:** `Authorization: Bearer <access_token>`
- **Response:** `200 OK` (Current user profile object)

---

## 📄 Document Management Endpoints

> **Owner:** Sumit Kumar Barnwal  
> **Route File:** `backend/app/api/routes/documents.py`

### 1. Upload Identity Document
- **Method:** `POST`
- **Path:** `/api/v1/documents/upload`
- **Content-Type:** `multipart/form-data`
- **Payload:** `file`: Binary image (JPEG/PNG/PDF)
- **Response:** `201 Created`
  ```json
  {
    "id": "doc-uuid-string",
    "original_filename": "aadhaar_sample.jpg",
    "file_size": 1542090,
    "mime_type": "image/jpeg",
    "document_type": "unknown",
    "status": "pending",
    "created_at": "2026-11-27T10:05:00Z"
  }
  ```

### 2. List User Documents
- **Method:** `GET`
- **Path:** `/api/v1/documents/?page=1&limit=10`
- **Headers:** `Authorization: Bearer <access_token>`
- **Response:** `200 OK` (Paginated list of user documents)

### 3. Delete Document
- **Method:** `DELETE`
- **Path:** `/api/v1/documents/{doc_id}`
- **Headers:** `Authorization: Bearer <access_token>`
- **Response:** `204 No Content`

---

## 🔬 Screening & ML Analysis Endpoints

> **Owner:** Ansh  
> **Route File:** `backend/app/api/routes/screening.py`

### 1. Trigger ML Analysis
- **Method:** `POST`
- **Path:** `/api/v1/screening/analyze`
- **Request Body:**
  ```json
  {
    "document_id": "doc-uuid-string"
  }
  ```
- **Response:** `200 OK` or `202 Accepted`
  ```json
  {
    "id": "result-uuid-string",
    "document_id": "doc-uuid-string",
    "verdict": "authentic",
    "confidence_score": 0.982,
    "forgery_score": 0.018,
    "ocr_validation_score": 0.995,
    "ocr_fields": {
      "name": "Rahul Sharma",
      "dob": "14/08/1992",
      "id_number": "4829 1049 8921"
    },
    "fraud_indicators": [
      { "type": "photo_tampering", "detected": false, "score": 0.02 }
    ]
  }
  ```

### 2. Get Screening Result
- **Method:** `GET`
- **Path:** `/api/v1/screening/result/{result_id}`
- **Response:** `200 OK` (Detailed result object)

### 3. User Screening History
- **Method:** `GET`
- **Path:** `/api/v1/screening/history?page=1&limit=10`
- **Response:** `200 OK` (Paginated history list)

### 4. Screening Metrics
- **Method:** `GET`
- **Path:** `/api/v1/screening/stats`
- **Response:** `200 OK` (Total screenings, authentic ratio, fraud count)

---

## 🛡️ Administrative Endpoints

> **Owner:** Sumit Kumar Barnwal  
> **Route File:** `backend/app/api/routes/admin.py`  
> **Access:** `admin` role required

### 1. List Users
- **Method:** `GET`
- **Path:** `/api/v1/admin/users?page=1&limit=20`

### 2. Update User Status / Role
- **Method:** `PATCH`
- **Path:** `/api/v1/admin/users/{user_id}`
- **Request Body:** `{"is_active": true, "role": "admin"}`

### 3. List Flagged Documents
- **Method:** `GET`
- **Path:** `/api/v1/admin/documents/flagged`
- **Description:** Returns all documents identified as `SUSPICIOUS` or `FAKE`.

### 4. System-Wide Statistics
- **Method:** `GET`
- **Path:** `/api/v1/admin/stats`
- **Response:** `200 OK`
  ```json
  {
    "total_users": 150,
    "total_documents": 1240,
    "total_screenings": 1180,
    "authentic_count": 1050,
    "suspicious_count": 85,
    "fake_count": 45,
    "fraud_rate_percent": 11.02
  }
  ```

---

## 🗄️ Database Integration Note

> **Owner:** Mohit Trivedi (Database Developer)  
> All data models and queries conform to the MongoDB schema defined in [docs/WORK_DIVISION.md](file:///docs/WORK_DIVISION.md) and maintained by Mohit Trivedi.
