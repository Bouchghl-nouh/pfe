from time import sleep
#from espeak import espea
import pyttsx3
import pytesseract
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera, camera
camera = PiCamera()
camera.resolution = (1200,680)
camera.framerate = 50


camera.start_preview()


# for i in range(1,3):
#     sleep(10)
#     camera.capture('/home/pi/Desktop/image%s.jpg' % i)
# camera.stop_preview()
img = cv2.imread('/home/pi/Desktop/image2.jpeg')
text = pytesseract.image_to_string(img)
print(text)
engine = pyttsx3.init();
engine.setProperty('voice','french')
engine.setProperty("rate",140)
engine.say(text)
engine.runAndWait()
for voice in engine.getProperty('voices'):
    print (voice.id)