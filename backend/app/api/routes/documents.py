# ====================================================
# Owner: Sumit Kumar Barnwal
# File: backend/app/api/routes/documents.py
# Responsibilities: Upload, retrieve, delete documents
# ====================================================
from fastapi import APIRouter, UploadFile, File

router = APIRouter()

# TODO (Sumit): Implement the following endpoints:
# POST   /upload        → Upload identity document image
# GET    /{id}          → Get document metadata and image URL
# DELETE /{id}          → Delete a document
# GET    /              → List user's uploaded documents

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """Upload an identity document for screening. (Sumit)"""
    pass

@router.get("/{doc_id}")
async def get_document(doc_id: str):
    """Retrieve a specific document's metadata. (Sumit)"""
    pass

@router.delete("/{doc_id}")
async def delete_document(doc_id: str):
    """Delete a document. (Sumit)"""
    pass
