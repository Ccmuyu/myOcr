
import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = "D:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

text = pytesseract.image_to_string(Image.open('C:\\Users\\Administrator\\Pictures\\hi.png'))

print(text)

