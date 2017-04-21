import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('stevensEmpty.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('skeleton5.jpg',0)
w, h = template.shape[::-1]
print w 
print h
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.827
loc = np.where( res >= threshold)
total = 1
xs = []
ys = []
x=0
y=0
repeat=0
count=0
for pt in zip(*loc[::-1]):
    #cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255,255,255), 2)
    cX = int(pt[0] + w/2)
    cY = int(pt[1] + h/2)
    # get cx and cy from the previous code
    if count == 0 or (abs(cX - cxp) < 112 and abs(cY - cyp) <=51 ):
	    x = x + cX
	    y = y + cY
	    cxp = cX
	    cyp = cY
	    count = count+1
    elif (abs(cX - cxp) > 112) or (abs(cY - cyp) >51):
    	x = x/count
    	y = y/count
    	repeat = 0
    	for i in range(0,len(xs)-1) :
    		if abs(xs[i] - x) <= 15:
    			if abs(ys[i] - y) <=15 :
    				repeat = 1
        if repeat != 1:
	        xs.append(x)
	        print "xs"
	        print xs
	        ys.append(y)
	        print "ys"
	        print ys
	 	    # draw circle at
	        cv2.circle(img_rgb, (x, y), 7, (255, 255, 255), -1) 
        count = 1
        total = total + 1
        x = cxp = cX
        y = cyp = cY
        # cv2.circle(img_rgb, (cX, cY), 7, (255, 255, 255), -1)
cv2.imwrite('res3.png',img_rgb)
# print repeat
print len(xs)
