import cv2,time
import numpy as np

# Reading the images

img=cv2.imread('123.jpg')
img2=cv2.imread('478517276.jpg')

#Resize for blending

img2=cv2.resize(img2,(450,470))

#Blending

f=cv2.addWeighted(img,0.5,img2,0.5,0.5)

# Rows and column ogf images

row1,col1,_=img.shape
row,col,_=f.shape
#  Translation

m=np.float32([[1,0,100],[0,1,50]])
f2=cv2.warpAffine(f,m,(col,row))

#Rotation (180)

m2=cv2.getRotationMatrix2D((col/2,row/2),180,1)
f3=cv2.warpAffine(img,m2,(col1,row1))

#Showing the images

cv2.imshow('rot',f3)
cv2.imshow('uu',f)
cv2.imshow('uu3',f2)
cv2.imshow('nnn',img2)
cv2.imshow('im',img)
k=cv2.waitKey(0)
if k==ord('q'):
    cv2.destroyAllWindows()
