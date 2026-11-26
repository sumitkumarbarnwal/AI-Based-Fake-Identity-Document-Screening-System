from fastapi import APIRouter, Depends, HTTPException, status, Query
from pydantic import BaseModel
from datetime import datetime, timezone
from typing import Optional, List

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
    db = Depends(get_db),
) -> User:
    """Dependency that ensures the caller is an admin."""
    doc = await db["users"].find_one({"_id": current_user_id})
    if not doc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required",
        )
    user = User.from_mongo(doc)
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
    items: List[UserAdminResponse]
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
    db = Depends(get_db),
):
    """List all users in the system (admin only, paginated)."""
    offset = (page - 1) * limit

    total = await db["users"].count_documents({})
    cursor = (
        db["users"]
        .find({})
        .sort("created_at", -1)
        .skip(offset)
        .limit(limit)
    )
    docs = await cursor.to_list(length=limit)
    users = [User.from_mongo(d) for d in docs]

    return PaginatedUsers(items=users, total=total, page=page, limit=limit)


@router.get("/users/{user_id}", response_model=UserAdminResponse)
async def get_user(
    user_id: str,
    admin: User = Depends(require_admin),
    db = Depends(get_db),
):
    """Get a specific user's details (admin only)."""
    doc = await db["users"].find_one({"_id": user_id})
    if not doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return User.from_mongo(doc)


@router.patch("/users/{user_id}", response_model=UserAdminResponse)
async def update_user(
    user_id: str,
    payload: UpdateUserRequest,
    admin: User = Depends(require_admin),
    db = Depends(get_db),
):
    """Update a user's role or active status (admin only)."""
    doc = await db["users"].find_one({"_id": user_id})
    if not doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    user = User.from_mongo(doc)

    update_fields = {}
    if payload.is_active is not None:
        user.is_active = payload.is_active
        update_fields["is_active"] = payload.is_active
    if payload.role is not None:
        user.role = payload.role
        update_fields["role"] = payload.role.value if hasattr(payload.role, "value") else str(payload.role)

    if update_fields:
        update_fields["updated_at"] = datetime.now(timezone.utc)
        user.updated_at = update_fields["updated_at"]
        await db["users"].update_one({"_id": user_id}, {"$set": update_fields})

    return user


@router.get("/documents", response_model=dict)
async def list_all_documents(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    admin: User = Depends(require_admin),
    db = Depends(get_db),
):
    """List all documents across all users (admin only, paginated)."""
    offset = (page - 1) * limit
    total = await db["documents"].count_documents({})
    cursor = (
        db["documents"]
        .find({})
        .sort("created_at", -1)
        .skip(offset)
        .limit(limit)
    )
    docs = await cursor.to_list(length=limit)
    return {
        "items": [
            {
                "id": str(d.get("_id") or d.get("id")),
                "user_id": d.get("user_id"),
                "original_filename": d.get("original_filename"),
                "document_type": d.get("document_type"),
                "status": d.get("status"),
                "created_at": str(d.get("created_at")),
            }
            for d in docs
        ],
        "total": total,
        "page": page,
        "limit": limit,
    }


@router.get("/documents/flagged", response_model=dict)
async def list_flagged_documents(
    admin: User = Depends(require_admin),
    db = Depends(get_db),
):
    """List all documents screened as suspicious or fake (admin only)."""
    cursor = (
        db["screening_results"]
        .find({"verdict": {"$in": [Verdict.SUSPICIOUS.value, Verdict.FAKE.value]}})
        .sort("created_at", -1)
        .limit(100)
    )
    flagged = await cursor.to_list(length=100)
    return {
        "items": [
            {
                "result_id": str(r.get("_id") or r.get("id")),
                "document_id": r.get("document_id"),
                "user_id": r.get("user_id"),
                "verdict": r.get("verdict"),
                "confidence_score": r.get("confidence_score"),
                "fraud_indicators": r.get("fraud_indicators"),
                "created_at": str(r.get("created_at")),
            }
            for r in flagged
        ],
        "total": len(flagged),
    }


@router.get("/stats", response_model=SystemStats)
async def get_system_stats(
    admin: User = Depends(require_admin),
    db = Depends(get_db),
):
    """Overall system statistics for the admin dashboard."""
    total_users = await db["users"].count_documents({})
    total_docs = await db["documents"].count_documents({})
    total_screenings = await db["screening_results"].count_documents({})

    authentic = await db["screening_results"].count_documents({"verdict": Verdict.AUTHENTIC.value})
    suspicious = await db["screening_results"].count_documents({"verdict": Verdict.SUSPICIOUS.value})
    fake = await db["screening_results"].count_documents({"verdict": Verdict.FAKE.value})

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
