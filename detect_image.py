
# Setup
# Run this:
# !pip3 install opencv-python

import numpy as np
import cv2
from matplotlib import pyplot as plt
import time as t
print("OpenCV Version : %s " % cv2.__version__)

def convertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  
#load cascade classifier training file for haarcascade
#haar_object_cascade = cv2.CascadeClassifier('classifiers/watch.xml')
haar_object_cascade = cv2.CascadeClassifier('classifiers/hotdog_cascade.xml')

#load test iamge
#img = cv2.imread('images/image01.jpg')
img = cv2.imread('images/image02.jpg')
#img = cv2.imread('images/image03.jpg')
#img = cv2.imread('images/image04.jpg')


#convert the test image to gray image as opencv object detector expects gray images
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(convertToRGB(img))
plt.show()

plt.imshow(gray_img, cmap='gray')
#plt.show()

objects = haar_object_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=10)

#print the number of objects found
print('Objects found: ', len(objects))

font = cv2.FONT_HERSHEY_SIMPLEX

if len(objects) > 0:
  text = "HOTDOG!"
  # get boundary of this text
  textsize = cv2.getTextSize(text, font, 4, 2)[0]

  # get coords based on boundary
  textX = int((img.shape[1] - textsize[0]) / 2)
  textY = int((img.shape[0] + textsize[1]) / 2)
  cv2.putText(img, text, (textX, textY ), font, 4, (11, 255, 255), 10, cv2.LINE_AA)
  

  #go over list of objects and draw them as rectangles on original colored img
  for (x, y, w, h) in objects:
      cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
else:
  text = "NOT HOTDOG!"
  # get boundary of this text
  textsize = cv2.getTextSize(text, font, 7, 2)[0]

  # get coords based on boundary
  textX = int((img.shape[1] - textsize[0]) / 2)
  textY = int((img.shape[0] + textsize[1]) / 2)
  cv2.putText(img, text, (textX, textY ), font, 7, (11, 255, 255), 10, cv2.LINE_AA)
  
#convert image to RGB and show image
plt.imshow(convertToRGB(img))
plt.show()


