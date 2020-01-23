#!/usr/bin/env python

import serial
import time
import os
import termios


class Animation(): 
	
	def __init__(self): 
		self.mystr = "hello"
		self.row1 = []
		self.row2 = []
		
	def open_serial(self): 
		port='/dev/ttyAMA0'
		#port='/dev/ttyACM0'
		with open(port) as f:
			attrs = termios.tcgetattr(f)
			attrs[2] = attrs[2] & ~termios.HUPCL
			termios.tcsetattr(f, termios.TCSAFLUSH,attrs)
    
		self.ser = serial.Serial(
			port='/dev/ttyACM0',
			baudrate = 115200,
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
		
		return
		
	def generate_order(self,order):
		#sides in
		if(order == 0):
			self.row1 = [0,1,2,3,4,5,6,7,8,9,10,11]
			self.row2 = [23,22,21,20,19,18,17,16,15,14,13,12]
		if(order == 1):
			self.row1 = [17,16,15,14,13,12]
			self.row2 = [23,22,21,20,19,18]
			 
	def dance_up(self,row): 
		delay = 0
		#lets dance our windows
		#What should it look like?
		#goToE {addr} {%between 2 and 3} {speed} {time delay}
		#row1,row2 = self.generate_order(0)
		
		if(row == 1):
			for item in self.row1:
				delay = delay + 1000
				position = 95
				speed = 30
				print(item)
			
				data = "goToE {} {} {} {}\r\n".format(item,position,speed,delay)
				self.ser.write(data.encode())
				read_ser = self.ser.readline().decode()
				time.sleep(0.1)
				print (read_ser)
		if(row == 2):
			for item in self.row2:
				delay = delay + 1000
				position = 95
				speed = 30
				print(item)
	
				data = "goToE {} {} {} {}\r\n".format(item,position,speed,delay)
				self.ser.write(data.encode())
				read_ser = self.ser.readline().decode()
				time.sleep(0.1)
				print (read_ser)			
		return
		
		
	def dance_down(self,row):
		delay = 0
		#lets dance our windows
		#What should it look like?
		#goToE {addr} {%between 2 and 3} {speed} {time delay}
		#row1,row2 = self.generate_order(0)
		if(row == 1):
			for item in self.row1:
				delay = delay + 1000
				position = 25
				speed = 30
				print(item)
			
				data = "goToE {} {} {} {}\r\n".format(item,position,speed,delay)
				self.ser.write(data.encode())
				read_ser = self.ser.readline().decode()
				time.sleep(0.1)
				print (read_ser)
		if(row == 2):
			for item in self.row2:
				delay = delay + 1000
				position = 25
				speed = 30
				print(item)
	
				data = "goToE {} {} {} {}\r\n".format(item,position,speed,delay)
				self.ser.write(data.encode())
				read_ser = self.ser.readline().decode()
				time.sleep(0.1)
				print (read_ser)		
		return
		
	def dance_one(self):
		#try this... if this doesnt work then put the dance down code into the dance up and create a big animation function
		self.dance_up(2)
		time.sleep(5.5)
		self.dance_up(1)
		time.sleep(8)
		self.dance_down(2)
		time.sleep(5.5)
		self.dance_down(1)
		
		time.sleep(7)
		
		self.dance_up(2)
		time.sleep(5.5)
		self.dance_up(1)
		time.sleep(8)
		self.dance_down(2)
		time.sleep(5.5)
		self.dance_down(1)

if __name__ == "__main__": 
	myany = Animation() 
	myany.open_serial()
	myany.generate_order(1)
	#myany.dance_one()
	
