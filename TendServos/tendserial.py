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
		self.freq = 15
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
	
	def send_serial(self, right, left): 
		# if time is greater than the sendTime
		# send which ever right or left is greater
		if(right > left): 
			send = 'r'
		elif(left > right): 
			send = 'l'
		else: 
			send = 'e'
		print(send)
		return
		#self.ser.write(send.encode()) 
		
	def do_everyTwo(self,freq,right,left):
		next_call = time.time()
		while True:
			print (datetime.datetime.now())
			next_call = next_call + freq;
			time.sleep(next_call - time.time())
			self.send_serial(right,left)
			
	def foo(self):
		global next_call
		print (datetime.datetime.now())
		next_call = next_call+1
		threading.Timer( next_call - time.time(), self.foo ).start()

	def send_thread(self): 
		timerThread = threading.Thread(target=tserial.do_everyTwo(self.freq,self.right,self.left))
		timerThread.daemon = True
		timerThread.start()


if __name__ == "__main__": 
	count = 0
	tserial = TendSerial() 
	#tserial.do_every(1,tserial.send_serial,0,1)
	#tserial.send_thread()
	next_call = time.time()
	tserial.foo()
	
	#myany.open_serial()
	while True:
		#tserial.send_serial(0,1)
		next_call = time.time()
		
		
		count = count + 1
		print(count)
		if(count > 20000): 
			tserial.right = 2
			print(count)
		key = cv2.waitKey(1) & 0xFF
		
		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break


	
