import cv2
import requests
from gpiozero import Buzzer, LED
from time import sleep
#import winsound
frequency = 2500 
duration = 1000
buzzer = Buzzer(2)
led = LED(3)

from PlateExtraction import extraction
from OpticalCharacterRecognition import ocr
from OpticalCharacterRecognition import check_if_string_in_file

cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 8)

while(True):
    ret,frame = cap.read()
    plate = extraction(frame)
    if plate is not None:
        
        try:
            text = ocr(plate)
            text = ''.join(e for e in text if e.isalnum())
        except:
            continue
            
        if text != '':
            print(text,end=" ")
            # To check in file
            if check_if_string_in_file('./Database/Database.txt', text):
                buzzer.off()
                led.off()
                print('Registered')
                #winsound.Beep(frequency, duration)
            # To check on server using api
            
            #url = 'https://www.example.com/demopage.php'
            #formData = {'plate': text }
            #response = requests.post(url, json = formData)
            
            #if response:
            #    buzzer.off()
            #    led.off()
            #    print('Registered')
            else:
                buzzer.on()
                led.on()
                print('Not Registered')
            
    cv2.imshow('frame',plate)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
