import numpy as np
import cv2
from matplotlib import pyplot as plt
import time as t
print("OpenCV Version : %s " % cv2.__version__)

def convertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  
#load cascade classifier training file for haarcascade
haar_object_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_alt.xml')


#load test iamge
test1 = cv2.imread('images/IMG_6295.JPG')


#convert the test image to gray image as opencv object detector expects gray images
gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)

plt.imshow(convertToRGB(test1))
plt.show()

plt.imshow(gray_img, cmap='gray')
#plt.show()

objects = haar_object_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

#print the number of objects found
print('Objects found: ', len(objects))

#go over list of objects and draw them as rectangles on original colored img
for (x, y, w, h) in objects:
    cv2.rectangle(test1, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
#convert image to RGB and show image
plt.imshow(convertToRGB(test1))
plt.show()
