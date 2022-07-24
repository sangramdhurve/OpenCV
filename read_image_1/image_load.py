import cv2
#we are using 1 for color image and 0 for gray scale image
img = cv2.imread("D:\Projects\OpenCV\Load_image\image_load.py", 1)
img_1 = cv2.imread("D:\Projects\OpenCV\Load_image\image_load.py",0)
print(img)
print(type(img))#it would be numpy array


print(img.shape)#(row, column, channels)
