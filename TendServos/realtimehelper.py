from imutils.video import VideoStream
import datetime
import argparse
import imutils
import time
import cv2


class RealTimeHelper(): 
	
	def __init__(self): 
		self.hello = "hello World" 
		self.width = 0
		self.height = 0
		self.classes = ["background", "aeroplane", "bicycle", "bird", "boat",
			"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
			"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
			"sofa", "train", "tvmonitor"]
			
	def setSize(self, width, height): 
		self.width = width
		self.height = height
		
	def create_line(self, frame): 
		cv2.line(frame, (self.width // 2, self.height ), (self.width // 2, 0), (0, 255, 0), 2)
		cv2.line(frame, (self.width // 2 + 2, self.height ), (self.width // 2 + 2, 0), (0, 128, 0), 2)
		cv2.line(frame, (self.width // 2 - 2, self.height ), (self.width // 2 - 2, 0), (0, 128, 0), 2)
		
	def create_text(self,frame,info):	
		# loop over the info tuples and draw them on our frame
		for (i, (k, v)) in enumerate(info):
			text = "{}: {}".format(k, v)
			cv2.putText(frame, text, (self.width // 4 + i*self.width//2 - 30, self.height - (20)),
			cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 255), 2)

	
	#def create_text(self): 
		
