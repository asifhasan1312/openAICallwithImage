import PIL
from PIL import Image
#import Image
from pytesseract import pytesseract
import enum
import os

class OprSys(enum.Enum):
    def __str__(self):
        return str(self.value)
    Mac = 0
    Windows = 1
    
class Language(enum.Enum):
    def __str__(self):
        return str(self.value)
    ENG = 'eng'
    RUS = 'rus'
    ITA = 'ita'
    
class ImageReader:
    def __init__(self):
        window_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pytesseract.tesseract_cmd = window_path
            
    def extract_text(self, image: str, lang: str) -> str:
        # You can check if the file is located in this directory
        if os.path.exists(image): 
            # only if this file exists in this location do we continue
            print('The file exists!')
            with open(image) as f:
                img = Image.open(image)
                extracted_text = pytesseract.image_to_string(img, lang=lang)
                return extracted_text
        else:
            return False
            
        
