import fitz  # PyMuPDF
import pytesseract
import numpy as np
import dagster as dg

from PIL import Image, ImageEnhance

from langchain_postgres import PGVector

# Read Pdf from file.
pdf_path = "documents/test_pdf/test_ocr-3.pdf"
doc = fitz.open(pdf_path)

# # Function to apply thresholding
# def apply_threshold(img):
#     # Convert to grayscale
#     img_gray = img.convert('L')
    
#     # Apply a simple threshold to create a binary image (black and white)
#     img_thresholded = img_gray.point(lambda p: p > 180 and 255)  # Simple thresholding at 180
    
#     return img_thresholded

# # Loop through the pages in the PDF
# for page_num in range(len(doc)):
#     page = doc[page_num]

#     # Render page as an image
#     pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x DPI scaling for higher resolution
#     img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

#     # Apply thresholding to improve text contrast
#     img_thresholded = apply_threshold(img)

#     # Enhance the image contrast (improves legibility)
#     enhancer = ImageEnhance.Contrast(img_thresholded)
#     img_enhanced = enhancer.enhance(2)  # Increase contrast by a factor of 2

#     # Run OCR with Thai language and improved configuration
#     custom_config = r'--oem 3 --psm 6'  # OCR Engine Mode and Page Segmentation Mode
#     text = pytesseract.image_to_string(img_enhanced, lang="tha+eng", config=custom_config)

#     print(f"Page {page_num + 1} OCR Output:\n{text}\n")


# Design to Loading PDF and Convert Them to Vector Database and Database.
@dg.asset(
    name="PDF_Loader",
)
def pdf_loader():
    pass

@dg.asset(
    name="PDF_Extraction"
)
def pdf_extraction():
    pass

@dg.asset(
    name="PDF_Embedding"
)
def pdf_embedding():
    pass

@dg.asset(
    name="PDF_Vector_database"
)
def pdf_vector_database():
    pass