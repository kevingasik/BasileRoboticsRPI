import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# switch pinout
switch1 = 18
switch2 = 17
switch3 = 27
switch4 = 22
switch5 = 23
switch6 = 24
switch7 = 25
switch8 =  8

GPIO.setup(switch1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch3,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch4,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch5,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch6,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch7,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch8,GPIO.IN, pull_up_down=GPIO.PUD_UP)

while (1):
	if GPIO.input(switch1) == 0:
		print("Switch 1 set")
		time.sleep(0.2)
		
	if GPIO.input(switch2) == False:
		print("Switch 2 set")
		time.sleep(0.2)
		
	if GPIO.input(switch3) == False:
		print("Switch 3 set")
		time.sleep(0.2)
		
	if GPIO.input(switch4) == False:
		print("Switch 4 set")
		time.sleep(0.2)
		
	if GPIO.input(switch5) == False:
		print("Switch 5 set")
		time.sleep(0.2)
		
	if GPIO.input(switch6) == False:
		print("Switch 6 set")
		time.sleep(0.2)
		
	if GPIO.input(switch7) == False:
		print("Switch 7 set")
		time.sleep(0.2)
		
	if GPIO.input(switch8) == False:
		print("Switch 8 set")
		time.sleep(0.2)
