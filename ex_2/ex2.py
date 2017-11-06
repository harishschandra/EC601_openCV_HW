import cv2

pic = cv2.imread('C:/Users/harish/pic_1.png') 

[b,g,r] = cv2.split(pic) #split into color channels

cv2.imshow('Blue',b)
cv2.imwrite('Blue.png',b)
cv2.imshow('Red',r) 
cv2.imwrite('Red.png',r)
cv2.imshow('Green',g)
cv2.imwrite('Green.png',g)

hsv_pic = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV) #convert to HSV

[h,s,v] = cv2.split(hsv_pic) #split into HSV channells

cv2.imshow('Hue',h)
cv2.imwrite('Hue.png',h)
cv2.imshow('Saturation',s)
cv2.imwrite('Saturation.png',s)
cv2.imshow('Value',v)
cv2.imwrite('Value.png',v)

YCC_pic = cv2.cvtColor(pic, cv2.COLOR_BGR2YCR_CB) #convert to YCrCb

[y,Cb,Cr] = cv2.split(YCC_pic) #split YCrCb channels

cv2.imshow('Y',y)
cv2.imwrite('Y.png',y)
cv2.imshow('Cb',Cb)
cv2.imwrite('Cb.png',Cb)
cv2.imshow('Cr',Cr)
cv2.imwrite('Cr.png',Cr)

print(r[20][25])
print(g[20][25])
print(b[20][25])

print(y[20][25])
print(Cb[20][25])
print(Cr[20][25])

print(h[20][25])
print(s[20][25])
print(v[20][25])

#cv2.waitKey(0)