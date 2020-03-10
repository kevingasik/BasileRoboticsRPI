import time
import os
import RPi.GPIO as GPIO
import cv2


class MGButtons():
	GPIO.setmode(GPIO.BCM)
	#BCM17,11 Motor_INB
	#BCM22 15 Motor_EnB
	#BCM5,29 Motor_CS
	#Motor_EnA, BCM13 33
	#BCM26,37 Motor_INA
	#MotorPWM BCM18_PCM_C 12 but in verision one it was where?
	
	def __init__(self): 
		self.button_dict = {} 
		
		# self.button_dict['red'] = {} 
		# self.button_dict['red']['read'] = 23
		# self.button_dict['red']['light'] = 37
		# self.button_dict['red']['status'] = 'off'
		
		self.button_dict['red'] = {} 
		self.button_dict['red']['read'] = 24
		self.button_dict['red']['light'] = 13
		self.button_dict['red']['status'] = 'off'
		
		self.button_dict['white'] = {} 
		self.button_dict['white']['read'] = 25
		self.button_dict['white']['light'] = 6
		self.button_dict['white']['status'] = 'off'
		
		self.button_dict['green'] = {} 
		self.button_dict['green']['read'] = 12
		self.button_dict['green']['light'] = 22
		self.button_dict['green']['status'] = 'off'
		
		self.button_dict['yellow'] = {} 
		self.button_dict['yellow']['read'] = 16
		self.button_dict['yellow']['light'] = 12
		self.button_dict['yellow']['status'] = 'off'
		
		for key,value in self.button_dict.items():
			#print(value['read'])
			GPIO.setup(value['read'],GPIO.IN, pull_up_down=GPIO.PUD_UP)
			GPIO.setup(value['light'],GPIO.OUT)
			
	def read_button(self,button): 
		return GPIO.input(button)
	
	#def get_buttons(self): 
		#return [self.button1, self.button2, self.button3, self.button4, self.button5]
	
	
	def read_buttons(self): 
		for key,value in self.button_dict.items(): 
			print(GPIO.input(value['read']))
			
			
	def light_buttons(self): 
		for key,value in self.button_dict.items(): 
			GPIO.output(value['light'],1)
	#def light_button(self,button): 
		#this function will light up a specific button	
			
			
			
	#def read_return_buttons(self): 
		#this function reads the buttons and then returns the ones that have been pressed
	

if __name__ == "__main__": 
	buttons = MGButtons() 
	#while True: 
		#buttons.read_buttons()
		#print(buttons.read_button(16))
	
	#for key,value in MGButtons.button_dict.items(): 
		#print(value['read'])
	print(buttons.button_dict)
	

