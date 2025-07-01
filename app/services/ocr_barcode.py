import cv2
import pytesseract
from pyzbar.pyzbar import decode

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(image_path: str) -> str:
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text.strip()

def extract_barcodes(image_path: str) -> list:
    image = cv2.imread(image_path)
    barcodes = decode(image)
    results = []

    for barcode in barcodes:
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type
        results.append({"type": barcode_type, "data": barcode_data})

    return results