# ====================================================
# Owner: Ansh
# File: ml/models/document_classifier/classifier.py
# Responsibilities: Classify document type from image
#   - Input: raw document image
#   - Output: Aadhaar | PAN | Passport | DL | Voter ID + confidence
# ====================================================

DOCUMENT_TYPES = ["aadhaar", "pan", "passport", "driving_license", "voter_id"]


class DocumentClassifier:
    """
    Classifies the type of an identity document from its image.
    
    Approach options (TODO Ansh - choose best):
    Option A: CNN-based (MobileNetV3 / EfficientNet-B0) — fast, accurate
    Option B: Template matching + layout analysis — simpler baseline
    Option C: CLIP zero-shot classification — no training data needed
    
    Recommended: Option A (MobileNetV3 fine-tuned on document dataset)
    """
    
    def __init__(self, model_path: str = None):
        self.model = None
        self.classes = DOCUMENT_TYPES
        # TODO (Ansh): Load trained model from model_path
    
    def classify(self, image_path: str) -> dict:
        """
        Classify document type.
        
        Returns:
            {
                "document_type": "aadhaar",
                "confidence": 0.97,
                "all_scores": {
                    "aadhaar": 0.97,
                    "pan": 0.01,
                    "passport": 0.01,
                    "driving_license": 0.005,
                    "voter_id": 0.005,
                }
            }
        """
        # TODO (Ansh): Preprocess image → run through model → return top class
        pass
    
    def preprocess(self, image_path: str):
        """Resize to 224×224, normalize to ImageNet stats."""
        # TODO (Ansh): Implement using torchvision transforms
        pass
