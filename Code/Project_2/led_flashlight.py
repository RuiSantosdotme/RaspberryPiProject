#Project 2 - Pushbutton LED Flashlight
#latest code updates available at: https://github.com/RuiSantosdotme/RaspberryPiProject
#project updates at: https://nostarch.com/RaspberryPiProject

from gpiozero import LED, Button
from signal import pause

led = LED(25)
button = Button(2)

button.when_pressed = led.on
button.when_released = led.off

pause()
