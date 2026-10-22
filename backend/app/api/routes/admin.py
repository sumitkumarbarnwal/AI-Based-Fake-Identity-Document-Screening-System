from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, update
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from app.core.database import get_db
from app.core.security import get_current_user_id
from app.models.user import User, UserRole
from app.models.document import Document
from app.models.screening_result import ScreeningResult, Verdict

router = APIRouter()


# ──────────────────────────────────────────────────────
# Admin guard dependency
# ──────────────────────────────────────────────────────

async def require_admin(
    current_user_id: str = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
) -> User:
    """Dependency that ensures the caller is an admin."""
    result = await db.execute(select(User).where(User.id == current_user_id))
    user = result.scalar_one_or_none()
    if not user or user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required",
        )
    return user


# ──────────────────────────────────────────────────────
# Pydantic Schemas
# ──────────────────────────────────────────────────────

class UserAdminResponse(BaseModel):
    id: str
    email: str
    username: str
    full_name: str
    role: UserRole
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class PaginatedUsers(BaseModel):
    items: list[UserAdminResponse]
    total: int
    page: int
    limit: int


class UpdateUserRequest(BaseModel):
    is_active: Optional[bool] = None
    role: Optional[UserRole] = None


class SystemStats(BaseModel):
    total_users: int
    total_documents: int
    total_screenings: int
    authentic_count: int
    suspicious_count: int
    fake_count: int
    fraud_rate_percent: float


# ──────────────────────────────────────────────────────
# Routes
# ──────────────────────────────────────────────────────

@router.get("/users", response_model=PaginatedUsers)
async def list_users(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    admin: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """List all users in the system (admin only, paginated)."""
    offset = (page - 1) * limit

    total = (await db.execute(select(func.count(User.id)))).scalar_one()
    result = await db.execute(
        select(User).order_by(User.created_at.desc()).offset(offset).limit(limit)
    )
    users = result.scalars().all()

    return PaginatedUsers(items=list(users), total=total, page=page, limit=limit)


@router.get("/users/{user_id}", response_model=UserAdminResponse)
async def get_user(
    user_id: str,
    admin: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """Get a specific user's details (admin only)."""
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.patch("/users/{user_id}", response_model=UserAdminResponse)
async def update_user(
    user_id: str,
    payload: UpdateUserRequest,
    admin: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """Update a user's role or active status (admin only)."""
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if payload.is_active is not None:
        user.is_active = payload.is_active
    if payload.role is not None:
        user.role = payload.role

    await db.flush()
    return user


@router.get("/documents", response_model=dict)
async def list_all_documents(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    admin: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """List all documents across all users (admin only, paginated)."""
    offset = (page - 1) * limit
    total = (await db.execute(select(func.count(Document.id)))).scalar_one()
    result = await db.execute(
        select(Document).order_by(Document.created_at.desc()).offset(offset).limit(limit)
    )
    documents = result.scalars().all()
    return {
        "items": [
            {
                "id": d.id, "user_id": d.user_id, "original_filename": d.original_filename,
                "document_type": d.document_type, "status": d.status, "created_at": str(d.created_at),
            }
            for d in documents
        ],
        "total": total, "page": page, "limit": limit,
    }


@router.get("/documents/flagged", response_model=dict)
async def list_flagged_documents(
    admin: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """List all documents screened as suspicious or fake (admin only)."""
    result = await db.execute(
        select(ScreeningResult)
        .where(ScreeningResult.verdict.in_([Verdict.SUSPICIOUS, Verdict.FAKE]))
        .order_by(ScreeningResult.created_at.desc())
        .limit(100)
    )
    flagged = result.scalars().all()
    return {
        "items": [
            {
                "result_id": r.id, "document_id": r.document_id, "user_id": r.user_id,
                "verdict": r.verdict, "confidence_score": r.confidence_score,
                "fraud_indicators": r.fraud_indicators, "created_at": str(r.created_at),
            }
            for r in flagged
        ],
        "total": len(flagged),
    }


@router.get("/stats", response_model=SystemStats)
async def get_system_stats(
    admin: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """Overall system statistics for the admin dashboard."""
    total_users = (await db.execute(select(func.count(User.id)))).scalar_one()
    total_docs = (await db.execute(select(func.count(Document.id)))).scalar_one()
    total_screenings = (await db.execute(select(func.count(ScreeningResult.id)))).scalar_one()

    authentic = (await db.execute(
        select(func.count(ScreeningResult.id)).where(ScreeningResult.verdict == Verdict.AUTHENTIC)
    )).scalar_one()
    suspicious = (await db.execute(
        select(func.count(ScreeningResult.id)).where(ScreeningResult.verdict == Verdict.SUSPICIOUS)
    )).scalar_one()
    fake = (await db.execute(
        select(func.count(ScreeningResult.id)).where(ScreeningResult.verdict == Verdict.FAKE)
    )).scalar_one()

    fraud_rate = ((suspicious + fake) / total_screenings * 100) if total_screenings > 0 else 0.0

    return SystemStats(
        total_users=total_users,
        total_documents=total_docs,
        total_screenings=total_screenings,
        authentic_count=authentic,
        suspicious_count=suspicious,
        fake_count=fake,
        fraud_rate_percent=round(fraud_rate, 2),
    )
