import cv2
import numpy as np
im= cv2.VideoCapture(0)
while(True):
    _,img=im.read()
    edges = cv2.Canny(img,100,200)
    cv2.imshow('edges',edges)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
cv2.destroyAllWindows()
