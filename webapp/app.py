from flask import Flask, render_template, request
#from flask_socketio import SocketIO
import RPi.GPIO as GPIO 
import board
import neopixel 

pixels = neopixel.NeoPixel(board.D18, 15) # sixth one
pixels.fill((0, 0, 0))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
GPIO.setmode(GPIO.BCM)

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   23 : {'name' : 'GPIO 23', 'state' : GPIO.LOW},
   24 : {'name' : 'GPIO 24', 'state' : GPIO.LOW}
   }
   
COLORS =  {'red' : (255,0,0), 
			'orange' : (255,127,0),
			'yellow' : (255,255,0),
			'green' : (0,255,0),
			'blue' : (0,0,255),
			'purple' : (127,0,255),
			'cyan' : (0,255,255),
			'majenta' : (255,0,127) 
			
} 

# Set each pin as an output and make it low:
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)

@app.route("/")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'pins' : pins,
      'COLORS' : COLORS,
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/single/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   deviceName = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      # Set the pin high:
      GPIO.output(changePin, GPIO.HIGH)
      pixels.fill(COLORS['green'])


      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "off":
      #GPIO.output(changePin, GPIO.LOW)
      pixels.fill((0, 0, 0))

      
      GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + deviceName + " off."

   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins,
      'COLORS': COLORS
   }

   return render_template('main.html', **templateData)
   
@app.route("/colorAction/<changeColor>/<action>")
def colorAction(changeColor, action):
   print(changeColor)
	#changePin = int(changePin)
   # If the action part of the URL is "on," execute the code indented below:
   deviceName = pins[24]['name']
   
   if action == "on":
      # Set the pin high:
      GPIO.output(24, GPIO.HIGH)
      pixels.fill(COLORS[changeColor])
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
      
   if action == "off":
      #GPIO.output(changePin, GPIO.LOW)
      pixels.fill((0, 0, 0))
      GPIO.output(24, GPIO.LOW)
      message = "Turned " + deviceName + " off."

   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins,
      'COLORS': COLORS
   }

   return render_template('main.html', **templateData)
   

#background process happening without any refreshing
@app.route('/changeColor/', methods = ['POST'])
def changeColor():
	if request.method == 'POST':
	    result = request.form
	    value = result['COLOR'].lstrip('#')
	    print(value) 
	    print(value.upper())
	    print('RGB =', tuple(int(value[i:i+2], 16) for i in (0, 2, 4)))
	    pixels.fill(tuple(int(value[i:i+2], 16) for i in (0, 2, 4))) 
	    
	return render_template('main.html',result = result)
   

if __name__ == '__main__': 
	app.run(debug=True, host='192.168.1.99')
