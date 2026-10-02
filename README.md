<h1 align="center">AI-Based Fake Identity &amp; Document Screening System</h1>

<p align="center">
  <strong>AI-Powered Document Intelligence, Forgery Detection &amp; Identity Consistency Screening</strong>
</p>

<p align="center">
  A 6-month Major Capstone Project combining OCR, computer vision, image forensics, machine learning,
  anomaly detection, and explainable risk assessment to support preliminary screening of identity documents.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-Planned-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/OpenCV-Planned-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV"/>
  <img src="https://img.shields.io/badge/OCR-Planned-FF6F00?style=for-the-badge" alt="OCR"/>
  <img src="https://img.shields.io/badge/Machine%20Learning-Planned-F7931E?style=for-the-badge" alt="ML"/>
  <img src="https://img.shields.io/badge/PostgreSQL-Planned-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
  <img src="https://img.shields.io/badge/Docker-Planned-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
  <img src="https://img.shields.io/badge/Status-In%20Development-yellow?style=for-the-badge" alt="Status"/>
  <img src="https://img.shields.io/badge/License-Not%20Yet%20Specified-lightgrey?style=for-the-badge" alt="License"/>
</p>

<p align="center">
  <a href="https://github.com/sumitkumarbarnwal/AI-Based-Fake-Identity-Document-Screening-System">
    <strong>GitHub Repository</strong>
  </a>
</p>

---

