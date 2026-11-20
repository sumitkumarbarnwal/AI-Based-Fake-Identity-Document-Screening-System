import uuid
from datetime import datetime, timezone
import enum
from pydantic import BaseModel, Field


class DocumentType(str, enum.Enum):
    AADHAAR = "aadhaar"
    PAN = "pan"
    PASSPORT = "passport"
    DRIVING_LICENSE = "driving_license"
    VOTER_ID = "voter_id"
    UNKNOWN = "unknown"


class DocumentStatus(str, enum.Enum):
    PENDING = "pending"       # Uploaded, awaiting analysis
    PROCESSING = "processing" # ML pipeline running
    COMPLETED = "completed"   # Analysis done
    FAILED = "failed"         # Processing error


class Document(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str
    original_filename: str
    stored_filename: str
    file_path: str
    file_size: int  # bytes
    mime_type: str
    document_type: DocumentType = DocumentType.UNKNOWN
    status: DocumentStatus = DocumentStatus.PENDING
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    def to_mongo(self) -> dict:
        d = self.model_dump()
        d["_id"] = d.pop("id")
        return d

    @classmethod
    def from_mongo(cls, data: dict):
        if not data:
            return None
        data = dict(data)
        if "_id" in data and "id" not in data:
            data["id"] = str(data["_id"])
        return cls(**data)

    def __repr__(self) -> str:
        return f"<Document id={self.id} type={self.document_type} status={self.status}>"
