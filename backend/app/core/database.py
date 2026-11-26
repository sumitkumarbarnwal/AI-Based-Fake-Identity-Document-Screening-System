import logging
from typing import Optional
from pymongo import ASCENDING
try:
    from pymongo import AsyncMongoClient
except ImportError:
    try:
        from motor.motor_asyncio import AsyncIOMotorClient as AsyncMongoClient
    except ImportError:
        AsyncMongoClient = None

from app.core.config import settings

logger = logging.getLogger(__name__)

class MongoDBManager:
    client: Optional[AsyncMongoClient] = None
    db = None

db_manager = MongoDBManager()


def get_client() -> AsyncMongoClient:
    """Return the global AsyncMongoClient instance, initializing if necessary."""
    if db_manager.client is None:
        db_manager.client = AsyncMongoClient(settings.MONGODB_URL)
        db_manager.db = db_manager.client[settings.MONGODB_DB_NAME]
    return db_manager.client


def get_database():
    """Return the active MongoDB database instance."""
    if db_manager.db is None:
        get_client()
    return db_manager.db


async def get_db():
    """
    FastAPI dependency that provides access to the MongoDB database per request.
    
    Usage:
        @router.get("/example")
        async def example(db = Depends(get_db)):
            doc = await db["users"].find_one({"email": email})
    """
    db = get_database()
    yield db


async def init_db():
    """
    Ensure all required MongoDB collections and unique/lookup indexes are created.
    Called once during application startup.
    """
    db = get_database()
    try:
        # Users indexes
        await db["users"].create_index([("email", ASCENDING)], unique=True)
        await db["users"].create_index([("username", ASCENDING)], unique=True)

        # Documents indexes
        await db["documents"].create_index([("stored_filename", ASCENDING)], unique=True)
        await db["documents"].create_index([("user_id", ASCENDING)])
        await db["documents"].create_index([("created_at", -1)])

        # Screening results indexes
        await db["screening_results"].create_index([("document_id", ASCENDING)], unique=True)
        await db["screening_results"].create_index([("user_id", ASCENDING)])
        await db["screening_results"].create_index([("verdict", ASCENDING)])
        await db["screening_results"].create_index([("created_at", -1)])
        logger.info("MongoDB collections and indexes initialized successfully.")
    except Exception as e:
        logger.error(f"Error initializing MongoDB indexes: {e}")
        raise


async def close_mongo_connection():
    """Close the MongoDB client connection cleanly on application shutdown."""
    if db_manager.client is not None:
        await db_manager.client.close()
        db_manager.client = None
        db_manager.db = None
        logger.info("MongoDB connection closed.")
