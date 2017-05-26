# -*- coding: utf-8 -*-
#"""
#Created on Mon May 15 17:35:05 2017
#
#@author: Sahil
#"""

# EDGE DETECTION and Gradient
import cv2
import numpy as np
img=cv2.imread('redcap.jpg')
laplacian=cv2.Laplacian(img,cv2.CV_64F)
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
edges=cv2.Canny(img,100,200)

cv2.imshow('img',img)
cv2.imshow('laplacian',laplacian)
cv2.imshow('sobelx',sobelx)
cv2.imshow('sobely',sobely)
cv2.imshow('edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
