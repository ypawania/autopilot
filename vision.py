import cv2
import pyautogui
import numpy as np
import time

camera = cv2.VideoCapture(0)

def vision(region):
    frame = pyautogui.screenshot(region=region)
    frame = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2GRAY)
    cv2.imshow("camera read", frame)
    time.sleep(0.3)

while True:
    vision((1250, 295, 200, 90))
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
camera.release()