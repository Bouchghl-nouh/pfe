import cv2
import pytesseract
import pyttsx3
import subprocess
from subprocess import call
cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0
def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
text = pytesseract.image_to_string('opencv_frame_0.png')
f = open("demofile4.txt", "w")
f.write(text)
f.close()
subprocess.call("./sound.sh")
