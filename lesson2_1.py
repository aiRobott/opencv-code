"""
Lesson - 2 : Capture Video from Camera
"""

# Import required packages:
import cv2

# Capture video from camera 
# and assign it to variable "cap"
cap = cv2.VideoCapture(0)

# use while loop to capture video frame-by-frame
while True:
	# capture frame-by-frameq
	ret, frame = cap.read()

	# convert the frame into grayscale
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# display the resulting frame
	cv2.imshow('Video',frame)
	cv2.imshow('GrayVideo', gray)
	if cv2.waitKey(1) == ord('q'):
		break

# when everything done, release the capture
cap.release()
cv2.destroyAllWindows()