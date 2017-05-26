# -*- coding: utf-8 -*-
#"""
#Created on Tue May 16 20:04:46 2017
#
#@author: Sahil
#"""
#
import cv2
import numpy as np

img_rgb = cv2.imread('template.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template1 = cv2.imread('sample.jpg',0)
w, h = template1.shape[::-1]

res = cv2.matchTemplate(img_gray,template1,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow('Detected',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()