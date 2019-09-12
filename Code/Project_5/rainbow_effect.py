#Project 5 - Rainbow Light Strip
#latest code updates available at: https://github.com/RuiSantosdotme/RaspberryPiProject
#project updates at: https://nostarch.com/RaspberryPiProject

#based on Tony DiCola's NeoPixel library strandtest example

#import necessary libraries
from neopixel import *
from time import sleep
from gpiozero import Button, MCP3008

# LED strip configuration
LED_COUNT = 14 #number of LED pixels
LED_PIN = 18 #GPIO pin connected to the pixels (must support PWM!)
LED_FREQ_HZ = 800000 #LED signal frequency in hertz (usually 800khz)
LED_DMA = 5 #DMA channel to use for generating signal (try 5)
LED_INVERT = False #set True to invert the signal
LED_CHANNEL = 0 #leave channel '0' for GPIO 18

#create pot objects to refer to MCP3008 channel 0 and 1
pot_brightness = MCP3008(0)
pot_speed = MCP3008(1)

#connect pushbutton to GPIO pin 2, pull-up
button_start = Button(2)

#animation running control variable
running_animation = False

#generate rainbow colors across 0-255 positions
def wheel(pos):
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

#draw rainbow that uniformly distributes itself across all pixels
def rainbowCycle(strip):
    for j in range(256):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        sleep((pot_speed.value*40)/1000.0)

#function to start and stop the animation
def start_animation():
    global running_animation
    if running_animation == True:
        running_animation = False
    else:
        running_animation = True

#assign a function that runs when the button is pressed
button_start.when_pressed = start_animation

#create NeoPixel object with appropriate configuration
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, int(pot_brightness.value*255), LED_CHANNEL)
#initialize the strip
strip.begin()
while True:
    if running_animation == True:
        #set LED strip brightness
        strip.setBrightness(int(pot_brightness.value*255))
        rainbowCycle(strip)
