import cv2
import numpy as np
from matplotlib import pyplot as plt
img_rgb = cv2.imread('stevensEmpty.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('skeleton5.jpg',0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.825
loc = np.where( res >= threshold)
#Cx is each element
#Cy is each element
#previous_Cx
#previous_Cy
#X is total if difference is small enough
#Y is total if difference is small enough
#count is counter

for pt in zip(*loc[::-1]):
    #cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255,255,255), 2)
    cX = int(pt[0] + w/2)
    cY = int(pt[1] + h/2)
    cv2.circle(img_rgb, (cX, cY), 7, (255, 255, 255), -1)
cv2.imwrite('res.png',img_rgb)