import cv2
import numpy as np

cap=cv2.VideoCapture(0)


while(True):
    c,f=cap.read()
    l_b=np.array([50,100,100])
    
    u_b=np.array([255,255,255])
    
    hsv = cv2.cvtColor(f, cv2.COLOR_BGR2HSV)
    
    mask=cv2.inRange(hsv,l_b,u_b)
    
    res=cv2.bitwise_and(f,f,mask=mask)
    
    cv2.imshow('f',f)
    cv2.imshow('m',mask)
    cv2.imshow('r',res)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
cv2.destroyAllWindows()
