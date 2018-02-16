#Project 18 - Digital Drum Set
#latest code updates available at: https://github.com/RuiSantosdotme/RaspberryPiProject
#project updates at: https://nostarch.com/RaspberryPiProject

#import the necessary packages
import pygame.mixer
from pygame.mixer import Sound
from gpiozero import Button
from signal import pause

#create an object for the mixer module that loads and plays sounds
pygame.mixer.init()

#assign each button to a drum sound
button_sounds = {
    Button(2): Sound("samples/drum_cymbal_open.wav"),
    Button(3): Sound("samples/drum_heavy_kick.wav"),
    Button(14): Sound("samples/drum_snare_hard.wav"),
    Button(15): Sound("samples/drum_cymbal_closed.wav"),
    Button(17): Sound("samples/drum_roll.wav"),
    Button(18): Sound("samples/perc_snap.wav"),
    Button(22): Sound("samples/loop_amen_full.wav"),
    Button(27): Sound("samples/loop_mika.wav"),
}

#the sound plays when the button is pressed
for button, sound in button_sounds.items():
    button.when_pressed = sound.play

#keep the program running to detect events
pause()
