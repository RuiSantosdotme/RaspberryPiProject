#Project 9 - Reading Temperature, Humidity, And Pressure
#latest code updates available at: https://github.com/RuiSantosdotme/RaspberryPiProject
#project updates at: https://nostarch.com/RaspberryPiProject

from sense_hat import SenseHat
#from sense_emu import SenseHat

from time import sleep

#create an object called sense
sense = SenseHat()

while True:
    temperature = sense.temperature
    temperature = str(round(temperature, 2))
    print('Temperature: ' + temperature + '*C\n')

    humidity = sense.humidity
    humidity = str(round(humidity, 2))
    print ('Humidity: ' + humidity + '%\n')

    pressure = sense.pressure
    pressure = str(round(pressure, 2))
    print('Pressure: ' + pressure + 'hPa\n')

    sleep(1)

