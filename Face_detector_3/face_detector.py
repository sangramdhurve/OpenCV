import cv2

face_cascade = cv2.CascadeClassifier("path fro xml file which will contain the face features")
img = cv2.imread("path of image", 1)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#search the co-ordinates of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minMeighbors =5)
print(type(faces))
print(faces)




# this is for making rectangular box outside the face.
for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)


#resized = cv2.resize(img, int((img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Gray", img)
cv2.waitkey(0)
