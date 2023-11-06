import requests
import json
from secretStuff import airtable_id, airtable_url, token
import paho.mqtt.client as mqtt
from secretStuff import mqtt_client_id, adafruit_io_key, adafruit_io_url, adafruit_user
import time

# where "Color" is the table name
url = f"{airtable_url}/Color"

# establish headers to access the table
headers = {
    "Authorization": "Bearer " + str(token),
    "Content-Type": "application/json",
}

def receive_color():
    response = requests.get(url, headers=headers)  # Get the response in JSON format
    response_data = response.json()
    records = response_data.get("records", [])

    if records:
        color = str(records[-1]["fields"]["COLOR"])  # Get the last entry in the COLOR column
        print(color)  # Print the entry
        return color
    else:
        print("No records found.")
        return None  # Return None when no records are found

# establish feed id names
celsius_feed_id = 'celsius'
farenheit_feed_id = 'farenheit'

# callback when connection to Adafruit MQTT is established
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to Adafruit IO MQTT")
    else:
        print(f"Failed to connect, return code {rc}")

# connect to Adafruit MQTT
client = mqtt.Client(client_id=mqtt_client_id)
client.username_pw_set(username=adafruit_user, password=adafruit_io_key)
client.on_connect = on_connect

try:
    client.connect(adafruit_io_url, 1883)
    client.loop_start()  # start the MQTT loop
except Exception as e:
    print(e)

# establish links to feeds
celsius_feed = f'{adafruit_user}/feeds/{celsius_feed_id}'
farenheit_feed = f'{adafruit_user}/feeds/{farenheit_feed_id}'


# publish to 2 feeds
def send_data(celsius, farenheit):
    client.publish(celsius_feed, str(celsius))
    print("Celsius:", celsius)
    client.publish(farenheit_feed, str(farenheit))
    print("Fahrenheit:", farenheit)

import time

def main():
    while True:
        # get the color from airtable
        color = receive_color()

        # set the appropriate unit based on the color
        if color == "green" or color == "ignore":
            celsius = 1
            farenheit = 0
        elif color == "red":
            celsius = 0
            farenheit = 1

        send_data(celsius, farenheit)
        print("unit sent to dashboard!")

        # Sleep for 5 minutes
        time.sleep(300)  # 300 seconds = 5 minutes


main()
