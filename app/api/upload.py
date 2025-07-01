from fastapi import APIRouter, File, UploadFile
import shutil
import os
from app.services.image_preprocess import preprocess_image
from app.services.ocr_barcode import extract_text, extract_barcodes
from app.services.fake_detector import predict_fake_or_real


router = APIRouter()

UPLOAD_DIR = "app/static"

@router.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    # Save original file
    file_location = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

# Set processed image path
    processed_path = os.path.join(UPLOAD_DIR, f"processed_{file.filename}")
# Preprocess the image
    preprocess_image(file_location, processed_path)

# OCR and Barcode Detection
    text = extract_text(processed_path)
    barcodes = extract_barcodes(processed_path)
    
# Predict fake or real using dummy AI
    ai_result = predict_fake_or_real(processed_path)

    return {
        "original": file.filename,
        "processed": f"processed_{file.filename}",
        "ocr_text": text,
        "barcodes": barcodes,
        "ai_prediction": {
        "label": "Fake",
        "confidence": 0.87
        },
        "status": "uploaded and processed"
    }