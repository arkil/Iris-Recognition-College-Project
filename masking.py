import cv2
import numpy as np
pic1 = cv2.imread('p.png')
pic2 = cv2.imread('m.png')
mask_ab = cv2.bitwise_xor(pic2, pic1)

cv2.imshow('abc',mask_ab)
cv2.imwrite('final.png',mask_ab)


cv2.waitKey(0)