#Project 12 - Temperature and Humidity Data Logger
#latest code updates available at: https://github.com/RuiSantosdotme/RaspberryPiProject
#project updates at: https://nostarch.com/RaspberryPiProject

#import necessary packages
import Adafruit_DHT
import time

#comment and uncomment the line below for your sensor
#sensor = Adafruit_DHT.DHT11
sensor = Adafruit_DHT.DHT22
#sensor = Adafruit_DHT.AM2302

#DHT pin connects to GPIO 4
sensor_pin = 4

#create a variable to control the while loop
running = True

#new .txt file created with header
file = open('sensor_readings.txt', 'w')
file.write('time and date, temperature, humidity\n')

#loop forever
while running:
    try:
        #read the humidity and temperature
        humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)

        #uncomment the line below to convert the temperature to Fahrenheit
        #temperature = temperature * 9/5.0 + 32

        #sometimes you won't get a reading and the results will be null
        #the next statement guarantees that it only saves valid readings
        if humidity is not None and temperature is not None:
            #print temperature and humidity
            print('Temperature = ' + str(temperature) + ', Humidity = ' + str(humidity))
            #save time, date, temperature and humidity in .txt file
            file.write(time.strftime('%H:%M:%S %d/%m/%Y') + ', ' +
                str(temperature) + ', '+ str(humidity) + '\n')
        else:
            print('Failed to get reading. Try again!')
        #waits 10s between each sensor reading
        time.sleep(10)
    #if KeyboardInterrupt triggered: stops loop and closes .txt file
    except KeyboardInterrupt:
        print ('Program stopped')
        running = False
        file.close()
