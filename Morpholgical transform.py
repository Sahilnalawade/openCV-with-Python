# -*- coding: utf-8 -*-
#"""
#Created on Mon May 15 17:05:44 2017
#
#@author: Sahil
#"""
# Morphological - remove noise 
# Erosion - Erodes the small pixels (averaging)
# Dialation - Opposite to erosion (dialates the small pixel)
#Opening - remove false positive (remove things from background)
#Closing - remove  flase negative (remove things from the image noise)
#Tophat - diff. between image and opeing of the image
#Blackhat- diff. between closing of image and input image

import cv2
import numpy as np

img=cv2.imread('redcap.jpg')
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lr=np.array([50,50,50])
ur=np.array([255, 255, 255])
mask=cv2.inRange(hsv,lr,ur)
res=cv2.bitwise_and(img,img,mask=mask)
kernel = np.ones((5,5),np.uint8)
erosion=cv2.erode(mask,kernel,iterations=1)
dilation=cv2.dilate(mask,kernel,iterations=1)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
tophat=cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)
blackhat=cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow('img',img)
cv2.imshow('res',res)
cv2.imshow('erosion',erosion)
cv2.imshow('dilation',dilation)
cv2.imshow('opening',opening)
cv2.imshow('closing',closing)
cv2.imshow('tophat',tophat)
cv2.imshow('blackhat',blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()
