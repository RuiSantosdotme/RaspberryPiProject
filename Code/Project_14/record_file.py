#Project 14 - Record Video to a File
#latest code updates available at: https://github.com/RuiSantosdotme/RaspberryPiProject
#project updates at: https://nostarch.com/RaspberryPiProject

import picamera

camera = picamera.PiCamera()

camera.resolution = (640, 480)
camera.start_recording('videotest.h264')
camera.wait_recording(60)
camera.stop_recording()

print('Finished recording')
