#Project 6 - An LCD Reminder
#latest code updates available at: https://github.com/RuiSantosdotme/RaspberryPiProject
#project updates at: https://nostarch.com/RaspberryPiProject

import Adafruit_CharLCD as LCD
import time

#Raspberry Pi pin configuration
lcd_rs = 27
lcd_en = 22
lcd_d4 = 25
lcd_d5 = 24
lcd_d6 = 23
lcd_d7 = 18
lcd_backlight = 4

#define the LCD size
lcd_columns = 16
lcd_rows = 2

#initialize the LCD
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5,
            lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

#write your message
title = "Don't forget!"
reminder = "You have a doctor appointment next Monday"

#set the delay for scroll
delay = 0.3

#write a function to scroll the message
def scroll_text(reminder, delay):
    padding = " " * lcd_columns
    scroll_message = padding + reminder + " "
    for i in range(len(scroll_message)):
        lcd.set_cursor(0, 1)
        lcd.message(scroll_message[i:(i+lcd_columns)])
        time.sleep(delay)

#Scroll text in infinite loop
lcd.clear()
lcd.home()
lcd.message(title)

while(True):
    scroll_text(reminder, delay)
