import cv2
import numpy as np

img =cv2.imread('j.png')

kernel=np.ones((5,5),np.uint8)
er=cv2.erode(img,kernel,iterations=1)
dil=cv2.dilate(img,kernel,iterations=1)
op=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
cl=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
gd=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
bh=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
tp=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)

cv2.imshow('img',img)
cv2.imshow('erossion',er)
cv2.imshow('dilate',dil)
cv2.imshow('open',op)
cv2.imshow('close',cl)
cv2.imshow('gradient',gd)
cv2.imshow('blackhat',bh)
cv2.imshow('Top hat',tp)
cv2.waitKey(0)
cv2.destroyAllWindows()