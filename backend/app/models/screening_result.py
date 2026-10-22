import uuid
from datetime import datetime, timezone
from sqlalchemy import String, Float, ForeignKey, DateTime, Enum as SAEnum, JSON, Text
from sqlalchemy.orm import Mapped, mapped_column
import enum

from app.core.database import Base


class Verdict(str, enum.Enum):
    AUTHENTIC = "authentic"
    SUSPICIOUS = "suspicious"
    FAKE = "fake"
    INCONCLUSIVE = "inconclusive"


class ScreeningResult(Base):
    __tablename__ = "screening_results"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    document_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("documents.id", ondelete="CASCADE"),
        nullable=False, unique=True, index=True
    )
    user_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False, index=True
    )

    # ML pipeline outputs
    verdict: Mapped[Verdict] = mapped_column(SAEnum(Verdict), nullable=False)
    confidence_score: Mapped[float] = mapped_column(Float, nullable=False)  # 0.0–1.0
    forgery_score: Mapped[float] = mapped_column(Float, nullable=True)       # from CNN model
    ocr_validation_score: Mapped[float] = mapped_column(Float, nullable=True) # from validator

    # Structured JSON results
    ocr_fields: Mapped[dict] = mapped_column(JSON, nullable=True)
    # e.g. {"name": "John", "dob": "01/01/1990", "id_number": "XXXX XXXX XXXX"}

    fraud_indicators: Mapped[list] = mapped_column(JSON, nullable=True)
    # e.g. [{"type": "photo_tampering", "detected": True, "score": 0.87}]

    validation_errors: Mapped[list] = mapped_column(JSON, nullable=True)
    # e.g. [{"field": "dob", "error": "Invalid date format"}]

    processing_time_ms: Mapped[float] = mapped_column(Float, nullable=True)
    error_message: Mapped[str] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )

    def __repr__(self) -> str:
        return f"<ScreeningResult id={self.id} verdict={self.verdict} confidence={self.confidence_score:.2f}>"
