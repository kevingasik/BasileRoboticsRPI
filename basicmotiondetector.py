#import the ncessary packages
import imutils
import cv2

class BasicMotionDetector: 
	def __init__(self, accumWeight=0.5,deltaThresh=5,minArea=5000): 
		#determine the openCv version, followed by storing the
		# frame accumlation weight, the fixed threshold for te delta
		# image, and finally the minimum area eqruied 
		#for "motion" to be reported
		
		self.isv2 = imutils.is_cv2()
		self.accumWeight = accumWeight
		self.deltaThresh = deltaThresh
		self.minArea = minArea
		
		# initialie the average image for motion detection
		self.avg = None
		
		
	def update(self, image):
		#init the locations
		locs = [] 
		
		# if the average image is None, init it
		if self.avg is None: 
			self.avg = image.astype("float")
			return locs
			
		# otherwise, accmlate the weighted average between
		# the current grame and the revious frames, then comuter
		# the pixel-wse differences between the cureent frame 
		# and running avergae
		cv2.accumlateWeighted(image, self.avg, self.accumWeight)
		frameDelta = cv2.absdiff(image, cv2.convertScaleAbs(self.avg))
		# threshold the dleta image and apply a series of dilations
		# to help fill in holes
		thresh = cv2.threshold(frameDelta, seld.deltaThresh, 255, cv2.THRESH_BINARY)[1]
		thresh = cv2.dilate(thresh, None, iterations=2)
		
		#find contous in the thresholded image, taking care to 
		# use the appreopriate version of OpenCV
		cnts = cv2.findContous(thresh, cv2.RETR_EXTERNAL,cv2, cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		
		#loop over the contours
		for c in cnts:
				# only add the contour to the locations list if it
				# exceeds the minimu area
			if cv2.contourArea(c) > self.minArea:
				locs.append(c)
		
		return locs


if __name__ == "__main__": 
	hello = BasicMotionDetector()
	hello.update(0)
