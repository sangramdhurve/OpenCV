#this will capture video.
import cv2, time

from cv2 import cvtColor
# we can replace the path with zero
video = cv2.VideoCapture(0)#zero for buil in camera, 1 for secondry, 2 for third party cam.
a = 1
while True:
    a = a + 1
    check, frame = video.read()# check is bool data type, frame is numpy array, will return True when video is working else Flase.
    print(frame)
    gray = cv2,cvtColor(frame, cv2.COLOR_BGR2GRAY)
    time.sleep(3)#for time dely of camera
    cv2.imshow('Capturing', frame)
    key = cv2.waitkey(1)
    if key ==ord('q'):
        break
video.release()

cv2.destroyAllWindows