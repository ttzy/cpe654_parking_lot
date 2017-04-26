import cv2
import numpy as np
from matplotlib import pyplot as plt

# img_rgb = cv2.imread('stevensEmpty.jpg')
img_rgb = cv2.imread('stevens2.jpg')
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
reps=0
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
    	repeat_flag = 0
    	for i in range(0,len(xs)) :
    		if abs(xs[i] - x) <= 15:
    			if abs(ys[i] - y) <=15 :
    				repeat_flag = 1
    				reps = reps + 1
        if repeat_flag != 1:
	        xs.append(x)
	        print "xs"
	        print xs
	        ys.append(y)
	        print "ys"
	        print ys
	 	    # draw circle at
	        cv2.circle(img_rgb, (x, y), 7, (10, 255, 10), -1) 
        count = 1
        total = total + 1
        x = cxp = cX
        y = cyp = cY
        # cv2.circle(img_rgb, (cX, cY), 7, (255, 255, 255), -1)
cv2.imwrite('res4.png',img_rgb)
free = len(xs)
free_list = []

'''
IMFORMATION WE'RE GIVING TEAM 3
IMAGE = res4.png
COUNT = free
'''
'''Seeing which exactly is free'''
xs2 = [921, 272, 394, 72, 920, 271, 396, 595, 722, 920, 267, 397, 592, 720, 924, 269, 396, 593, 720, 924, 269, 398, 593, 722, 921, 396, 598, 723, 922, 395, 593, 721, 922, 594, 721, 923, 594, 721, 924, 594, 721]
ys2 = [70, 93, 93, 94, 119, 142, 143, 146, 147, 168, 192, 192, 196, 196, 218, 241, 241, 245, 245, 267, 291, 291, 295, 295, 316, 340, 343, 344, 365, 389, 394, 394, 414, 442, 443, 463, 491, 492, 512, 540, 540]

for i in range(len(xs2)):
	if xs2[i] in xs and ys2[i] in ys:
		free_list.append("Free")
	else:
		free_list.append("Occ")

print free_list

'''with open("output.txt", 'w') as write_to:
	for i in range(len(xs)):
		print xs[i] +','+ ys[i],file=write_to
'''

# Working on making it more efficient
# f = open('parking.txt','w+')
# for i in range(len(xs)):
# 	a = str(xs[i]) + ',' + str(ys[i]) +'\n'
# 	print a
# 	f.write(a)
# f.close()

# xs2 = [921, 272, 394, 72, 920, 271, 396, 595, 722, 920, 267, 397, 592, 720, 924, 269, 396, 593, 720, 924, 269, 398, 593, 722, 921, 396, 598, 723, 922, 395, 593, 721, 922, 594, 721, 923, 594, 721, 924, 594, 721]
# ys2 = [70, 93, 93, 94, 119, 142, 143, 146, 147, 168, 192, 192, 196, 196, 218, 241, 241, 245, 245, 267, 291, 291, 295, 295, 316, 340, 343, 344, 365, 389, 394, 394, 414, 442, 443, 463, 491, 492, 512, 540, 540]

# for i in len(xs):
# 	cor = np.where(xs[i], ys[i])
# 	sub_img = 
