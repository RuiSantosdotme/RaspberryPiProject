#Project 16 - Connecting Your Electronics to the Web
#latest code updates available at: https://github.com/RuiSantosdotme/RaspberryPiProject
#project updates at: https://nostarch.com/RaspberryPiProject

#import necessary packages
from gpiozero import LED
from flask import Flask, render_template, request

#create a Flask object
app = Flask(__name__)

#create an object that refers to a relay
relay = LED(17)
#set the relay off; remember the relay works with inverted logic
relay.on()
#save current relay state
relay_state = 'Relay is off'

#display the main web page
@app.route('/')
def main():
   global relay_state
   # pass the relay state to the index.html and return it to the user
   return render_template('index.html', relay_state=relay_state)

#execute control() when someone presses the on/off buttons
@app.route('/<action>')
def control(action):
   global relay_state
   #if the action part of the URL is 'on', turn the relay on
   if action == 'on':
      #set the relay on
      relay.off()
      #save the relay state
      relay_state = 'Relay is on'
   if action == 'off':
      relay.on()
      relay_state = 'Relay is off'

   #pass the relay state to the index.html and return it to the user
   return render_template('index.html', relay_state=relay_state)

#start the web server at localhost on port 80
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug=True)
