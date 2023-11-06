# lcd_api and pico_i2c_lcd libraries via https://github.com/T-622/RPI-PICO-I2C-LCD
# degree symbol designed on https://maxpromer.github.io/LCD-Character-Creator/
# display name (amazon): SunFounder IIC I2C TWI 1602 Serial LCD Module Display Compatible with Arduino R3 Mega 2560 16x2
# allows for up to 5 characters for temperature (100.5, 20.67, etc...)

import utime
import machine
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# establishes i2c address and intializes rows and columns
I2C_ADDR = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

# sets up i2c connection using pins 0 and 1
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

# displays current temperature
def display_temp(temp, unit):
    lcd.clear() # clears display
    lcd.move_to(5, 0) # moves cursor to starting post
    lcd.putstr(str(temp))  # convert temp to string
    lcd.move_to(10, 0)
    lcd.putchar(chr(0)) # places degree symbol at line 1, spot 10
    lcd.putstr(unit)
    utime.sleep(5) # keeps message up for 2 seconds
    lcd.clear()

# lays out degree symbol design
def degree_symbol():
    lcd.custom_char(0, bytearray([0x0E, 0x0A, 0x0E, 0x00, 0x00, 0x00, 0x00, 0x00]))


degree_symbol()  # intializes custom character
