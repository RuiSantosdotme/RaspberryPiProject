#Project 7 - Mini Weather Forecaster
#latest code updates available at: https://github.com/RuiSantosdotme/RaspberryPiProject
#project updates at: https://nostarch.com/RaspberryPiProject

#import necessary libraries
import time
import Adafruit_SSD1306
import requests

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#Raspberry Pi pin configuration
RST = 24

#128x32 display with hardware I2C
#disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

#128x64 display with hardware I2C
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

#set your unique OpenWeatherMap.org URL
open_weather_map_url = 'http://api.openweathermap.org/data/2.5/weather?q=Porto,PT&APPID=801d2603e9f2e1c70e042e4f5f6e0381'

#initialize display
disp.begin()

while True:
    #clear display
    disp.clear()
    disp.display()

    #create blank image for drawing
    #make sure to create image with mode '1' for 1-bit color
    width = disp.width
    height = disp.height
    image = Image.new('1', (width, height))

    #get drawing object to draw on image
    draw = ImageDraw.Draw(image)

    #draw a black filled box to clear the image
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    #define constants to define drawing area
    padding = 2
    top = padding
    #move left to right keeping track of the current x position for drawing text
    x = padding

    #load default font
    font = ImageFont.load_default()

    #OpenWeatherMap.org weather data request
    weather_data = requests.get(open_weather_map_url)

    #display location
    location = weather_data.json().get('name') + ' - ' + weather_data.json().get('sys').get('country')
    draw.text((x, top), location,  font=font, fill=255)

    #display description
    description = 'Desc ' + weather_data.json().get('weather')[0].get('main')
    draw.text((x, top+10), description,  font=font, fill=255)

    #temperature
    raw_temperature = weather_data.json().get('main').get('temp')-273.15

    #temperature in Celsius
    temperature = 'Temp ' + str(raw_temperature) + '*C'
    #uncomment for temperature in Fahrenheit
    #temperature = 'Temp ' + str(raw_temperature*(9/5.0)+32) + '*F'
    draw.text((x, top+20), temperature, font=font, fill=255)

    #display pressure
    pressure = 'Pres ' + str(weather_data.json().get('main').get('pressure')) + 'hPa'
    draw.text((x, top+30), pressure, font=font, fill=255)

    #displays humidity
    humidity = 'Humi ' + str(weather_data.json().get('main').get('humidity')) + '%'
    draw.text((x, top+40), humidity, font=font, fill=255)

    #displays wind
    wind = 'Wind ' + str(weather_data.json().get('wind').get('speed')) + 'mps ' + str(weather_data.json().get('wind').get('deg')) + '*'
    draw.text((x, top+50), wind, font=font, fill=255)

    #display image
    disp.image(image)
    disp.display()
    time.sleep(10)
