import os
import uuid
import shutil
import aiofiles
from pathlib import Path
from typing import Optional
from fastapi import HTTPException, status

from app.core.config import settings


class StorageService:
    """
    Handles file storage operations.
    Currently uses local disk; can be swapped for S3/Cloudinary
    by overriding save() and delete().
    """

    def __init__(self, base_dir: str = None):
        self.base_dir = Path(base_dir or settings.UPLOAD_DIR)
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def get_user_dir(self, user_id: str) -> Path:
        """Get (and create) the per-user upload directory."""
        user_dir = self.base_dir / user_id
        user_dir.mkdir(parents=True, exist_ok=True)
        return user_dir

    async def save(self, content: bytes, user_id: str, extension: str) -> tuple[str, str]:
        """
        Save raw bytes to disk with a UUID filename.

        Returns:
            (stored_filename, absolute_file_path)
        """
        filename = f"{uuid.uuid4()}.{extension}"
        file_path = self.get_user_dir(user_id) / filename

        async with aiofiles.open(file_path, "wb") as f:
            await f.write(content)

        return filename, str(file_path)

    def delete(self, file_path: str) -> bool:
        """
        Delete a file from disk.

        Returns:
            True if file was deleted, False if it didn't exist.
        """
        path = Path(file_path)
        if path.exists():
            path.unlink()
            return True
        return False

    def get_file_url(self, user_id: str, filename: str) -> str:
        """
        Return a URL/path to serve the file.
        With local storage this is the relative path; swap for S3 URL if using cloud.
        """
        return f"/uploads/{user_id}/{filename}"

    def file_exists(self, file_path: str) -> bool:
        return Path(file_path).exists()


# Singleton
storage_service = StorageService()
