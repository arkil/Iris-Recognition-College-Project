import cv2
import image_slicer
xy=image_slicer.slice('polar.png', 16)
yz=image_slicer.slice('gh.png', 16)
yz=image_slicer.slice('jsk.png', 16)
cv2.imshow("hj",xy)
cv2.imshow("jk",yz)

cv2.waitKey(0)

