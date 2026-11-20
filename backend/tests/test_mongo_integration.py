import pytest
import uuid
from datetime import datetime, timezone
from app.models.user import User, UserRole
from app.models.document import Document, DocumentType, DocumentStatus
from app.models.screening_result import ScreeningResult, Verdict


def test_user_model_mongo_conversion():
    uid = str(uuid.uuid4())
    now = datetime.now(timezone.utc)
    user = User(
        id=uid,
        email="test@example.com",
        username="testuser",
        full_name="Test User",
        hashed_password="hashed_secret",
        role=UserRole.USER,
        is_active=True,
        created_at=now,
        updated_at=now,
    )
    
    mongo_doc = user.to_mongo()
    assert mongo_doc["_id"] == uid
    assert "id" not in mongo_doc
    assert mongo_doc["email"] == "test@example.com"
    assert mongo_doc["username"] == "testuser"
    assert mongo_doc["role"] == UserRole.USER

    # Deserialization from MongoDB
    hydrated = User.from_mongo(mongo_doc)
    assert hydrated.id == uid
    assert hydrated.email == "test@example.com"
    assert hydrated.role == UserRole.USER


def test_document_model_mongo_conversion():
    doc_id = str(uuid.uuid4())
    user_id = str(uuid.uuid4())
    doc = Document(
        id=doc_id,
        user_id=user_id,
        original_filename="sample_aadhaar.jpg",
        stored_filename="stored_sample.jpg",
        file_path="/tmp/stored_sample.jpg",
        file_size=1024,
        mime_type="image/jpeg",
        document_type=DocumentType.AADHAAR,
        status=DocumentStatus.PENDING,
    )
    
    mongo_doc = doc.to_mongo()
    assert mongo_doc["_id"] == doc_id
    assert "id" not in mongo_doc
    assert mongo_doc["user_id"] == user_id
    assert mongo_doc["document_type"] == DocumentType.AADHAAR

    hydrated = Document.from_mongo(mongo_doc)
    assert hydrated.id == doc_id
    assert hydrated.document_type == DocumentType.AADHAAR
    assert hydrated.status == DocumentStatus.PENDING


def test_screening_result_model_mongo_conversion():
    res_id = str(uuid.uuid4())
    doc_id = str(uuid.uuid4())
    user_id = str(uuid.uuid4())
    
    result = ScreeningResult(
        id=res_id,
        document_id=doc_id,
        user_id=user_id,
        verdict=Verdict.AUTHENTIC,
        confidence_score=0.95,
        forgery_score=0.02,
        ocr_validation_score=0.98,
        ocr_fields={"name": "Alice", "dob": "01/01/1990"},
        fraud_indicators=[],
    )
    
    mongo_doc = result.to_mongo()
    assert mongo_doc["_id"] == res_id
    assert mongo_doc["verdict"] == Verdict.AUTHENTIC
    assert mongo_doc["confidence_score"] == 0.95

    hydrated = ScreeningResult.from_mongo(mongo_doc)
    assert hydrated.id == res_id
    assert hydrated.verdict == Verdict.AUTHENTIC
    assert hydrated.ocr_fields["name"] == "Alice"


@pytest.mark.asyncio
async def test_mock_mongo_collection_operations():
    """Verify in-memory dictionary-based simulation of PyMongo async API patterns."""
    collection = {}
    
    # Insert
    user_id = str(uuid.uuid4())
    user_data = {
        "_id": user_id,
        "email": "agent@example.com",
        "username": "agent007",
        "role": "user",
    }
    collection[user_id] = user_data
    
    # Find one by id
    found = collection.get(user_id)
    assert found is not None
    assert found["email"] == "agent@example.com"
    
    # Count
    assert len(collection) == 1
    
    # Delete
    del collection[user_id]
    assert collection.get(user_id) is None
