import time
import os
import RPi.GPIO as GPIO


class MGButtons():
	switch1 = 18
	switch2 = 17
	switch3 = 27
	switch4 = 22
	switch5 = 23
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(switch1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(switch2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(switch3,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(switch4,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(switch5,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	def __init__(self): 
		self.button1 = 18
		self.button2 = 17
		self.button3 = 27
		self.button4 = 22
		self.button5 = 23
		
	def read_button(self,button): 
		return GPIO.input(button)
	
	def get_buttons(self): 
		return [self.button1, self.button2, self.button3, self.button4, self.button5]
	
	def read_buttons(self): 
		return [GPIO.input(self.button1), GPIO.input(self.button2), GPIO.input(self.button3), GPIO.input(self.button4), GPIO.input(self.button5)] 
		
	def print_buttons(self): 
		button_list = [GPIO.input(self.button1), GPIO.input(self.button2), GPIO.input(self.button3), GPIO.input(self.button4), GPIO.input(self.button5)] 
		for item in button_list: 
			print(item)
		
	#def light_button(self, button): 
		# lights up one of the buttons
		
	#def light_buttons(self): 
		# lights up all the buttons
	

if __name__ == "__main__": 
	buttons = MGButtons() 
	print(buttons.read_buttons())
	buttons.print_buttons()
	print(buttons.get_buttons())
	
