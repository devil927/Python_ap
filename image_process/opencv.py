# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 02:20:27 2018

@author: Tushar
"""
# Import the libraries
import cv2
import glob

# list of images
imgs=glob.glob('*.jpg')

#for black and whie and resizing
for img in imgs:
    im=cv2.imread(img,0) # 0 is for greyish
    re_im=cv2.resize(im,(100,100))
    cv2.imshow('resized_'+img,re_im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('resized_'+img,re_im)
    
