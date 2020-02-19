#!/usr/bin/env python

import serial
import time
import os
import termios
import cv2


class TendSerial(): 
	
	def __init__(self): 
		self.mystr = "hello"
		self.row1 = []
		self.row2 = []
		self.openPort = False
		self.time_elapsed = time.time()
		self.sendTime = 15
		
	def open_serial(self): 
		port='/dev/ttyAMA0'
		#port='/dev/ttyACM0'
		with open(port) as f:
			attrs = termios.tcgetattr(f)
			attrs[2] = attrs[2] & ~termios.HUPCL
			termios.tcsetattr(f, termios.TCSAFLUSH,attrs)
    
		self.ser = serial.Serial(
			port='/dev/ttyACM0',
			baudrate = 9600,
			parity = serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE,
			bytesize=serial.EIGHTBITS,
			timeout=1
		)	

		self.ser.close()
		self.ser.open()
		self.ser.reset_input_buffer()
		self.ser.reset_output_buffer()
		self.ser.close()
		self.ser.open()
		
		self.openPort = True
		return
		
	def send_serial(self, right, left): 
		# if time is greater than the sendTime
		# send which ever right or left is greater
		
		start = time.time()
		print("hello")
		end = time.time()
		print(end - start)
		
		if(self.time_elapsed > self.sendTime): 
			if(right > left): 
				send = right
			elif(left > right): 
				send = left
			else: 
				send = equal
		#self.ser.write(send.encode()) 
		


if __name__ == "__main__": 
	tserial = TendSerial() 
	#myany.open_serial()
	while True:
		tserial.send_serial(0,1)
		key = cv2.waitKey(1) & 0xFF
		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break


	
