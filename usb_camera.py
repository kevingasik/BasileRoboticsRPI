#import the necessary packages

from __future__ import print_function
from basicmotiondetector import BasicMotionDetector
from imutils.video import VideoStream
import numpy as np
import datetime
import datetime
import imutils
import time
import cv2
import argparse

#init the video streams and all them to warump
print("[INFO] starting camera...")
#webcam1 = VideoStream(src=0).start()

#ap = argparse.ArgumentParser()
#ap.add_argument("-p","--picamera", type=int, default=-1,help="weather or not the pi cam should be used")
#args = vars(ap.parse_args())

stream = VideoStream().start()

motion = BasicMotionDetector()
total = 0

time.sleep(2.0)


while True: 
	frames = []
	
	#loop over the frames and their detectors
	if stream and motion: #((webcam,camMotion))
		#read the next frame and resize it to have a max width of 400 pixels

		
		frame = stream.read()
		frame = imutils.resize(frame, width=500)
		
		# convert the frame to grayscale, blue it slightly, update the motion detector
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray, (21,21),0)
		locs = motion.update(gray)
		
		
		# we should allow the motion detector to run for a bit 
		# and then accumlate a set of frame to form a nice avergage
		#if total < 32: 
		#	frames.append(frame)
		#	print("hello1")
		#	continue
			#otherwise check to see if motion was detected
		
		if len(locs) > 0:
			#init the minimum and maximum xy coords
			(minX, minY) = (np.inf, np.inf)
			(maxX, maxY) = (-np.inf,-np.inf)

			#loop over the ocations of motion and accumulate the minimum and maximum locations of the bounding boxes
			for l in locs:
				(x, y, w,h) = cv2.boundingRect(l)
				(minX, maxX) = (min(minX, x), max(maxX, x + w))
				(minY, maxY) = (min(minY, y), max(maxY, y +h))
				
			cv2.rectangle(frame, (minX, minY), (maxX, maxY),(0,0,255), 3)
			
		frames.append(frame)
		total += 1
		timestamp = datetime.datetime.now()
		ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
	
	#loop over the frames a second time
	for(frame,name) in zip(frames, ("stream")):
		# draw the timestamp on the frame and display it
		cv2.putText(frame, ts, (10, frame.shape[0] - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0,0,255),1)
		cv2.imshow(name,frame)
		
	#check to see if a key was pressed
	key = cv2.waitKey(1) & 0xFF
		
	#if the 'q' was pressed, break from the loop
	if key==ord("q"):
		break
			
# cleanup
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
stream.stop()



