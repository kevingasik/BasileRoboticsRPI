#!/usr/bin/env python

import serial
import time
import os
import termios
import MG_serial

def main(): 
	comms = MG_serial.Animation()
	comms.open_serial()
	print(comms.ser.read(8))
	count = 0
	while True:
		if(count == 0):
			count = 1
			comms.ser.read(8)
    
		data = input("Enter something : ")
		if(data == "animate"): 
			comms.dance_one()
		comms.ser.write(data.encode())
		read_serial = comms.ser.readline().decode()
		print (read_serial)
		

if __name__ == "__main__": 
	main()
