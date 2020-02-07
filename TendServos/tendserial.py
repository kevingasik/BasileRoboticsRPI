#!/usr/bin/env python

import serial
import time
import os
import termios


class TendSerial(): 
	
	def __init__(self): 
		self.mystr = "hello"
		self.row1 = []
		self.row2 = []
		
		self.openPort = False
		
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
		
		


if __name__ == "__main__": 
	myany = Animation() 
	myany.open_serial()

	
