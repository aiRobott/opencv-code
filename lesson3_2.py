"""
Lesson - 3 : Drawing Functions in OpenCV
			 drawing a rectangle
"""

# Import required packages:
import cv2
import numpy as np

# Create a black image 
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5px
cv2.line(img,(0,0),(511,511),(256,0,256),5)

# draw a rectangle greeen box with thickness 3px
cv2.rectangle(img, (384,0),(510,128),(0,255,0),3)

# when everything done, close the windows
cv2.imshow('Drawing',img)
cv2.waitKey(0)
cv2.destroyAllWindows()