> **Repository Status:** This repository was initialized on 17 September 2026 and is currently in the early development and planning phase. All features described in this document are **planned** unless explicitly marked otherwise. This README accurately documents the proposed architecture, verified research foundation, and development roadmap.

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Problem Statement](#2-problem-statement)
3. [Project Objectives](#3-project-objectives)
4. [Key Features](#4-key-features)
5. [System Workflow](#5-system-workflow)
6. [Important Fraud Scenario](#6-important-fraud-scenario)
7. [Types of Anomalies](#7-types-of-anomalies)
8. [AI / ML Architecture](#8-ai--ml-architecture)
9. [Research and Literature Foundation](#9-research-and-literature-foundation)
10. [Research Gap](#10-research-gap)
11. [Dataset Strategy](#11-dataset-strategy)
12. [System Architecture](#12-system-architecture)
13. [Technology Stack](#13-technology-stack)
14. [Project Structure](#14-project-structure)
15. [Installation](#15-installation)
16. [Environment Variables](#16-environment-variables)
17. [API Documentation](#17-api-documentation)
18. [Database Design](#18-database-design)
19. [Screenshots](#19-screenshots)
20. [Testing Strategy](#20-testing-strategy)
21. [Model Evaluation](#21-model-evaluation)
22. [Security and Privacy](#22-security-and-privacy)
23. [Limitations](#23-limitations)
24. [Roadmap](#24-roadmap)
25. [Responsible AI Disclaimer](#25-responsible-ai-disclaimer)
26. [Contributing](#26-contributing)
27. [License](#27-license)
28. [Author](#28-author)

---

## 1. Project Overview

The **AI-Based Fake Identity and Document Screening System** is a 6-month capstone project designed to explore and implement an AI-driven pipeline for the preliminary screening of identity documents. The proposed system aims to detect potential manipulation, forgery, or identity inconsistencies in submitted documents by combining multiple complementary techniques:

| Technique | Role |
|---|---|
| **OCR (Optical Character Recognition)** | Extract structured text fields from document images |
| **Document Classification** | Identify the type of identity document |
| **Image Preprocessing** | Normalize, denoise, and prepare images for downstream analysis |
| **Computer Vision** | Analyse visual structure, layout, and appearance of documents |
| **Image Forensics** | Detect digital manipulation artefacts such as copy-paste regions, splicing, or re-compression |
| **Machine Learning** | Classify documents and detect anomalous patterns |
| **Field Validation** | Cross-validate extracted text fields against expected formats and rules |
| **Duplicate Detection** | Identify whether the same document or document number has been seen before |
| **Identity Consistency Checking** | Flag cases where a known document number appears with different identity fields |
| **Anomaly Detection** | Generate structured anomaly signals for suspicious indicators |
| **Risk Assessment** | Compute a composite risk score based on detected anomalies |
| **Explainable AI** | Communicate the evidence and reasoning behind every risk signal |

> **Important:** This system is designed as a **screening and decision-support tool**, not as an authoritative mechanism for declaring a document or person fraudulent. All high-risk signals are intended to guide human review, not to replace it.

---

## 2. Problem Statement

Identity documents are critical instruments of trust used for onboarding into financial services, government processes, healthcare, education, and employment. As a consequence, they are also targets for manipulation and forgery.

### Categories of Potential Manipulation

| Category | Examples |
|---|---|
| **Field-level text editing** | Name modification, date-of-birth change, document number alteration |
| **Photograph manipulation** | Photograph replacement, face splicing |
| **Copy-paste and splicing** | Inserting content from another document |
| **Font and layout modification** | Replacing text with a visually similar but different font |
| **Text removal** | Erasing original text and re-entering different values |
| **Recapture / reprint** | Printing a digitally modified document and re-photographing it |
| **Screenshot substitution** | Submitting a screenshot of a document rather than the original |
| **Synthetic / AI-generated documents** | Fully fabricated documents generated using image synthesis tools |
| **Duplicate documents** | Submitting the same document number for multiple identities |
| **Identity-field inconsistency** | Same document number associated with different names or dates of birth |

### Why OCR Alone Is Insufficient

A naive OCR-based approach can extract text fields from a document image:

```
Name           : Rahul Kumar
Document No.   : ABC1234567
Date of Birth  : 12-05-2001
```

However, OCR alone **cannot** determine:
- Whether the extracted text has been digitally modified after the document was issued
- Whether the photograph on the document belongs to the person presenting it
- Whether the document's visual layout is consistent with a genuine specimen
- Whether the document number has previously been associated with a different identity
- Whether the image contains forensic artefacts indicating digital manipulation

Addressing these gaps requires a multi-modal pipeline combining text extraction, visual analysis, forensic techniques, and cross-referencing against a stored knowledge base.

---

## 3. Project Objectives

| # | Objective | Status |
|---|---|---|
| 1 | Automatically process identity-document images and PDF files | Planned |
| 2 | Identify the type of identity document from its visual layout | Planned |
| 3 | Extract structured information fields using OCR | Planned |
| 4 | Analyse visual and structural characteristics of documents | Planned |
| 5 | Apply image forensic techniques to detect potential digital manipulation | Planned |
| 6 | Validate extracted text fields against format rules and cross-document consistency | Planned |
| 7 | Detect duplicate documents or document numbers associated with different identities | Planned |
| 8 | Generate structured anomaly signals for each detected suspicious indicator | Planned |
| 9 | Compute a composite, explainable risk assessment score | Planned |
| 10 | Provide supporting evidence for each anomaly | Planned |
| 11 | Present results via a web-based interface and REST API | Planned |
| 12 | Support export of screening reports for human/official verification | Planned |

---

## 4. Key Features

> All features listed below are **planned**. The repository is currently in the initialization and planning phase.

| Feature | Status | Planned Technology | Description |
|---|---|---|---|
| Document Upload (image/PDF) | Planned | FastAPI, Python | Accept JPEG, PNG, PDF uploads via REST API |
| File Validation | Planned | Python (Pillow, PyMuPDF) | Validate file format, size, and image quality |
| Image Preprocessing | Planned | OpenCV | Deskewing, denoising, contrast normalization, resizing |
| Document Type Classification | Planned | CNN / ML classifier | Identify document type |
| OCR Text Extraction | Planned | Tesseract / PaddleOCR | Extract raw text from document regions |
| Structured Field Extraction | Planned | Regex, NLP | Parse OCR output into structured fields |
| Image Forensics | Planned | OpenCV, forensic algorithms | Detect copy-paste, splicing, and re-compression artefacts |
| Tampering Detection | Planned | ML / Deep Learning | Detect evidence of digital editing |
| Field Validation | Planned | Rule-based engine | Validate field formats and cross-field consistency |
| Duplicate Detection | Planned | Database lookup, hashing | Identify documents or numbers seen before |
| Identity Consistency Check | Planned | Database comparison | Flag document numbers linked to different identity fields |
| Anomaly Detection | Planned | ML / rule-based | Detect and enumerate suspicious signals |
| Risk Scoring | Planned | Weighted scoring model | Aggregate anomalies into a composite risk level |
| Explainable AI Report | Planned | Custom reporting engine | Communicate anomalies with supporting evidence |
| REST API | Planned | FastAPI | Backend API for upload, processing, and result retrieval |
| Web Frontend | Planned | React / HTML + JS | User-facing interface |
| Admin Dashboard | Planned | Frontend framework | View processing history and analytics |
| Docker Containerisation | Planned | Docker, Docker Compose | Container-based deployment |

---

## 5. System Workflow

The following diagram describes the proposed end-to-end processing workflow:

```mermaid
flowchart TD
    A([Document Upload\nImage or PDF]) --> B[File Validation\nFormat · Size · Quality]
    B --> C[Image Preprocessing\nDeskew · Denoise · Normalize]
    C --> D[Document Type Classification]
    D --> E[OCR Text Extraction\nTesseract or PaddleOCR]
    E --> F[Structured Field Extraction\nName · DOB · Document Number]
    F --> G[Image Forensics\nCopy-Paste · Splicing · Recompression]
    F --> H[Field Consistency Validation\nFormat Rules · Cross-field Logic]
    F --> I[Duplicate and Identity Consistency Check\nDatabase Lookup · Hash Matching]
    G --> J[Anomaly Aggregation Engine]
    H --> J
    I --> J
    J --> K[Risk Assessment\nWeighted Composite Score]
    K --> L[Explainable Screening Report\nAnomaly List · Evidence · Risk Level]
    L --> M([Human and Official Verification])
```

> **Status:** This workflow represents the **proposed design**. Implementation has not yet commenced.

---

## 6. Important Fraud Scenario

### Same Document Number with Different Identity Information

One of the most significant fraud signals this system is designed to detect is the re-use of a genuine document number with different identity fields. The following uses **entirely fictional information**.

**Record already in the database:**

| Field | Value |
|---|---|
| Document Number | `ABC1234567` |
| Name | Rahul Kumar |
| Date of Birth | 12-05-2001 |

**Newly submitted document:**

| Field | Value |
|---|---|
| Document Number | `ABC1234567` |
| Name | Amit Sharma |
| Date of Birth | 12-05-2001 |

The document numbers are identical but the names differ — a suspicious identity-consistency signal.

#### Detection Flow

```mermaid
flowchart TD
    A([New Document Submitted]) --> B[OCR Extraction]
    B --> C[Extract Doc No. ABC1234567\nName: Amit Sharma · DOB: 12-05-2001]
    C --> D[Database Search by Document Number]
    D --> E{Document Number\nFound?}
    E -- No --> F[Store as New Record]
    E -- Yes --> G[Retrieve Existing Record\nName: Rahul Kumar · DOB: 12-05-2001]
    G --> H[Compare Identity Fields]
    H --> I{Name Match?}
    I -- Yes --> J[No Inconsistency Detected]
    I -- No --> K[ANOMALY: Name Mismatch\nABC1234567 linked to two different names]
    K --> L[Risk Score Increased]
    L --> M([Flag for Human Verification])
```

> **Important:** A name mismatch on a shared document number does **not** automatically prove fraud. It is a suspicious signal requiring additional human and official verification. Possible explanations include data entry errors, OCR misreads, document reissuance, or deliberate misuse.

---

## 7. Types of Anomalies

| Anomaly | Example | Detection Approach | Planned Response |
|---|---|---|---|
| Text / Field Manipulation | Name changed | Image forensics + OCR comparison | Flag |
| Date of Birth Modification | DOB changed | OCR + format validation + DB check | Flag |
| Document Number Modification | Last digits altered | OCR + format rules + DB lookup | Flag |
| Photograph Replacement | Different person's photo | Computer vision + face analysis | Flag |
| Image Splicing | Region from another image | Forensic artefact detection (proposed) | Flag |
| Copy-Paste Manipulation | Text block repositioned | Visual similarity analysis (proposed) | Flag |
| Font Inconsistency | Different font in edited field | Layout + typography analysis (proposed) | Flag |
| Layout / Alignment Inconsistency | Text field misaligned | Document structure comparison (proposed) | Flag |
| Screenshot Substitution | Digital screenshot submitted | Screen artefact detection (proposed) | Flag |
| Reprint / Recapture | Modified document re-scanned | Image quality analysis (proposed) | Flag |
| Duplicate Document | Same document for multiple people | Hash matching + embedding similarity (proposed) | Flag |
| Same ID + Different Name | Doc no. linked to two names | Database comparison | Flag |
| Same ID + Different DOB | Doc no. linked to two DOBs | Database comparison | Flag |
| Synthetic / AI-Generated Document | Fully fabricated document | Forensic / ML-based detection (proposed) | Flag |
| Metadata Inconsistency | Creation date after claimed issue date | File metadata analysis (proposed) | Flag |

---

## 8. AI / ML Architecture

### 8.1 Computer Vision (OpenCV)

- **Preprocessing:** Geometric correction, noise reduction, contrast normalisation, adaptive thresholding, edge detection
- **Feature extraction:** Structural analysis of document regions, field boundaries, and security element locations
- **Manipulation analysis:** Statistical noise analysis, block artefact detection, and local variance analysis to identify regions inconsistent with surrounding content

### 8.2 OCR — Text Extraction

The system proposes **Tesseract OCR** or **PaddleOCR** for text extraction. OCR output is parsed using regular expressions and named entity recognition to populate structured field objects (name, date of birth, document number, etc.).

### 8.3 Machine Learning

| Module | Proposed Approach |
|---|---|
| Document type classification | CNN-based classifier trained on document layout features |
| Tampering detection | Binary classifier (authentic vs. manipulated) using forensic image features |
| Anomaly detection | Isolation Forest or one-class SVM on extracted feature vectors |
| Risk scoring | Weighted aggregation of anomaly signals with tunable thresholds |

### 8.4 Deep Learning (Proposed)

Depending on dataset availability and project progress, the system may incorporate:

- **Convolutional Neural Networks (CNNs)** for document classification and visual feature extraction
- **Pre-trained Vision Transformers (ViT)** for fine-grained manipulation detection, building on the field-localised approach demonstrated in FLiD (Kumar et al., 2026)
- **MobileNetV3 / EfficientNet** as lightweight backbones for resource-efficient inference

### 8.5 Explainable AI — Planned

Planned explainability outputs include:

- **Anomaly description:** Plain-language explanation of the detected anomaly
- **Affected field:** Specific document field associated with the anomaly
- **Confidence level:** Model confidence or rule-match strength
- **Supporting evidence:** Highlighted region, field value comparison, or forensic artefact description
- **Risk level:** Low / Medium / High / Critical

> Specific XAI methods (LIME, SHAP, gradient-based saliency maps) will be selected during implementation based on the chosen model architecture.

---

## 9. Research and Literature Foundation

The following three research papers were independently verified and are directly relevant to the methods and objectives of this project.

---

### Paper 1: MIDV-2020 — A Comprehensive Benchmark Dataset for Identity Document Analysis

| Field | Detail |
|---|---|
| **Title** | MIDV-2020: A Comprehensive Benchmark Dataset for Identity Document Analysis |
| **Authors** | Konstantin Bulatov, Ekaterina Emelianova, Daniil Tropin, Natalya Skoryukina, Yulia Chernyshova, Alexey Sheshkus, Vladimir L. Arlazarov |
| **Year** | 2022 |
| **Journal / Conference** | Computer Optics, Vol. 46, No. 2 |
| **Publisher** | Image Processing Systems Institute (IPSI RAS) |
| **arXiv** | arXiv:2107.00396 |
| **URL** | https://arxiv.org/abs/2107.00396 |

**Problem Addressed:**
A key obstacle in identity document analysis research is the scarcity of publicly available, labelled datasets. Existing datasets at the time of publication lacked diversity in document types, capturing conditions, or field-value variability, and were typically designed for only a subset of document analysis tasks.

**Dataset and Methodology:**
MIDV-2020 consists of **1,000 video clips**, **2,000 scanned images**, and **1,000 photographs** covering 1,000 unique mock identity documents. Each document uses unique synthetic text field values and unique artificially generated face images, with rich annotation covering document localisation, OCR, and face detection. In total, MIDV-2020 contains **72,409 annotated images**.

**Key Findings:**
MIDV-2020 establishes a large-scale benchmark covering multiple document analysis sub-tasks simultaneously. The use of synthetic, privacy-preserving data allows public release without exposing real personal information.

**Limitations:**
MIDV-2020 is primarily designed for document recognition tasks rather than specifically for forgery or tampering detection. A derivative dataset, MIDV-DM, has since been introduced for document manipulation detection and localisation, extending MIDV-2020 with 8,000 automatically generated manipulated images covering eight manipulation types.

**Relevance to This Project:**
MIDV-2020 is a directly applicable resource for training and evaluating document type classification and OCR components. MIDV-DM is particularly relevant for the tampering detection module.

---

### Paper 2: FLiD — Field-Localized Forgery Detection for Digital Identity Documents

| Field | Detail |
|---|---|
| **Title** | Field-Localized Forgery Detection for Digital Identity Documents |
| **Authors** | Abhishek Kumar, Riya Tapwal, Carsten Maple, Mark Hooper |
| **Year** | 2026 |
| **Journal / Conference** | arXiv preprint, cs.CV |
| **arXiv** | arXiv:2605.09089 |
| **DOI** | 10.48550/arXiv.2605.09089 |
| **URL** | https://arxiv.org/abs/2605.09089 |

**Problem Addressed:**
Existing image forgery detectors are designed for natural images and do not account for the structured layout of identity documents, where security-relevant information is concentrated in specific semantic fields. Full-document processing is computationally expensive and dilutes the signal because the manipulated area is typically very small (0.3–4% of pixels) relative to the entire document.

**Methodology:**
FLiD (Field-Localised Forgery Detection) uses a **fine-tuned YOLO11 detector** to localise facial and textual regions, then extracts compact representations using a **frozen MobileNetV3-Small backbone**. A small 191K-parameter classification head makes the final forgery decision. Face and text detectors are trained independently and combined through **score-level fusion** for documents with simultaneous manipulations.

**Key Findings:**
Under 5-fold cross-validation, FLiD achieves:
- AUC **0.834** for face region manipulation detection
- AUC **0.926** for text region manipulation detection
- AUC **0.837** for combined attack detection

FLiD reduces Equal Error Rate by **28–29 percentage points** compared to a full-document baseline, requires **13x fewer trainable parameters**, and **21x fewer FLOPs** per field.

**Limitations:**
This is a preprint and has not yet undergone full peer review. Generalisation to highly diverse real-world document collections with varying capture conditions remains to be established.

**Relevance to This Project:**
FLiD directly validates the proposed capstone approach of combining field localisation, lightweight CNN backbone, and field-level forgery classification. The field-localised paradigm and score-level fusion strategy are applicable design patterns for the tampering detection module.

---

### Paper 3: DocForge-Bench — A Comprehensive Benchmark for Document Forgery Detection and Analysis

| Field | Detail |
|---|---|
| **Title** | DocForge-Bench: A Comprehensive Benchmark for Document Forgery Detection and Analysis |
| **Year** | 2026 |
| **Journal / Conference** | arXiv preprint, cs.CV |
| **arXiv** | arXiv:2603.01433 |
| **URL** | https://arxiv.org/abs/2603.01433 |

**Problem Addressed:**
General-purpose image manipulation detection methods assume the tampered region comprises 10–30% of the image area. Real-world identity document forgeries typically affect only **0.3–4% of pixels**, which invalidates standard decision thresholds and evaluation metrics used in natural image manipulation detection.

**Methodology:**
DocForge-Bench introduces a structured benchmark covering text-region tampering, commercial receipt forgery, and identity document forgery. It systematically evaluates multiple existing detectors (TruFor, CAT-Net, and others) against document-specific datasets including DocTamper, T-SROIE, RealTextManipulation, Tampered-IC13, MixTamper, FantasyID, and FSTS-1.5k, providing a rigorous cross-dataset evaluation framework and taxonomy of document manipulation types.

**Key Findings:**
Leading general-purpose manipulation detectors fail significantly on identity document forgeries due to extreme class imbalance between authentic and manipulated pixels. Domain-specific models trained with document-appropriate thresholds substantially outperform general detectors on this task.

**Limitations:**
As a preprint, peer-review conclusions are pending. Dataset licences and accessibility vary across the catalogued datasets.

**Relevance to This Project:**
DocForge-Bench provides the critical justification for why generic manipulation detectors are insufficient for identity documents, and catalogues the datasets (DocTamper, FantasyID, MIDV-DM) most applicable for training and evaluation in this capstone.

---

## 10. Research Gap

### Gap: Integrated Multi-Modal Identity Screening Pipeline with Explainable Risk Assessment

Existing published systems tend to address individual sub-problems in isolation:

| Sub-problem | State of Existing Research |
|---|---|
| Identity document recognition / OCR | Well-studied (MIDV-2020 and successors) |
| Full-document forgery classification | Partially addressed (FLiD, DocForge-Bench) |
| Tampered text-region localisation | Active research area (DocTamper, CAT-Net variants) |
| Photograph replacement detection | Addressed in face anti-spoofing literature |
| Identity consistency / duplicate detection | Primarily a systems engineering problem; limited academic ML work |
| Explainable risk assessment for documents | Very limited published work |

**The gap this capstone addresses:** No publicly documented, integrated, open-source pipeline currently combines all of the following in a single deployable system:

1. OCR-based structured field extraction  
2. Computer vision-based document analysis  
3. Image forensics for manipulation detection  
4. Field-level validation and consistency checking  
5. Cross-document identity consistency verification  
6. Duplicate detection  
7. Anomaly aggregation and risk scoring  
8. Explainable, human-readable screening reports  
9. A deployable REST API and web interface  

This capstone proposes to investigate the feasibility of such an integrated pipeline, evaluate its effectiveness on available public datasets, and document the engineering challenges encountered.

---

## 11. Dataset Strategy

> No dataset has been included in this repository. The project is in the planning phase.

### 11.1 Publicly Available Datasets Under Consideration

| Dataset | Description | Relevance |
|---|---|---|
| **MIDV-2020** | 72,409 annotated images of 1,000 unique mock identity documents | Document recognition, OCR baseline |
| **MIDV-DM** | MIDV-2020 extended with 8,000 manipulated images (8 manipulation types) | Tampering detection training and evaluation |
| **DocTamper** | Document-specific tampering dataset with pixel-level localisation masks | Text-region tampering localisation |
| **FantasyID** | Identity document forgery dataset | Identity document forgery classification |
| **FSTS-1.5k** | Forged seal/stamp and text dataset | Text manipulation detection |
| **Tampered-IC13** | ICDAR 2013 text dataset with synthetic tampering | Text manipulation detection |

### 11.2 Synthetic Data Generation

Given that real identity document images are subject to strict privacy and legal constraints, the project will explore:
- Generating mock identity documents with fictional names, dates, and document numbers
- Applying controlled, programmatic manipulations (text replacement, image splicing, contrast modification) to create labelled training data
- Augmentation techniques to maintain class balance

### 11.3 Key Considerations

| Consideration | Notes |
|---|---|
| **Privacy and Legal** | Real identity document images cannot be collected without explicit consent. All datasets will be publicly available research datasets with appropriate licences, or synthetically generated data using fictional information. |
| **Licensing** | Dataset licences will be reviewed before use. |
| **Class Imbalance** | Addressed through oversampling, class-weighted loss functions, or augmentation. |
| **Data Splits** | Standard 70/15/15 train/validation/test split with stratification. |
| **De-identification** | Any experimental data derived from real documents must be fully de-identified before use. |

---

## 12. System Architecture

```mermaid
graph TB
    subgraph FE["Frontend — Planned"]
        F1[Document Upload UI]
        F2[Result and Report View]
        F3[Admin Dashboard]
    end

    subgraph API["API Layer — Planned FastAPI"]
        A1[POST /documents/upload]
        A2[GET /documents/id/result]
        A3[GET /documents/id/report]
        A4[GET /admin/history]
    end

    subgraph PROC["Document Processing Engine — Planned Python"]
        P1[File Validator]
        P2[Image Preprocessor OpenCV]
        P3[Document Type Classifier CNN]
        P4[OCR Engine Tesseract or PaddleOCR]
        P5[Field Extractor Regex and NLP]
    end

    subgraph AI["AI and Forensic Analysis — Planned"]
        M1[Image Forensics Module OpenCV]
        M2[Tampering Detector CNN and ML]
        M3[Duplicate Detector Hashing and Embeddings]
        M4[Identity Consistency Checker Database Comparison]
    end

    subgraph VAL["Validation and Anomaly Engine — Planned"]
        V1[Field Validation Rule-based]
        V2[Anomaly Aggregator]
        V3[Risk Scoring Engine]
        V4[Explainability Module]
    end

    subgraph DB["Database — Planned PostgreSQL"]
        D1[(Documents)]
        D2[(ExtractedFields)]
        D3[(VerificationResults)]
        D4[(Anomalies)]
        D5[(ProcessingHistory)]
    end

    FE --> API
    API --> PROC
    PROC --> AI
    PROC --> VAL
    AI --> VAL
    VAL --> DB
    DB --> API
```

---

## 13. Technology Stack

> All technologies listed are **planned**. Final choices are subject to change during development.

| Category | Technology | Purpose |
|---|---|---|
| **Language** | Python 3.10+ | Primary development language |
| **Backend / API** | FastAPI | REST API framework |
| **Frontend** | React.js / HTML + JavaScript | Web interface |
| **OCR** | Tesseract OCR / PaddleOCR | Text extraction from document images |
| **Computer Vision** | OpenCV | Image preprocessing, feature extraction, forensic analysis |
| **Machine Learning** | scikit-learn | Classical ML models (classification, anomaly detection) |
| **Deep Learning** | PyTorch | CNN and transformer-based models |
| **Image Processing** | Pillow (PIL) | Image loading and format handling |
| **PDF Processing** | PyMuPDF | PDF to image conversion |
| **Database** | PostgreSQL | Storage of documents, fields, anomalies, and history |
| **ORM** | SQLAlchemy | Database interaction layer |
| **Containerisation** | Docker + Docker Compose | Reproducible deployment |
| **Data Processing** | NumPy, Pandas | Numerical computation and data manipulation |
| **Testing** | pytest | Unit and integration testing |
| **Version Control** | Git + GitHub | Source code management |

---

## 14. Project Structure

> The repository is currently empty (initialization phase). The following structure represents the **planned** project layout.

```
AI-Based-Fake-Identity-Document-Screening-System/
|
+-- README.md                          # Project documentation (this file)
|
+-- backend/                           # Planned: Python backend
|   +-- main.py                        # FastAPI application entry point
|   +-- requirements.txt               # Python dependencies
|   +-- .env.example                   # Environment variable template
|   |
|   +-- api/                           # API route definitions
|   |   +-- routes/
|   |   |   +-- documents.py           # Document upload and status endpoints
|   |   |   +-- admin.py               # Admin / history endpoints
|   |   +-- dependencies.py            # FastAPI dependency injection
|   |
|   +-- core/                          # Core configuration and utilities
|   |   +-- config.py                  # Application settings
|   |   +-- database.py                # Database connection and session
|   |   +-- security.py                # Authentication utilities
|   |
|   +-- processing/                    # Document processing pipeline
|   |   +-- validator.py               # File validation
|   |   +-- preprocessor.py            # Image preprocessing
|   |   +-- classifier.py              # Document type classification
|   |   +-- ocr_engine.py              # OCR wrapper
|   |   +-- field_extractor.py         # Structured field extraction
|   |
|   +-- forensics/                     # Image forensics and AI analysis
|   |   +-- image_forensics.py         # Copy-paste, splicing detection
|   |   +-- tampering_detector.py      # ML-based tampering detection
|   |   +-- duplicate_detector.py      # Hash and embedding-based duplicate detection
|   |
|   +-- validation/                    # Field validation and anomaly detection
|   |   +-- field_validator.py         # Rule-based field validation
|   |   +-- identity_consistency.py    # Identity consistency check
|   |   +-- anomaly_aggregator.py      # Anomaly aggregation
|   |   +-- risk_engine.py             # Risk score computation
|   |   +-- explainability.py          # Explainable AI report generation
|   |
|   +-- models/                        # Database ORM models
|   |   +-- document.py
|   |   +-- extracted_field.py
|   |   +-- verification_result.py
|   |   +-- anomaly.py
|   |   +-- processing_history.py
|   |
|   +-- tests/                         # Backend tests
|       +-- test_api.py
|       +-- test_ocr.py
|       +-- test_forensics.py
|       +-- test_validation.py
|
+-- frontend/                          # Planned: Web frontend
|   +-- index.html
|   +-- src/
|   |   +-- components/
|   |   +-- pages/
|   +-- package.json
|
+-- ml/                                # Planned: ML model training
|   +-- notebooks/                     # Research and exploration notebooks
|   +-- training/
|   |   +-- train_classifier.py
|   |   +-- train_tampering_detector.py
|   +-- models/
|   +-- evaluation/
|       +-- evaluate.py
|
+-- data/                              # Planned: Dataset management (gitignored)
|   +-- raw/
|   +-- processed/
|   +-- synthetic/
|
+-- docker/                            # Planned: Docker configuration
|   +-- Dockerfile.backend
|   +-- Dockerfile.frontend
|   +-- docker-compose.yml
|
+-- docs/                              # Planned: Extended documentation
|   +-- architecture.md
|   +-- api_reference.md
|   +-- screenshots/
|
+-- .gitignore
```

---

## 15. Installation

> **Note:** The repository is currently empty. Installation instructions describe the **planned** setup procedure.

### Prerequisites

- Python 3.10 or higher
- Node.js 18+ (for frontend)
- PostgreSQL 14+
- Docker and Docker Compose (optional)
- Tesseract OCR (system dependency)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/sumitkumarbarnwal/AI-Based-Fake-Identity-Document-Screening-System.git
cd AI-Based-Fake-Identity-Document-Screening-System
```

### Step 2: Backend Setup (Planned)

```bash
cd backend

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# Install Python dependencies
pip install -r requirements.txt
```

### Step 3: Install Tesseract OCR (Planned)

```bash
# Ubuntu / Debian
sudo apt-get install tesseract-ocr

# macOS (Homebrew)
brew install tesseract

# Windows: Download installer from https://github.com/UB-Mannheim/tesseract/wiki
```

### Step 4: Configure Environment Variables (Planned)

```bash
cp .env.example .env
# Edit .env with your configuration — see Section 16
```

### Step 5: Database Setup (Planned)

```bash
createdb ai_document_screening
python -m alembic upgrade head
```

### Step 6: Frontend Setup (Planned)

```bash
cd ../frontend
npm install
```

### Step 7: Run the Application (Planned)

```bash
# Backend (from backend/)
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Frontend (from frontend/, separate terminal)
npm run dev
```

### Alternative: Docker (Planned)

```bash
docker-compose up --build
```

---

## 16. Environment Variables

> `.env.example` will be provided when the backend is implemented. Never commit actual secrets.

```env
# Application
APP_ENV=development
APP_HOST=0.0.0.0
APP_PORT=8000
SECRET_KEY=your_secret_key_here

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/ai_document_screening

# OCR
TESSERACT_CMD=/usr/bin/tesseract

# File Upload
MAX_UPLOAD_SIZE_MB=10
ALLOWED_EXTENSIONS=jpg,jpeg,png,pdf

# ML Models
MODEL_DIR=./ml/models

# Storage
UPLOAD_DIR=./uploads

# Logging
LOG_LEVEL=INFO
```

---

## 17. API Documentation

> **Note:** The backend API has not yet been implemented. The following describes the **planned** REST API.

**Base URL:** `http://localhost:8000/api/v1`

### Planned Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/documents/upload` | POST | Upload a document image or PDF for screening |
| `/documents/{id}/status` | GET | Check processing status of a submitted document |
| `/documents/{id}/result` | GET | Retrieve the screening result and anomaly list |
| `/documents/{id}/report` | GET | Download the full explainable screening report |
| `/admin/documents` | GET | List all processed documents (admin only) |
| `/admin/documents/{id}` | DELETE | Remove a document record (admin only) |
| `/health` | GET | API health check |

### Example Request: Document Upload (Planned)

```http
POST /api/v1/documents/upload
Content-Type: multipart/form-data

file: <document image or PDF>
document_type_hint: "aadhaar"
```

### Example Response: Screening Result (Planned)

```json
{
  "document_id": "d_abc123",
  "status": "completed",
  "risk_level": "HIGH",
  "risk_score": 78,
  "extracted_fields": {
    "name": "Amit Sharma",
    "date_of_birth": "12-05-2001",
    "document_number": "ABC1234567"
  },
  "anomalies": [
    {
      "anomaly_id": "a_001",
      "type": "IDENTITY_CONSISTENCY",
      "description": "Document number ABC1234567 is already associated with a different name in the database.",
      "severity": "HIGH",
      "evidence": {
        "existing_name": "Rahul Kumar",
        "submitted_name": "Amit Sharma",
        "field": "name"
      }
    }
  ],
  "recommendation": "Flag for human verification",
  "processing_time_ms": 1842
}
```

---

## 18. Database Design

> **Status:** Proposed. No database has been implemented.

```mermaid
erDiagram
    DOCUMENTS {
        uuid id PK
        string filename
        string file_type
        string storage_path
        string document_type
        timestamp uploaded_at
        string status
    }

    EXTRACTED_FIELDS {
        uuid id PK
        uuid document_id FK
        string field_name
        string field_value
        float ocr_confidence
        timestamp extracted_at
    }

    VERIFICATION_RESULTS {
        uuid id PK
        uuid document_id FK
        string risk_level
        int risk_score
        string recommendation
        timestamp created_at
    }

    ANOMALIES {
        uuid id PK
        uuid document_id FK
        string anomaly_type
        string description
        string severity
        json evidence
        timestamp detected_at
    }

    PROCESSING_HISTORY {
        uuid id PK
        uuid document_id FK
        string stage
        string status
        string message
        timestamp recorded_at
    }

    DOCUMENTS ||--o{ EXTRACTED_FIELDS : "has"
    DOCUMENTS ||--o| VERIFICATION_RESULTS : "produces"
    DOCUMENTS ||--o{ ANOMALIES : "generates"
    DOCUMENTS ||--o{ PROCESSING_HISTORY : "tracked by"
```

---

## 19. Screenshots

No screenshots are currently available. The application interface has not yet been implemented.

Screenshots will be added as the application reaches the prototype stage. Planned screenshots include:
- Document upload interface
- OCR extraction result view
- Anomaly detection report
- Risk assessment dashboard
- Explainable screening report

---

## 20. Testing Strategy

> **Status:** Testing has not yet been implemented.

| Test Type | Tool | Description |
|---|---|---|
| **Unit Tests** | pytest | Test individual functions in preprocessing, OCR, field extraction, validation, and risk scoring modules |
| **API Tests** | pytest + httpx | Test each REST endpoint for correct request handling, status codes, and response schemas |
| **OCR Tests** | pytest | Evaluate OCR accuracy on a set of labelled test document images |
| **Model Tests** | pytest | Validate ML model loading, inference, and output format |
| **Integration Tests** | pytest | Test the full processing pipeline end-to-end with sample documents |
| **Security Tests** | Manual + tools | Test for file upload vulnerabilities, path traversal, and API authentication |
| **Performance Tests** | locust / pytest-benchmark | Measure processing time and throughput under concurrent load |
| **Adversarial Tests** | Manual | Test the system against deliberately manipulated documents to assess detection robustness |

---

## 21. Model Evaluation

> **Status:** No ML models have been implemented or trained. No numerical results are reported.

### Planned Evaluation Metrics

| Metric | Description |
|---|---|
| **Accuracy** | Overall classification correctness (authentic vs. manipulated) |
| **Precision** | Proportion of flagged documents that are genuinely suspicious |
| **Recall** | Proportion of genuinely suspicious documents correctly flagged |
| **F1-Score** | Harmonic mean of precision and recall |
| **ROC-AUC** | Area under the receiver operating characteristic curve |
| **False Positive Rate** | Rate of authentic documents incorrectly flagged |
| **False Negative Rate** | Rate of manipulated documents incorrectly cleared |
| **OCR Field Accuracy** | Percentage of text fields correctly extracted and parsed |
| **Processing Time** | Average end-to-end processing time per document |

> False negatives (failing to detect manipulation) and false positives (incorrectly flagging authentic documents) have different real-world consequences. Evaluation will consider this tradeoff explicitly in the context of a human-in-the-loop screening workflow.

---

## 22. Security and Privacy

Because this project processes identity documents — some of the most sensitive personal data — security and privacy are design-level requirements.

| Control | Status | Notes |
|---|---|---|
| No hard-coded secrets | Design requirement | All credentials managed via environment variables |
| Secure environment variables | Planned | `.env` files excluded from version control via `.gitignore` |
| Input validation | Planned | File type, size, and format validation before processing |
| Upload size limits | Planned | Configurable maximum upload size |
| Authentication | Planned | Token-based API authentication for all non-public endpoints |
| Access control | Planned | Admin-only endpoints for history and document management |
| Data minimisation | Design requirement | Only the minimum data necessary for screening will be stored |
| Encrypted storage | Planned | Document images stored with encryption at rest |
| Secure logging | Planned | Logs must not contain raw extracted personal data |
| Data retention | Planned | Documents and fields deleted after a defined retention period |
| Synthetic/de-identified data | Design requirement | Only publicly licensed or synthetically generated data used in development |
| HTTPS | Planned | TLS encryption for all API communication in production |

### Important Privacy Note

In a production context, applicable data protection regulations (such as the DPDP Act 2023 in India or GDPR in the EU) would govern data collection, storage, retention, and subject rights. During development and research, only publicly available research datasets with appropriate licences, or synthetically generated data using fictional information, will be used.

---

## 23. Limitations

| Limitation | Description |
|---|---|
| **OCR errors** | OCR accuracy degrades with poor image quality, unusual fonts, or low-contrast documents |
| **Image quality dependency** | The system's effectiveness depends heavily on the quality of the submitted image |
| **Unseen manipulation techniques** | A model trained on known techniques may fail to detect novel forgery methods |
| **Dataset limitations** | Publicly available identity document datasets are limited in diversity |
| **False positives** | The system may flag authentic documents as suspicious |
| **False negatives** | The system may fail to detect sophisticated or novel manipulations |
| **No legal authority** | Automated screening does not constitute legal verification |
| **Generalisation** | Performance may vary significantly across document types, issuing authorities, or countries |
| **Privacy constraints** | Use of real identity documents for training is subject to strict legal and ethical constraints |
| **Decision-support only** | This system is designed to support — not replace — human review and official verification |

---

## 24. Roadmap

### Phase 1: Research and Planning (Months 1–2)

- [x] Repository initialized
- [ ] Literature review (papers identified — see Section 9)
- [ ] Dataset research and licensing review
- [ ] Requirements specification
- [ ] System architecture design
- [ ] Technology stack finalisation
- [ ] Project structure setup

### Phase 2: Document Processing Foundation (Months 2–3)

- [ ] Backend project scaffolding (FastAPI)
- [ ] Document upload API endpoint
- [ ] File validation module
- [ ] Image preprocessing pipeline (OpenCV)
- [ ] OCR integration (Tesseract / PaddleOCR)
- [ ] Structured field extraction
- [ ] Database schema implementation
- [ ] Unit tests for processing modules

### Phase 3: AI and ML Components (Months 3–4)

- [ ] Document type classification model
- [ ] Image forensics module
- [ ] Tampering / manipulation detection model
- [ ] Model training on available datasets
- [ ] Model evaluation and benchmarking

### Phase 4: Identity Consistency and Validation (Month 4)

- [ ] Field validation rule engine
- [ ] Database-based identity consistency checking
- [ ] Duplicate document detection
- [ ] Anomaly aggregation engine
- [ ] Risk scoring model

### Phase 5: Application Layer (Months 4–5)

- [ ] Complete REST API implementation
- [ ] Web frontend: document upload interface
- [ ] Web frontend: result and anomaly display
- [ ] Explainable AI reporting module
- [ ] Admin dashboard
- [ ] API authentication

### Phase 6: Deployment, Evaluation, and Documentation (Months 5–6)

- [ ] Docker containerisation
- [ ] Full integration testing
- [ ] Performance evaluation and optimisation
- [ ] Security audit
- [ ] Adversarial testing
- [ ] Deployment (staging environment)
- [ ] Final project documentation and report
- [ ] Capstone presentation materials

---

## 25. Responsible AI Disclaimer

> **This system is designed for preliminary document screening and academic research purposes.**

An automated risk signal generated by this system **does not** establish that a document is forged, that an identity is fraudulent, or that any individual has engaged in illegal activity. Automated systems can produce false positives and false negatives. No automated screening system can authenticate a document in a legal sense.

**All high-risk signals must be reviewed by appropriately qualified human reviewers and, where applicable, by official verification authorities before any consequential decision is made.**

This system **must not** be used to:
- Make irreversible decisions about individuals solely on the basis of an automated prediction
- Deny services, access, or rights to individuals without human review
- Replace official document verification processes required by law

The developers of this system take no responsibility for decisions made on the basis of automated outputs without appropriate human oversight.

---

## 26. Contributing

Contributions are welcome as the project develops. To contribute:

1. **Fork** the repository on GitHub
2. **Create a branch** for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** following the project's code style and documentation conventions
4. **Write or update tests** for your changes
5. **Commit** with a clear message:
   ```bash
   git commit -m "feat: add image preprocessing pipeline"
   ```
6. **Push** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open a Pull Request** with a clear description of your changes

Please ensure all tests pass before submitting a pull request. For significant architectural changes, open an issue for discussion before starting development.

---

## 27. License

**License: Not yet specified.**

No `LICENSE` file is currently present in this repository. The license will be added during the project development phase. Until specified, all rights are reserved by the repository owner.

---

## 28. Author

**Sumit Kumar Barnwal**

- **GitHub:** [github.com/sumitkumarbarnwal](https://github.com/sumitkumarbarnwal)
- **Repository:** [AI-Based-Fake-Identity-Document-Screening-System](https://github.com/sumitkumarbarnwal/AI-Based-Fake-Identity-Document-Screening-System)

---

*This README was prepared for academic and portfolio purposes as part of a 6-month capstone project. All identity information used in examples is entirely fictional. This system is designed as a research and decision-support tool, not as an authoritative fraud detection system.*
