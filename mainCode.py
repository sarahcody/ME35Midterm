import network
import time
import utime
from secretStuff import wifi_pass, wifi_ssid
import thermistor as therm
import displayTempLib as display
import adafruitMQTT as adafruit
import airtableReceivePico as airtable

# connect to wifi
def connect_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.disconnect()
    wifi.connect(wifi_ssid, wifi_pass)
    if not wifi.isconnected():
        print('connecting...')
        timeout = 0
        while (not wifi.isconnected() and timeout < 5):
            print(5-timeout)
            timeout = timeout + 1
            time.sleep(1)
    if(wifi.isconnected()):
        print('connected')
    else:
        print('not connected')

connect_wifi()

# establishes global variables
temp = 0
unit = ""
last_send_time = 0

# sends temperature and unit data to API
def send_to_API():
    global temp
    global unit

    # for API, if celsius or farenheit feed value > 1, indicator turns on
    if unit == "C":
        celsius = 1
        farenheit = 0
    elif unit == "F":
        celsius = 0
        farenheit = 1

    adafruit.send_data(temp, celsius, farenheit)
    print("data sent to API!")

def main():
    global temp
    global unit
    global last_send_time

    # read temperature in celsius
    temp = therm.temp_C()
    temp = float(temp)

    # gets color from airtable
    color = airtable.receive_color()

    # sets unit and converts C to F based on color received from C
    if color == "green" or color == "ignore":
        unit = "C"
    elif color == "red":
        unit = "F"
        temp = (temp * 9 / 5) + 32
        temp = "{:.1f}".format(temp)

    # displays temperature and appropriate unit
    display.display_temp(temp, unit)

    # check if at least 5 minutes have passed since last sending to API
    current_time = utime.time()
    if current_time - last_send_time >= 300000:
        send_to_API()
        last_send_time = current_time


try:
    while True:
        main()
        time.sleep(2)
except KeyboardInterrupt:
    print("Keyboard interrupt. Bye!")
main()

