# Backend — FastAPI
# Owner: Sumit Kumar Barnwal (core/auth/storage) + Ansh (screening/tasks/tests)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Fake Document Screening API",
    description="AI-powered identity document forgery detection system",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import routers
# from app.api.routes.auth import router as auth_router
# from app.api.routes.documents import router as documents_router
# from app.api.routes.screening import router as screening_router
# from app.api.routes.admin import router as admin_router

# app.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"])
# app.include_router(documents_router, prefix="/api/v1/documents", tags=["Documents"])
# app.include_router(screening_router, prefix="/api/v1/screening", tags=["Screening"])
# app.include_router(admin_router, prefix="/api/v1/admin", tags=["Admin"])

@app.get("/")
async def root():
    return {"message": "AI Document Screening API is running", "version": "1.0.0"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
