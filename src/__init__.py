import pytesseract

from PIL import Image


pytesseract.pytesseract.tesseract_cmd = "D:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
jpg = "C:\\Users\\Administrator\\Pictures\\hi.png"
# jpg = "F:\\a1.png"
text = pytesseract.pytesseract.image_to_string(Image.open(jpg))

print(text)
