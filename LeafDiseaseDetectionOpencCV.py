
import numpy as np
import cv2

impath="C:\\Users\\sbyog\\Downloads\\misc\\misc\\leaf5.jpg"
img=cv2.imread(impath,1)


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#Green Color
low = np.array([1,60,20])
high = np.array([80, 255, 255])
image_mask = cv2.inRange(hsv, low, high)        
output = cv2.bitwise_and(img, img, mask = image_mask)

hsv = cv2.cvtColor(output, cv2.COLOR_BGR2HSV)
low = np.array([30,40,40])
high = np.array([200, 255, 255])
image_mask = cv2.inRange(hsv, low, high)  
output1 = cv2.bitwise_and(img, img, mask = image_mask)      


cv2.imshow("Image mask", image_mask)
cv2.imshow("Original leaf img", img)
cv2.imshow("leafonly", output)
cv2.imshow("leaf with out inf", output1)


l = 0
for i in range(output.shape[0]):
    for j in range(output.shape[1]):
        b = output[i][j][1]
        if (b!=0):
            l += 1
print(l)        

inf = 0 
for i in range(output1.shape[0]):
    for j in range(output1.shape[1]):
        b = output1[i][j][1]
        if (b!=0):
            inf += 1
print(inf)
infleaf=l-inf
perofinf=(infleaf/l)*100
perofhealthy=100-perofinf
print(infleaf)
print("% of leaf infected \033[1;31;47m",perofinf)
print("\033[0m% of leaf healthy  \033[1;32;47m",perofhealthy)

        
#cv2.imshow('leaf',img)
#cv2.imshow('leaf1',th1)
#cv2.imshow('leaf2',th2)
#cv2.imshow('leaf3',blur1)
#cv2.imshow('leaf4',Canny)
cv2.imshow('leaf5',hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()