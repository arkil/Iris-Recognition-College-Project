import cv2
import numpy as np

# load the image
img = cv2.imread('9.bmp')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# detect circles
gray = cv2.medianBlur(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY), 5)
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,30.0,param1=50,param2=110,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))

# draw mask
mask = np.full((img.shape[0], img.shape[1]), 0, dtype=np.uint8)  # mask is only 
for i in circles[0, :]:
    cv2.circle(mask, (i[0], i[1]), i[2], (255, 255, 255), -1)

# get first masked value (foreground)
fg = cv2.bitwise_and(img, img, mask=mask)


#cv2.imshow("godady",fg)
cv2.imwrite("p.png",fg)
cv2.waitKey(0)


import cv2
import numpy as np

# load the image
img = cv2.imread('9.bmp')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# detect circles
gray = cv2.medianBlur(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY), 5)
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,2,100.0,param1=30,param2=150,minRadius=90,maxRadius=140)
circles = np.uint16(np.around(circles))

# draw mask
mask = np.full((img.shape[0], img.shape[1]), 0, dtype=np.uint8)  # mask is only 
for i in circles[0, :]:
    cv2.circle(mask, (i[0], i[1]), i[2], (255, 255, 255), -1)

# get first masked value (foreground)
fg = cv2.bitwise_and(img, img, mask=mask)


#cv2.imshow("masked",fg)
cv2.imwrite("m.png",fg)


pic1 = cv2.imread('p.png')
pic2 = cv2.imread('m.png')
mask_ab = cv2.bitwise_xor(pic2, pic1)

#cv2.imshow('abc',mask_ab)
cv2.imwrite('final.png',mask_ab)


cv2.waitKey(0)

import cv2

    

    
img = cv2.imread('final.png')

    
#img2 = cv2.logPolar(img, (img.shape[0]/2, img.shape[1]/2), 40, cv2.WARP_FILL_OUTLIERS)
img3 = cv2.linearPolar(img, (img.shape[0]/2, img.shape[1]/2), 40, cv2.WARP_FILL_OUTLIERS)
    
#cv2.imshow('before', img)
#cv2.imshow('logpolar', img2)
#cv2.imshow('linearpolar', img3)

cv2.imwrite('polar.png',img3)
    
cv2.waitKey(0)

#!/usr/bin/env python
 
import numpy as np
import cv2
 
def build_filters():
 filters = []
 ksize = 31
 for theta in np.arange(0, np.pi, np.pi / 16):
     kern = cv2.getGaborKernel((ksize, ksize), 4.0, theta, 10.0, 0.5, 0, ktype=cv2.CV_32F)
     kern /= 1.5*kern.sum()
     filters.append(kern)
 return filters
 
def process(img, filters):
 accum = np.zeros_like(img)
 for kern in filters:
     fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
     np.maximum(accum, fimg, accum)
 return accum
 
if __name__ == '__main__':
 img=cv2.imread('polar.png')
 
 filters = build_filters()
 
 res1 = process(img, filters)
 cv2.imshow('result', res1)
 cv2.imwrite("gh.png",res1)
 cv2.waitKey(0)
 cv2.destroyAllWindows()

import cv2
import image_slicer
xy=image_slicer.slice('polar.png', 16)
yz=image_slicer.slice('gh.png', 16)
cv2.waitKey(0)
