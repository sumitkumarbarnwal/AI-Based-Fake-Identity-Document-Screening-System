import uuid
from datetime import datetime, timezone
import enum
from pydantic import BaseModel, Field


class UserRole(str, enum.Enum):
    USER = "user"
    ADMIN = "admin"


class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: str
    username: str
    full_name: str
    hashed_password: str
    role: UserRole = UserRole.USER
    is_active: bool = True
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
        return f"<User id={self.id} email={self.email} role={self.role}>"
