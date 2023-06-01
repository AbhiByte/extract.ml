from PIL import Image
from pytesseract import pytesseract
import enum

class OS(enum.Enum):
    Mac = 0
    Windows = 1


class Languages(enum.Enum):
    ENG = 'eng'
    RUS = 'rus'
    ITA = 'ita'

class ImageReader:
    def __init__(self, os: OS):
        if os == OS.Mac:
            #Tesseract already installed via homebrew
            print('Running on: MAC\n')

        if os == OS.Windows:
            windows_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            pytesseract.tesseract_cmd = windows_path
            print('Running on: WINDOWS\n')
    def extract_text(self, image:str, lang:Languages) -> str:
        img = Image.open(image)
        extracted_text = pytesseract.image_to_string(img, lang=lang.value)
        return extracted_text

if __name__ == '__main__':
    ir = ImageReader(OS.Mac)
    text = ir.extract_text('images/test.png', Languages.ENG)
    print(text)
