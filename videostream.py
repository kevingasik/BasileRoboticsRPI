# import the ncessary packages

from webcamvideostream import WebcamVideoStream

class VideoStream: 
	def __init__(self, src=0,usePiCamera=False, resolution=(320,240),framerate=32):
		#check to see if the picamera module should be used
		if usePiCamera:
			from pivideostream import PiVideoStream
			self.stream = PiVideoStream(resolution=resolution, framerate=framerate)
		else:
			self.stream = WebcamVideoStream(src=src)
			
		def start(self):
			#start the threaded video stream
			return self.stream.start()
		
		def update(self):
			#grab the next frame from the stream
			self.stream.update()
			
		def read(self):
			#return the current frame
			return self.stream.read()
		
		def stop(self):
			# stop the thread and release any resources
			self.stream.stop()

if __name__ =="__main__":
	videos = VideoStream()
