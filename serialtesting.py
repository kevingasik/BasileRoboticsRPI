#!/usr/bin/env python

import serial
import time
import os
import termios

port='/dev/ttyAMA0'
with open(port) as f:
    attrs = termios.tcgetattr(f)
    attrs[2] = attrs[2] & ~termios.HUPCL
    termios.tcsetattr(f, termios.TCSAFLUSH,attrs)
    


ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate = 115200,
    parity = serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

ser.close()
ser.open()
ser.reset_input_buffer()
ser.reset_output_buffer()
ser.close()
ser.open()

count = 0


def animationOne(): 
    for i in range(0,22): 
        data = "up {} 20".format(i)
        ser.write(data)
        read_ser = ser.readline()
        time.sleep(0.2)
        print read_ser

while True:
    if(count == 0):
        count = 1
        ser.read(8)
    
    data = raw_input("Enter something : ")
    if(data == "animate"): 
        animationOne()
    else: 
        ser.write(data)
    read_serial = ser.readline()
    print read_serial
