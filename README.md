# ME35 Midterm: Sarah Cody
Code for the ME35 midterm

## Project Description
There are 3 main files for this code: mainCode, midtermComputerCode, and cvMidtermScript. mainCode is to be run on the Raspberry Pi Pico W, while midtermComputerCode and cvMidtermCode may be run on any Python platform. The rest of the files are libraries. Any library containing another library will have the GitHub link to the embedded library within the code.  
### mainCode
The purpose of this code is to take in temperature data from a thermistor, and color data (in the form of a name such as "green" or "red") from an Airtable. The color will determine the units for the temperature reading (Fahrenheit or Celsius) and this, paired with the temperature, gets displayed on an LCD screen. Every 5 minutes, these data points are pushed to an Adafruit.IO dashboard using their MQTT broker.
This code requires 5 main libraries to be downloaded onto the Pico: 
1. thermistor
2. displayTempLib
3. adafruitMQTT
4. airtableReceivePico
5. secretStuff: to be made by the user, contains vulnerable information

All these libraries must be imported and independently functional in order for the code to work properly

### midtermComputerCode
The purpose of this code is to use Python instead of microPython to take color data from the Airtable, convert that into units (Fahrenheit or Celsius), and push it to the Adafruit.IO dashboard every 5 minutes using their MQTT broker. 

### cvMidtermCode
This code, run on https://chrisrogers.pyscriptapps.com/me35-midterm/latest/, uses histograms to determine the most prominent color in an image and pushes that information to the Airtable, where it is received by both the computer and Pico code. 

## Required Materials
**Pico W:** https://www.adafruit.com/product/5526

**Thermistor:** https://www.digikey.com/en/products/detail/ametherm/1DC103J-EC/5970120?utm_adgroup=&utm_source=google&utm_medium=cpc&utm_campaign=PMax%20Shopping_Product_High%20ROAS%20Categories&utm_term=&utm_content=&gclid=Cj0KCQjw-pyqBhDmARIsAKd9XINJLkVAvLebzkW2lwIHPHkug3_OiaEfrymcAPw4mUY2nQew-KoweOUaAqs8EALw_wcB

**Display:** https://www.amazon.com/SunFounder-Serial-Module-Display-Arduino/dp/B019K5X53O?th=1

**Resistor:** https://www.amazon.com/10k-ohm-resistor/s?k=10k+ohm+resistor

## Acknowledgements
This project could not have been done without the help of several online forums, youtube tutorials, and the occasional ChatGPT debugging. Each resource is cited in their respective library. 
I would also like to thank the amazing fall themed playlist that got me through this project :)


