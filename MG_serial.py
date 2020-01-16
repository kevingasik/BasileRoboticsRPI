#!/usr/bin/env python

import serial
import time
import os
import termios


class Animation(): 
	
	def __init__(self): 
		self.mystr = "hello"
		
	def open_serial(self): 
		port='/dev/ttyAMA0'
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
			return [0,1,2,3,4,5,6,7,8,9,10,11],[23,22,21,20,19,18,17,16,15,14,13,12]
		
	def dance_up(self): 
		delay = 0
		#lets dance our windows
		#What should it look like?
		#goToE {addr} {%between 2 and 3} {speed} {time delay}
		row1,row2 = self.generate_order(0)
		
		for item in row1:
			delay = delay + 2000
			position = 95
			speed = 30
			print(item)
			
			data = "goToE {} {} {} {}\r\n".format(item,position,speed,delay)
			self.ser.write(data.encode())
			read_ser = self.ser.readline().decode()
			print (read_ser)

		for item in row2:
			delay = delay + 2000
			position = 95
			speed = 30
			print(item)
	
			data = "goToE {} {} {} {}\r\n".format(item,position,speed,delay)
			self.ser.write(data.encode())
			read_ser = self.ser.readline().decode()
			print (read_ser)		
			
		return
		
		
	def dance_down(self):
		delay = 0
		#lets dance our windows
		#What should it look like?
		#goToE {addr} {%between 2 and 3} {speed} {time delay}
		row1,row2 = self.generate_order(0)
		
		for item in row1:
			delay = delay + 2000
			position = 15
			speed = 30
			print(item)
			
			data = "goToE {} {} {} {}\r\n".format(item,position,speed,delay)
			self.ser.write(data.encode())
			read_ser = self.ser.readline().decode()
			print (read_ser)

		for item in row2:
			delay = delay + 2000
			position = 15
			speed = 30
			print(item)
	
			data = "goToE {} {} {} {}\r\n".format(item,position,speed,delay)
			self.ser.write(data.encode())
			read_ser = self.ser.readline().decode()
			print (read_ser)		
			
		return
		
	def dance_one(self):
		#try this... if this doesnt work then put the dance down code into the dance up and create a big animation function
		self.dance_up()
		time.sleep(16)
		self.dance_down()

if __name__ == "__main__": 
	myany = Animation() 
	myany.open_serial()
	myany.dance_one()
	
