#!/usr/bin/env python

import serial
import time
import os
import termios
import cv2
import datetime
import threading


class TendSerial(): 
	
	def __init__(self): 
		self.mystr = "hello"
		self.row1 = []
		self.row2 = []
		self.openPort = False
		self.freq = 3
		self.right = 0
		self.left = 0
		
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
				
	def hello(self,s): 
		print('hello {} ({:.4f})'.format(s,time.time()))
		time.sleep(.3)
		
	def do_every(self,period,f,*args):
		def g_tick():
			t = time.time()
			count = 0
			while True:
				count += 1
				yield max(t + count*period - time.time(),0)
		g = g_tick()
		while True:
			time.sleep(next(g))
			f(*args)
	
	def send_serial(self): 
		# if time is greater than the sendTime
		# send which ever right or left is greater
		if(self.right > self.left): 
			send = 'r'
		elif(self.left > self.right): 
			send = 'l'
		else: 
			send = 'e'
		print(send)
		return
		#self.ser.write(send.encode()) 
		
	def send_thread(self): 
		timerThread = threading.Thread(target=lambda: self.do_every(self.freq,self.send_serial))
		timerThread.daemon = True
		timerThread.start()
		

if __name__ == "__main__": 
	count = 0
	tserial = TendSerial() 
	#tserial.do_every(1,tserial.send_serial,0,1)

	#threadmy = threading.Thread(target=lambda: do_every(5, hello,'foo')).start()
	tserial.send_thread()

	while True:
		count = count + 1
		if(count > 20000): 
			tserial.right = 2
			print(count)
			count = 0
			
		key = cv2.waitKey(1) & 0xFF
		
		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break


	
