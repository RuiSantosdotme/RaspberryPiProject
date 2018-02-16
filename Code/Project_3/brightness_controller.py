#Project 3 - LED Dimmer Switch
#latest code updates available at: https://github.com/RuiSantosdotme/RaspberryPiProject
#project updates at: https://nostarch.com/RaspberryPiProject

#import necessary packages
from gpiozero import PWMLED, MCP3008
from time import sleep

#create an object called pot which refers to MCP3008 channel 0
pot = MCP3008(0)

#create a PWMLED object called led that refers to GPIO 17
led = PWMLED(17)

while True:
    #the pot.value accesses the current pot reading
    if(pot.value < 0.001):
        #if the pot value is very small, the led is turned off
        led.value = 0
    else:
        #change led brightness accordingly to the pot value
        led.value = pot.value
    #print the pot value
    print(pot.value)
    #pause for 0.1 seconds
    sleep(0.1)
