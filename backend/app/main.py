# Backend — FastAPI
# Owner: Sumit Kumar Barnwal (core/auth/storage) + Ansh (screening/tasks/tests)

from contextlib import asynccontextmanager
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import init_db, close_mongo_connection
from app.api.routes.auth import router as auth_router
from app.api.routes.documents import router as documents_router
from app.api.routes.screening import router as screening_router
from app.api.routes.admin import router as admin_router

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize MongoDB indexes and pool
    try:
        await init_db()
    except Exception as e:
        logger.warning(f"MongoDB initialization at startup deferred: {e}")
    yield
    # Shutdown: Close MongoDB client connection pool
    try:
        await close_mongo_connection()
    except Exception as e:
        logger.warning(f"Error closing MongoDB connection: {e}")


app = FastAPI(
    title="AI Fake Document Screening API",
    description="AI-powered identity document forgery detection system",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers with v1 prefixes
app.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(documents_router, prefix="/api/v1/documents", tags=["Documents"])
app.include_router(screening_router, prefix="/api/v1/screening", tags=["Screening"])
app.include_router(admin_router, prefix="/api/v1/admin", tags=["Admin"])


@app.get("/")
async def root():
    return {"message": "AI Document Screening API is running", "version": "1.0.0"}


@app.get("/health")
async def health():
    return {"status": "healthy", "database": "mongodb"}
