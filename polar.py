import cv2

    

    
img = cv2.imread('final.png')

    
#img2 = cv2.logPolar(img, (img.shape[0]/2, img.shape[1]/2), 40, cv2.WARP_FILL_OUTLIERS)
img3 = cv2.linearPolar(img, (img.shape[0]/2, img.shape[1]/2), 40, cv2.WARP_FILL_OUTLIERS)
    
cv2.imshow('before', img)
#cv2.imshow('logpolar', img2)
cv2.imshow('linearpolar', img3)

cv2.imwrite('polar.png',img3)
    
cv2.waitKey(0)
