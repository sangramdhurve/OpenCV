import cv2


img = cv2.imread("path of image", 1)
#resized = cv2.resize(img, (600,600)) # it was a demo for checking of resize
resized = cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Legend", resized)
cv2.waitkey(0) # for pressing any key it will disappease
#cv2.waitkey(2000) #it keep runninng till 2k mili seconds.

cv2.destroyAllWindows() # for clossing all windows.