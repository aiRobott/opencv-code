"""
Lesson - 3 : Drawing Functions in OpenCV
			 drawing a Polygon
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

# draw a red circle with filling
cv2.circle(img,(447,63),63,(0,0,255),-1)

# drawing ellipse
cv2.ellipse(img, (256,256),(100,50),0,0,180,255,-1)

# draw polygon in yellow color
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True, (0,255,0))

# when everything done, close the windows
cv2.imshow('Drawing',img)
cv2.waitKey(0)
cv2.destroyAllWindows()