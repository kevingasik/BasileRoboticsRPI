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
		
		data = input("Enter something : ")
		data = data +'\r\n'
		if(data == "animate\r\n"):
			comms.generate_order(1) 
			comms.dance_one()
		comms.ser.write(data.encode())
		read_serial = comms.ser.readline().decode()
		print (read_serial)
		

if __name__ == "__main__": 
	main()
