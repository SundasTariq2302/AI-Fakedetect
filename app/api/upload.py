from fastapi import APIRouter, File, UploadFile
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "app/static"

@router.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "status": "uploaded"}
