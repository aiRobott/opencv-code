"""
Lesson - 1 : using matplotlib
"""

# Import required packages:
import cv2
from matplotlib import pyplot as plt

# Load an color image in grayscale
img = cv2.imread('messi5.jpg', 0)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')

# to hide tick values on X and Y axis
plt.xticks([]), plt.yticks([])
plt.show()