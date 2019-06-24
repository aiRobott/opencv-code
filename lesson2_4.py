"""
Lesson - 2 : Saving Video to a File
"""

# Import required packages:
import cv2

# Capture video from camera 
# and assign it to variable "cap"
cap = cv2.VideoCapture(0)

# define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

# use while loop to capture video frame-by-frame
while(cap.isOpened()):
	# capture frame-by-frame
	ret, frame = cap.read()

	# flip the video
	if ret == True:
		#frame = cv2.flip(frame,0)

		# convert the frame into grayscale
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		frame = cv2.flip(gray,1)

		# write the video to a file
		out.write(frame)

		# display the resulting frame
		#cv2.imshow('Video',frame)
		cv2.imshow('GrayVideo', gray)
		if cv2.waitKey(1) == ord('q'):
			break
	else:
		break

# when everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()