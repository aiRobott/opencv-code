"""
Lesson - 3 : Drawing Functions in OpenCV
			 drawing a line
"""

# Import required packages:
import cv2
import numpy as np

# Create a black image 
#img = np.zeros((512,512,3), np.uint8)

img = cv2.imread('messi5.jpg')

# Draw a diagonal blue line with thickness of 5px
cv2.line(img,(0,0),(548,342),(0,0,255),5)

# when everything done, close the windows
cv2.imshow('Drawing',img)
cv2.waitKey(0)
cv2.destroyAllWindows()