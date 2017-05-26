# -*- coding: utf-8 -*-
#"""
#Created on Thu May 11 19:35:47 2017
#
#@author: Sahil
#"""
#
import cv2
import numpy as np

img=cv2.imread('redcap.jpg')
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lr=np.array([50,50,50])
ur=np.array([255, 255, 255])
mask=cv2.inRange(hsv,lr,ur)
res=cv2.bitwise_and(img,img,mask=mask)
kernel=np.ones((15,15),np.float32)/255
smoothed=cv2.filter2D(res,-1,kernel)
blur=cv2.GaussianBlur(res,(15,15),0)
median=cv2.medianBlur(res,15)
bilateral=cv2.bilateralFilter(res,15,75,75)

cv2.imshow('img',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.imshow('blur',blur)
cv2.imshow('median',median)
cv2.imshow('smoothed',smoothed)
cv2.imshow('bilateral',bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
