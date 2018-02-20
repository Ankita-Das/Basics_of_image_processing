#FloodFill Algorithm to join the similar points
#cv.FloodFill(image, seed_point, new_val, lo_diff=(0, 0, 0, 0), up_diff=(0, 0, 0, 0), flags=4, mask=None) → comp

#https://www.tutorialspoint.com/computer_graphics/polygon_filling_algorithm.html
#https://docs.opencv.org/2.4/modules/imgproc/doc/miscellaneous_transformations.html

import cv2
import numpy as np

# read image, ensure binary
img = cv2.imread('original,JPG', 0)
#img[img!=0] = 255

# flood fill background to find inner holes
holes = img.copy()
cv2.floodFill(holes, None, (0, 0), 255)

# invert holes mask, bitwise or with img fill in holes
holes = cv2.bitwise_not(holes)
filled_holes = cv2.bitwise_or(img, holes)
cv2.imshow('', filled_holes)
cv2.waitKey()
