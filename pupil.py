import cv2
import numpy as np

# load the image
img = cv2.imread('27.bmp')
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


cv2.imshow("godady",fg)
cv2.imwrite("p.png",fg)
cv2.waitKey(0)
