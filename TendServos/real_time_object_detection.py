# USAGE
# python3 real_time_object_detection.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel
# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
from tendserial import TendSerial
from realtimehelper import RealTimeHelper
import numpy as np
import argparse
import imutils
import time
import cv2


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True,
	help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,
	help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.2,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

rth = RealTimeHelper()

# initialize the list of class labels MobileNet SSD was trained to
# detect, then generate a set of bounding box colors for each class
CLASSES = rth.classes

		
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

# initialize the video stream, allow the cammera sensor to warmup,
# and initialize the FPS counter
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
fps = FPS().start()

frame = vs.read()
frame = imutils.resize(frame, width=1000)
# grab the frame dimensions and convert it to a blob
(h, w) = frame.shape[:2]
rth.setSize(w,h)

#import serial class and open serial port
openCM_comms = TendSerial()
#establish comms with an arduino
try:
	openCM_comms.open_serial()
	# keep going
except: 
	print("[INFO} Failed to open comms...  Check Connection")
	
#move two servos that are being controlled by the OPENCM board... 
if(openCM_comms.openPort == True): 
	# if we successfully opened the serial port 
	# then we can start communicating to the servos
	# if not then just look at the video
	print("[INFO} Success to opened Comm port to OpenCM Board...")

#complete

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=1000)

	# grab the frame dimensions and convert it to a blob
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
		0.007843, (300, 300), 127.5)

	# pass the blob through the network and obtain the detections and
	# predictions
	net.setInput(blob)
	detections = net.forward()
	
	#create a line with the realtimehelper class
	rth.create_line(frame)

	totalUp = 0
	totalDown = 0
	# loop over the detections
	for i in np.arange(0, detections.shape[2]):
		# extract the confidence (i.e., probability) associated with
		# the prediction
		confidence = detections[0, 0, i, 2]
		centroids = np.zeros((detections.shape[2], 2), dtype="int")
		
		# filter out weak detections by ensuring the `confidence` is
		# greater than the minimum confidence
		if confidence > args["confidence"]:
			# extract the index of the class label from the
			# `detections`, then compute the (x, y)-coordinates of
			# the bounding box for the object
			idx = int(detections[0, 0, i, 1])
							# if the class label is not a person, ignore it
			if CLASSES[idx] != "person":
				continue
			
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")
			cX = int((startX + endX) / 2.0)
			cY = int((startY + endY) / 2.0)
			centroids[i] = (cX, cY)
			
			# draw the prediction on the frame
			label = "{}: {:.2f}%".format(CLASSES[idx],
				confidence * 100)
			cv2.rectangle(frame, (startX, startY), (endX, endY),
				COLORS[idx], 2)
			y = startY - 15 if startY - 15 > 15 else startY + 15
			cv2.putText(frame, label, (startX, y),
				cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
				
			for centroid in centroids:
				direction = centroid[0]
			
				if centroid.any():
					# if the direction is negative (indicating the object
					# is moving up) AND the centroid is above the center
					# line, count the object
					if direction < w // 2: # and centroid[1] < H // 2:
						totalUp += 1

					# if the direction is positive (indicating the object
					# is moving down) AND the centroid is below the
					# center line, count the object
					elif direction > w // 2 :# and centroid[1] > H // 2:
						totalDown += 1
				cv2.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)


	# construct a tuple of information we will be displaying on the
	# frame
	info = [
		("left", totalUp),
		("right", totalDown),
	]
	
	# loop over the info tuples and draw them on our frame
	rth.create_text(frame,info)

	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

	# update the FPS counter
	fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
