import cv2
from PIL import Image
from pytesseract import pytesseract
import keyboard
import time

camera=cv2.VideoCapture(0)
_,image=camera.read()
cv2.imshow('Text detection', image)
if cv2.waitKey(1)& 0xFF==ord('s'):
    cv2.imwrite('test1.jpg', image)

time.sleep(10)
camera.release()
cv2.destroyAllWindow()
def tesseract():
    path_to_tesseract=f"C:\\Users\\neera\\PycharmProjects\\AI Friday\\Database\\tesseract-ocr-w64-setup-5.3.0.20221222 (1).exe"
    Imagepath= 'test1.jpg'
    pytesseract.tesseract_cmd= path_to_tesseract
    text=pytesseract.image_to_string(Image.open(Imagepath))
    print(text[:-1])

tesseract()