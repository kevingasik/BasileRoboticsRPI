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
		self.button_dict['red']['light'] = 22 #13
		self.button_dict['red']['status'] = 'off'
		self.button_dict['red']['prevState'] = None
		self.button_dict['red']['currState'] = None
		
		self.button_dict['white'] = {} 
		self.button_dict['white']['read'] = 25
		self.button_dict['white']['light'] = 26 #6
		self.button_dict['white']['status'] = 'off'
		self.button_dict['white']['prevState'] = None
		self.button_dict['white']['currState'] = None
		
		self.button_dict['green'] = {} 
		self.button_dict['green']['read'] = 12
		self.button_dict['green']['light'] = 13 #22
		self.button_dict['green']['status'] = 'off'
		self.button_dict['green']['prevState'] = None
		self.button_dict['green']['currState'] = None
		
		self.button_dict['yellow'] = {} 
		self.button_dict['yellow']['read'] = 16
		self.button_dict['yellow']['light'] = 6 #32
		self.button_dict['yellow']['status'] = 'off'
		self.button_dict['yellow']['prevState'] = None
		self.button_dict['yellow']['currState'] = None
		
		for key,value in self.button_dict.items():
			#print(value['read'])
			GPIO.setup(value['read'],GPIO.IN, pull_up_down=GPIO.PUD_UP)
			GPIO.setup(value['light'],GPIO.OUT)
			
		GPIO.add_event_detect(self.button_dict['red']['read'], GPIO.RISING, callback=lambda x: self.change_status(self.button_dict['red']['read']), bouncetime=300)
		GPIO.add_event_detect(self.button_dict['white']['read'], GPIO.RISING, callback=lambda x: self.change_status(self.button_dict['white']['read']), bouncetime=300)
		GPIO.add_event_detect(self.button_dict['green']['read'], GPIO.RISING, callback=lambda x: self.change_status(self.button_dict['green']['read']), bouncetime=300)
		GPIO.add_event_detect(self.button_dict['yellow']['read'], GPIO.RISING, callback=lambda x: self.change_status(self.button_dict['yellow']['read']), bouncetime=300)
			
	def change_status(self,button):
		a_button_pressed = False
		
		for key,value in self.button_dict.items():
			if(value['status'] == 'on'): 
				a_button_pressed = True
				
		for key,value in self.button_dict.items():		
			if(value['read'] == button) and (value['status'] == 'off') and (a_button_pressed == False):	
				self.button_dict[str(key)]['status'] = 'on'
				GPIO.output(self.button_dict[str(key)]['light'],1)
			elif(value['read'] == button) and (value['status'] == 'on'): 
				self.button_dict[str(key)]['status'] = 'off'
				GPIO.output(self.button_dict[str(key)]['light'],0)
				
	def read_button(self,button): 
		return GPIO.input(button)
		
	def read_buttons(self): 
		# this function returns an arr of the values being read
		read_arr = []
		for key,value in self.button_dict.items(): 
			read_arr.append(GPIO.output(value['read']))
		return read_arr 
		
	def print_buttons(self,read, light, status):
		#this function prints the button read values
		if(read == True): 
			for key,value in self.button_dict.items(): 
				print(value['read'])
		elif(light == True): 
			for key,value in self.button_dict.items(): 
				print(value['light'])
		elif(status == True): 
			for key,value in self.button_dict.items(): 
				print(value['status'])
		 		
	def light_buttons(self): 
		for key,value in self.button_dict.items(): 
			if(value['status'] == 'on'): 
				GPIO.output(self.button_dict[str(key)]['light'],1)
			elif(value['status'] == 'off'): 
				GPIO.output(value['light'],0)
		
	# def read_light_buttons(self): 
		# for key,value in self.button_dict.items(): 
			# print(GPIO.input(value['read']))
			# GPIO.output(value['light'],1)


if __name__ == "__main__": 
	buttons = MGButtons() 
	while True: 
		#buttons.change_status_buttons()
		#print(buttons.read_button(16))
		#print('hello')
		buttons.print_buttons(False,False,True)
		#buttons.light_buttons()
		time.sleep(0.25)
	#for key,value in MGButtons.button_dict.items(): 
		#print(value['read'])
	#print(buttons.button_dict)
	

