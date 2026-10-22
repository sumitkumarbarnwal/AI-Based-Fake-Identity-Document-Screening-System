# ====================================================
# Owner: Ansh
# File: backend/app/services/ocr_service.py
# Responsibilities: Wrap OCR pipeline for API use
#   - Call ml/models/ocr_pipeline/extractor.py
#   - Return structured JSON of extracted fields
# ====================================================

class OCRService:
    """
    Wrapper service that calls the ML OCR pipeline.
    Used by the screening API to extract text from documents.
    """

    async def extract_fields(self, image_path: str, document_type: str) -> dict:
        """
        Extract text fields from a document image.
        
        Args:
            image_path: Path to the document image
            document_type: 'aadhaar' | 'pan' | 'passport' | 'driving_license' | 'voter_id'
        
        Returns:
            {
                "name": "John Doe",
                "dob": "01/01/1990",
                "id_number": "XXXX XXXX XXXX",
                "address": "...",
                "raw_text": "full extracted text",
                "validation": {
                    "name_valid": True,
                    "id_format_valid": True,
                    "dob_valid": True,
                }
            }
        """
        # TODO (Ansh): Call ml/models/ocr_pipeline/extractor.py here
        pass


ocr_service = OCRService()
