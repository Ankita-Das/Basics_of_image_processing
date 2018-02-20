#Harris_Corner_Detection

#The Main Function:cv2.cornerHarris()
#Arguments Used: 4
#They are:
#1.img-Input image which should be grayscale and float32 type
#2.blockSize-size of neighbourhood selected for cornerdetection
#3.ksize-Aperture parameter of Sobel Derivative used
#4.k-Harris Detector free parameter in the equation
import cv2
import numpy as np

filename='eye.jpg'
img=cv2.imread(filename)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray=np.float32(gray)
dst=cv2.cornerHarris(gray,2,3,0.04)

#result is dilated to marking the corners
dst=cv2.dilate(dst,None)

#threshhold for an optimal image,it may vary depending on the image
img[dst>0.01*dst.max()]=[0,255,0]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff==27:
    cv2.destroyAllWindows()
    
