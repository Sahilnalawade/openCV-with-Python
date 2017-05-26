# -*- coding: utf-8 -*-
#"""
#Created on Fri Apr 28 20:39:12 2017
#
#@author: Sahil
#"""
import cv2
import numpy as np
import math

filename = "a.jpg"
oriimage = cv2.imread(filename)

newx,newy = oriimage.shape[1]/4,oriimage.shape[0]/4#new size (w,h)
newx1=math.ceil(newx)
newy1=math.ceil(newy)
img1 = cv2.resize(oriimage,(newx1,newy1))

filename = "b.jpg"
oriimage = cv2.imread(filename)

newx,newy = oriimage.shape[1]/4,oriimage.shape[0]/4#new size (w,h)
newx1=math.ceil(newx)
newy1=math.ceil(newy)
img2 = cv2.resize(oriimage,(newx1,newy1))

rows,cols,channels=img2.shape
roi=img1[0:rows,0:cols]
# Load two images
img3 = cv2.addWeighted(img1,0.5,img2,0.9,0)
img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)

mask_inv=cv2.bitwise_not(mask)

img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_fg=cv2.bitwise_and(img2,img2,mask=mask)

dst=cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols]=dst
    
cv2.imshow('res',img2)
cv2.imshow('dst',dst)
cv2.imshow('img1Z_bg',img1_bg)
cv2.imshow('img2_fg',img2_fg)
cv2.imshow('mask_inv',mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()