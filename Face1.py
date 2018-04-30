# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 16:30:29 2018

@author: Tushar
"""
import cv2

# importing the xml file containing the info about the face 

face_clf=cv2.CascadeClassifier('face.xml')

# import the image

img=cv2.imread('photo.jpg')

img2=cv2.imread('news.jpg')
# convert the bgr image into gray

gr_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gr_img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# detecting the face 

face=face_clf.detectMultiScale(gr_img,scaleFactor=1.1,minNeighbors=5)

face2=face_clf.detectMultiScale(gr_img2,scaleFactor=1.1,minNeighbors=5)
# making  an rectangle across the face

for x,y,w,h in face:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,10),2)

for x,y,w,h in face2:
    img2=cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,10),2)
    
# Resize the image

re_img=cv2.resize(img,(500,500))

re_img2=cv2.resize(img2,(500,500))

# Display the image

cv2.namedWindow('Face Detection',cv2.WINDOW_NORMAL)
cv2.imshow("Face Detection",re_img)

cv2.namedWindow('Face Detection 2',cv2.WINDOW_NORMAL)
cv2.imshow("Face Detection 2",re_img2)

# wait for processing

cv2.waitKey(0)

# Delete the Window

cv2.destroyAllWindows()

    
