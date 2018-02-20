import cv2
import numpy as pyplot
from matplotlib import pyplot as plt

img=cv2.imread('original.JPG')
#blur=cv2.blur(img,(5,5))
gauss_blur=cv2.GaussianBlur(img,(5,5),0)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])
#plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
#plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(gauss_blur),plt.title('Gaussian_blur')
plt.xticks([]),plt.yticks([])
plt.show()
