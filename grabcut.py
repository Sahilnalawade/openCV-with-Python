# -*- coding: utf-8 -*-
# Grab Cut and fore ground extraction

import cv2
import numpy as np
import matplotlib.pyplot as plt

img1=cv2.imread('a.jpg')
img=cv2.resize(img1,(500,500))
 
mask=np.zeros(img.shape[:2],np.uint8)

bgdmodel=np.zeros((1,65),np.float64)
fgdmodel=np.zeros((1,65),np.float64)
rect=(60,70,450,250)#size of image(10%, 10% , 90 %, 90%)

cv2.grabCut(img,mask,rect,bgdmodel,fgdmodel,5,cv2.GC_INIT_WITH_RECT)
mask2=np.where((mask==2)|(mask==0),0,1).astype('uint8')
img=img*mask2[:,:,np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()