import os
import uuid
import shutil
import aiofiles
from pathlib import Path
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from pydantic import BaseModel
from datetime import datetime

from app.core.database import get_db
from app.core.security import get_current_user_id
from app.core.config import settings
from app.models.document import Document, DocumentType, DocumentStatus

router = APIRouter()

UPLOAD_DIR = Path(settings.UPLOAD_DIR)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_MIME_TYPES = {
    "image/jpeg": "jpg",
    "image/png": "png",
    "application/pdf": "pdf",
}


# ──────────────────────────────────────────────────────
# Pydantic Schemas
# ──────────────────────────────────────────────────────

class DocumentResponse(BaseModel):
    id: str
    original_filename: str
    file_size: int
    mime_type: str
    document_type: DocumentType
    status: DocumentStatus
    created_at: datetime

    class Config:
        from_attributes = True


class DocumentListResponse(BaseModel):
    items: list[DocumentResponse]
    total: int
    page: int
    limit: int


# ──────────────────────────────────────────────────────
# Routes
# ──────────────────────────────────────────────────────

@router.post("/upload", response_model=DocumentResponse, status_code=status.HTTP_201_CREATED)
async def upload_document(
    file: UploadFile = File(...),
    current_user_id: str = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    """
    Upload an identity document image/PDF.
    - Validates file type and size
    - Saves file to disk with a UUID filename
    - Creates Document record in DB with status=PENDING
    """
    # Validate MIME type
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"Unsupported file type: {file.content_type}. Allowed: JPEG, PNG, PDF",
        )

    # Read and validate size
    contents = await file.read()
    size_mb = len(contents) / (1024 * 1024)
    if size_mb > settings.MAX_FILE_SIZE_MB:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"File too large: {size_mb:.1f}MB. Maximum allowed: {settings.MAX_FILE_SIZE_MB}MB",
        )

    # Save file with unique name
    ext = ALLOWED_MIME_TYPES[file.content_type]
    stored_filename = f"{uuid.uuid4()}.{ext}"
    user_upload_dir = UPLOAD_DIR / current_user_id
    user_upload_dir.mkdir(parents=True, exist_ok=True)
    file_path = user_upload_dir / stored_filename

    async with aiofiles.open(file_path, "wb") as f:
        await f.write(contents)

    # Create DB record
    document = Document(
        user_id=current_user_id,
        original_filename=file.filename or stored_filename,
        stored_filename=stored_filename,
        file_path=str(file_path),
        file_size=len(contents),
        mime_type=file.content_type,
        document_type=DocumentType.UNKNOWN,
        status=DocumentStatus.PENDING,
    )
    db.add(document)
    await db.flush()
    return document


@router.get("/", response_model=DocumentListResponse)
async def list_documents(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    current_user_id: str = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    """List all documents uploaded by the current user (paginated)."""
    offset = (page - 1) * limit

    total_result = await db.execute(
        select(func.count(Document.id)).where(Document.user_id == current_user_id)
    )
    total = total_result.scalar_one()

    result = await db.execute(
        select(Document)
        .where(Document.user_id == current_user_id)
        .order_by(Document.created_at.desc())
        .offset(offset)
        .limit(limit)
    )
    documents = result.scalars().all()

    return DocumentListResponse(items=list(documents), total=total, page=page, limit=limit)


@router.get("/{doc_id}", response_model=DocumentResponse)
async def get_document(
    doc_id: str,
    current_user_id: str = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    """Retrieve a specific document by ID (must belong to current user)."""
    result = await db.execute(
        select(Document).where(Document.id == doc_id, Document.user_id == current_user_id)
    )
    document = result.scalar_one_or_none()
    if not document:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Document not found")
    return document


@router.delete("/{doc_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_document(
    doc_id: str,
    current_user_id: str = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    """
    Delete a document.
    - Removes the file from disk
    - Deletes the DB record (cascades to screening_results)
    """
    result = await db.execute(
        select(Document).where(Document.id == doc_id, Document.user_id == current_user_id)
    )
    document = result.scalar_one_or_none()
    if not document:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Document not found")

    # Remove from disk
    file_path = Path(document.file_path)
    if file_path.exists():
        file_path.unlink()

    await db.delete(document)
