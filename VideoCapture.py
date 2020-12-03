# -*- coding: utf-8 -*-
import cv2
import winsound
frequency = 2500 
duration = 1000

from PlateExtraction import extraction
from OpticalCharacterRecognition import ocr
from OpticalCharacterRecognition import check_if_string_in_file

cap = cv2.VideoCapture(0)
while(True):
    ret,frame = cap.read()
    plate = extraction(frame)
    try:
        text = ocr(plate)
    except:
        continue
        
    if text != '':
        print(text,end=" ")
        if check_if_string_in_file(r'C:\Users\sonia\Desktop\AutomaticNumberPlateRecognition\Database\Database.txt', text) and text != "":
            print('Registered')
            winsound.Beep(frequency, duration)
        else:
            print('Not Registered')
        
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
