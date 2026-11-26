import uuid
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
import enum
from pydantic import BaseModel, Field


class Verdict(str, enum.Enum):
    AUTHENTIC = "authentic"
    SUSPICIOUS = "suspicious"
    FAKE = "fake"
    INCONCLUSIVE = "inconclusive"


class ScreeningResult(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    document_id: str
    user_id: str

    # ML pipeline outputs
    verdict: Verdict
    confidence_score: float  # 0.0–1.0
    forgery_score: Optional[float] = None        # from CNN model
    ocr_validation_score: Optional[float] = None # from validator

    # Structured JSON results
    ocr_fields: Optional[Dict[str, Any]] = None
    # e.g. {"name": "John", "dob": "01/01/1990", "id_number": "XXXX XXXX XXXX"}

    fraud_indicators: Optional[List[Any]] = None
    # e.g. [{"type": "photo_tampering", "detected": True, "score": 0.87}]

    validation_errors: Optional[List[Any]] = None
    # e.g. [{"field": "dob", "error": "Invalid date format"}]

    processing_time_ms: Optional[float] = None
    error_message: Optional[str] = None

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

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
        return f"<ScreeningResult id={self.id} verdict={self.verdict} confidence={self.confidence_score:.2f}>"
