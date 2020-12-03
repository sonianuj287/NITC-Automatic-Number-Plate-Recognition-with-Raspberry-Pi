import cv2
import winsound
frequency = 2500 
duration = 1000

from PlateExtraction import extraction
from OpticalCharacterRecognition import ocr
from OpticalCharacterRecognition import check_if_string_in_file

image = cv2.imread(r'C:\Users\sonia\Desktop\AutomaticNumberPlateRecognition\CarPictures\010.jpg')
plate = extraction(image)
text = ocr(plate)
text = ''.join(e for e in text if e.isalnum())
print(text, end=" ")
if check_if_string_in_file(r'C:\Users\sonia\Desktop\AutomaticNumberPlateRecognition\Database\Database.txt', text) and text != "":
    print('Registered')
    winsound.Beep(frequency, duration)
else:
    print("Not Registered")