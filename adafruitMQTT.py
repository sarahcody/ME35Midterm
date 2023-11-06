# MUST BE CONNECTED TO WIFI TO USE THIS LIBRARY
# majority of library via techiesims
# https://github.com/techiesms/ESP32-Micropython-Series-Codes

from mqtt import MQTTClient
from secretStuff import mqtt_client_id,adafruit_io_key,adafruit_io_url,adafruit_user

# establishes feed id names
celsius_feed_id = 'celsius'
farenheit_feed_id = 'farenheit'
temp_feed_id = 'temperature'

# connect to Adafruit MQTT
client = MQTTClient(client_id=mqtt_client_id,
                    server=adafruit_io_url,
                    user=adafruit_user,
                    password=adafruit_io_key,
                    ssl=False)

try:
    client.connect()
except Exception as e:
    print(e)

# establishes link to feed
celsius_feed = bytes('{:s}/feeds/{:s}'.format(adafruit_user, celsius_feed_id), 'utf-8')
farenheit_feed = bytes('{:s}/feeds/{:s}'.format(adafruit_user, farenheit_feed_id), 'utf-8')
temp_feed = bytes('{:s}/feeds/{:s}'.format(adafruit_user, temp_feed_id), 'utf-8')

# publishes to 3 feeds
def send_data(temp, celsius, farenheit):
    client.publish(temp_feed,
                    bytes(str(temp), 'utf-8'),
                    qos=0)
    print("Temp: ", str(temp))
    client.publish(celsius_feed,
                    bytes(str(celsius), 'utf-8'),
                    qos=0)
    print("Celsius: ", str(celsius))
    client.publish(farenheit_feed,
                    bytes(str(farenheit), 'utf-8'),
                    qos=0)
    print("Farenheit: ", str(farenheit))

