# -*- coding: utf-8 -*-
#"""
#Created on Sat Apr 29 16:18:43 2017
#
#@author: Sahil
#"""
import cv2
import numpy as np

img=cv2.imread('bookpage.jpg')
retval, threshold=cv2.threshold(img,12,255,cv2.THRESH_BINARY)

grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2, threshold=cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)
gaus=cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
retval, otsu=cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('img',img)
cv2.imshow('threshold',threshold)
cv2.imshow('gaus',gaus)
cv2.imshow('otsu',otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()