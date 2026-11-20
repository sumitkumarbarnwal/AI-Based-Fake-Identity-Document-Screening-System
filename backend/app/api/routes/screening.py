# ====================================================
# Owner: Ansh
# File: backend/app/api/routes/screening.py
# Responsibilities: Trigger ML analysis, fetch results, history
# ====================================================
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status
from app.core.database import get_db
from app.core.security import get_current_user_id
from app.models.screening_result import ScreeningResult

router = APIRouter()

# TODO (Ansh): Implement the following endpoints:
# POST /analyze         → Trigger ML pipeline on a document (async via Celery)
# GET  /result/{id}     → Get detailed screening result (fraud score, OCR fields, indicators)
# GET  /history         → Get paginated list of user's past screenings
# GET  /stats           → Dashboard stats: total, fraud_count, success_rate

@router.post("/analyze")
async def analyze_document(
    doc_id: str,
    background_tasks: BackgroundTasks,
    current_user_id: str = Depends(get_current_user_id),
    db = Depends(get_db),
):
    """Trigger ML analysis on an uploaded document. (Ansh)"""
    # TODO: Dispatch to Celery task queue or run inline
    return {"message": "Screening analysis queued", "doc_id": doc_id}

@router.get("/result/{result_id}")
async def get_screening_result(
    result_id: str,
    current_user_id: str = Depends(get_current_user_id),
    db = Depends(get_db),
):
    """Retrieve detailed ML screening result. (Ansh)"""
    doc = await db["screening_results"].find_one({"_id": result_id, "user_id": current_user_id})
    if not doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Screening result not found")
    return ScreeningResult.from_mongo(doc)

@router.get("/history")
async def get_screening_history(
    page: int = 1,
    limit: int = 10,
    current_user_id: str = Depends(get_current_user_id),
    db = Depends(get_db),
):
    """Get paginated screening history for current user. (Ansh)"""
    offset = (page - 1) * limit
    total = await db["screening_results"].count_documents({"user_id": current_user_id})
    cursor = (
        db["screening_results"]
        .find({"user_id": current_user_id})
        .sort("created_at", -1)
        .skip(offset)
        .limit(limit)
    )
    docs = await cursor.to_list(length=limit)
    items = [ScreeningResult.from_mongo(d) for d in docs]
    return {"items": items, "total": total, "page": page, "limit": limit}

@router.get("/stats")
async def get_stats(
    current_user_id: str = Depends(get_current_user_id),
    db = Depends(get_db),
):
    """Get screening statistics for dashboard. (Ansh)"""
    total = await db["screening_results"].count_documents({"user_id": current_user_id})
    fraud_count = await db["screening_results"].count_documents({
        "user_id": current_user_id,
        "verdict": {"$in": ["suspicious", "fake"]}
    })
    success_rate = ((total - fraud_count) / total * 100) if total > 0 else 100.0
    return {"total": total, "fraud_count": fraud_count, "success_rate": round(success_rate, 2)}
