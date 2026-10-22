# ====================================================
# Owner: Sumit Kumar Barnwal
# File: backend/app/api/routes/admin.py
# Responsibilities: Admin-only routes for user & doc management
# ====================================================
from fastapi import APIRouter

router = APIRouter()

# TODO (Sumit): Implement admin endpoints:
# GET /users            → List all users (paginated)
# GET /users/{id}       → Get a specific user
# PATCH /users/{id}     → Update user role/status (deactivate, promote to admin)
# GET /documents        → List all uploaded documents across all users
# GET /documents/flagged → List all documents with suspicious/fake results

@router.get("/users")
async def list_users(page: int = 1, limit: int = 20):
    """List all users. Admin only. (Sumit)"""
    pass

@router.get("/documents")
async def list_all_documents(page: int = 1, limit: int = 20):
    """List all documents in the system. Admin only. (Sumit)"""
    pass

@router.get("/documents/flagged")
async def list_flagged_documents():
    """List all flagged/suspicious documents. Admin only. (Sumit)"""
    pass
