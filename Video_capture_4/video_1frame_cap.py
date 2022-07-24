#this will capture first frame of video.
import cv2, time
# we can replace the path with zero
video = cv2.VideoCapture(0)#zero for buil in camera, 1 for secondry, 2 for third party cam.

check, frame = video.read()# check is bool data type, frame is numpy array, will return True when video is working else Flase.

print(check)
print(frame)
time.sleep(3)#for time dely of camera
cv2.imshow('Capturing', frame)
cv2.waitkey(0)
video.release()

cv2.destroyAllWindows