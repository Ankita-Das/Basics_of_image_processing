#Thresholding
#ADAPTIVE_THRESH_MEAN)C:mean of neighbourhood gives thrshold value
#ADAPTIVE_THRESH_GAUSSIAN_C:threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.

#cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
#C is the constant to be subtracted from mean/weighted mean
#For more details:https://www.tutorialspoint.com/opencv/opencv_adaptive_threshold.htm




import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('original.JPG',0)
img=cv2.GaussianBlur(img,(5,5),0)

ret,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)


titles=['Original Image','Global Thresholding','Adaptive_mean','Adaptive_gaussian']
images=[img,th1,th2,th3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
