#Project 8 - Joystick Control
#latest code updates available at: https://github.com/RuiSantosdotme/RaspberryPiProject
#project updates at: https://nostarch.com/RaspberryPiProject

from signal import pause

from sense_hat import SenseHat
#uncomment the following line if you are using the emulator from sense_emu import SenseHat

sense = SenseHat()

def move_up(event):
    print('joystick was moved up')

def move_down(event):
    print('joystick was moved down')

def move_right(event):
    print('joystick was moved right')

def move_left(event):
    print('joystick was moved left')

def move_middle(event):
    print('joystick was pressed')

sense.stick.direction_up = move_up
sense.stick.direction_down = move_down
sense.stick.direction_right = move_right
sense.stick.direction_left = move_left
sense.stick.direction_middle = move_middle

pause()
