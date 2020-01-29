#imort the necessary packages
from threading import Thread
import cv2

class WebcamVideoStream:
	
	def __init__(self, src=0):
		# init the video camera stream and read the first frame from the stream
		self.stream = cv2.VideoCapture(src)
		(self.grabbed, self.frame) = self.stream.read()
		# init the variable used to indicate if the thread should be stopped
		self.stopped = False
		
	def start(self):
		
		Thread(args(),target=self.update).start()
		return self
		
	def update(self):
		#keep looping infinitely until the thread is stopped
		while True:
			# if the thread indicator variable is set, stop the thread
			if self.stopped:
				return 
				
				# otherwise, read the next frame from the stream
				(self.grabbed, self.frame) = self.stream.read()
	
	def read(self):
		# return the frame most recently read
		return self.frame
	
	def stop(self):
		# indicate that the thread should be stopped
		self.stopped = True
