# ====================================================
# Owner: Ansh
# File: ml/models/ocr_pipeline/extractor.py
# Responsibilities: OCR text extraction from document images
#   - Support all 5 document types
#   - Use EasyOCR or Tesseract
#   - Extract region-specific text (name, DOB, ID number, etc.)
# ====================================================

# TODO (Ansh): Install: pip install easyocr pytesseract pillow opencv-python

DOCUMENT_FIELDS = {
    "aadhaar": ["name", "dob", "gender", "aadhaar_number", "address"],
    "pan": ["name", "father_name", "dob", "pan_number"],
    "passport": ["surname", "given_names", "passport_number", "nationality", "dob", "expiry_date", "mrz"],
    "driving_license": ["name", "dob", "dl_number", "validity", "vehicle_class"],
    "voter_id": ["name", "relation_name", "dob", "voter_id_number", "assembly_constituency"],
}


class OCRExtractor:
    """
    OCR-based text extractor for identity documents.
    
    Supported engines:
    - EasyOCR (recommended: better for Indian scripts)
    - Tesseract (alternative)
    """
    
    def __init__(self, engine: str = "easyocr", languages: list = None):
        """
        Args:
            engine: 'easyocr' or 'tesseract'
            languages: List of language codes. Default: ['en', 'hi']
        """
        self.engine = engine
        self.languages = languages or ['en', 'hi']
        self.reader = None
        
        # TODO (Ansh): Initialize OCR engine
        # if engine == "easyocr":
        #     import easyocr
        #     self.reader = easyocr.Reader(self.languages)
    
    def extract(self, image_path: str, document_type: str) -> dict:
        """
        Extract text fields from document image.
        
        Args:
            image_path: Path to document image (jpg/png/pdf)
            document_type: One of DOCUMENT_FIELDS keys
        
        Returns:
            dict with extracted fields + confidence scores
        """
        # TODO (Ansh):
        # 1. Load and preprocess image (denoise, deskew, enhance contrast)
        # 2. Run OCR on full image
        # 3. Parse and map text to document fields
        # 4. Return structured dict
        pass
    
    def preprocess_image(self, image_path: str):
        """
        Preprocess image for better OCR accuracy.
        Steps: resize, grayscale, denoise, deskew, threshold
        """
        # TODO (Ansh): Implement using OpenCV
        pass
