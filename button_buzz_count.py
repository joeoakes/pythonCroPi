#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import RPi.GPIO as GPIO
import time
import Adafruit_CharLCD as LCD

# configure both button and buzzer pins
button_pin = 26
buzzer_pin = 18

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)


# set board mode to GPIO.BOARD
GPIO.setmode(GPIO.BCM)

# setup button pin asBu input and buzzer pin as output
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer_pin, GPIO.OUT)

cnt = 0

try:
    # Turn backlight on
    lcd.set_backlight(0)
    
    while True:
        # check if button pressed
        if(GPIO.input(button_pin) == 0):
            # set buzzer on
            GPIO.output(buzzer_pin, GPIO.HIGH)
            # increment count and display on the LCD
            cnt = cnt +1
            # Print a two line message
            lcd.message(cnt)
        else:
            # it's not pressed, set button off
            GPIO.output(buzzer_pin, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
