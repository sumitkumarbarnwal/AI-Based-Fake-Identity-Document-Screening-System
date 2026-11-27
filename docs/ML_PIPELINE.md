# Machine Learning & OCR Pipeline Architecture

## AI-Based Fake Identity Document Screening System

This guide outlines the technical architecture, computer vision models, and algorithmic pipelines used to detect forged identity documents.

---

## 🧩 Pipeline Overview

The screening pipeline processes document images in four sequential stages:

```
[Document Image]
       │
       ▼
1. Preprocessing & Normalization (Sumit)
       │
       ▼
2. Document Classification (Ansh)
       │
       ├─────────────────────────────────┐
       ▼                                 ▼
3a. OCR Text Extraction (Ansh)    3b. Deep Forgery Detection (Sumit)
       │                                 │
3c. Algorithmic Validation (Ansh)        │
       │                                 │
       └────────────────┬────────────────┘
                        ▼
4. Composite Scoring & Verdict Aggregation (Sumit)
                        │
                        ▼
       [Structured Screening Result JSON]
```

---

## 1. Document Classification

> **Owner:** Ansh  
> **Source:** `ml/models/document_classifier/classifier.py`

### Approach:
- **Architecture:** Lightweight MobileNetV3 (Small/Large) backbone with a custom 5-class classification head.
- **Classes:**
  1. `aadhaar` (UIDAI Aadhaar Card)
  2. `pan` (Income Tax Department PAN Card)
  3. `passport` (Republic of India Passport)
  4. `driving_license` (State RTO Driving License)
  5. `voter_id` (ECI Voter Identity Card)
- **Zero-Shot Alternative:** CLIP vision-text embeddings for zero-shot orientation and type recognition without extensive fine-tuning.

---

## 2. OCR Text Extraction & Field Mapping

> **Owner:** Ansh  
> **Source:** `ml/models/ocr_pipeline/extractor.py`

### OCR Processing Steps:
1. **Adaptive Preprocessing:** Bilateral filtering, contrast limited adaptive histogram equalization (CLAHE), and Otsu binarization to enhance micro-text and security guilloche patterns.
2. **Bilingual Text Recognition:** EasyOCR engine configured for English (`en`) and Hindi (`hi`) character sets.
3. **Bounding Box Mapping:** Extracted text bounding boxes are mapped to expected document regions (e.g., photo box, header, national emblem, date zone).

---

## 3. Algorithmic Field Validation

> **Owner:** Ansh  
> **Source:** `ml/models/ocr_pipeline/validator.py`

Extracted alphanumeric fields are checked against deterministic mathematical rules:

### A. Aadhaar Card — Verhoeff Check Digit Algorithm
- 12-digit Aadhaar numbers are validated using the Verhoeff base-10 dihedral check algorithm based on permutations and group theory.
- Any digit swap or single-digit alteration fails this check.

### B. PAN Card — Structure & Correspondence Rule
- Formatted as `[A-Z]{5}[0-9]{4}[A-Z]{1}`.
- 4th character denotes entity status (`P` = Individual, `C` = Company, `F` = Firm, etc.).
- 5th character must match the first letter of the applicant's surname.

### C. Passport — ICAO 9303 MRZ Checksums
- Dual 44-character Machine Readable Zone (MRZ) lines.
- Modulo 10 checksums with weights `[7, 3, 1]` on document number, date of birth, expiration date, and the composite checksum.

### D. Calendar Sanity Rules
- Checks for impossible dates (e.g., February 31st).
- DOB cannot be in the future; minimum age checks applied.

---

## 4. Deep Forensic Forgery Detection

> **Owner:** Sumit Kumar Barnwal  
> **Source:** `ml/models/forgery_detector/model.py`

### Multi-Faceted Forensic Techniques:
1. **Error Level Analysis (ELA):** Resaving images at known compression levels and computing pixel-difference matrices to highlight spliced or digitally added text/photos.
2. **Photo Cut-and-Paste Boundary Detection:** High-frequency gradient analysis around the photo boundary box to detect pasting artifacts.
3. **Typography & Font Anomaly Analysis:** Convolutional filters detect inconsistent anti-aliasing or font glyph weights across neighboring characters.
4. **Deep CNN / Vision Transformer (ViT):** Patch-based ViT embeddings detect subtle pixel-level tampering and synthetic generation.

---

## 5. Result Aggregation & Scoring

> **Owner:** Sumit Kumar Barnwal  
> **Source:** `backend/app/services/ml_service.py`

The pipeline synthesizes all findings into a deterministic verdict:

$$\text{Confidence Score} = 1.0 - \text{Composite Risk}$$

### Verdict Thresholds:
- **`AUTHENTIC`:** Composite Risk $\le 0.15$ (High confidence, all checksums valid, zero tampering detected).
- **`SUSPICIOUS`:** $0.15 < \text{Composite Risk} \le 0.45$ (Low-resolution scan, minor OCR ambiguity, or slight compression anomaly).
- **`FAKE`:** Composite Risk $> 0.45$ (Failed checksums, photo splicing detected, or impossible date syntax).
