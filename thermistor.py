# formulas via chat gpt
# values for thermistor via https://www.gotronic.fr/pj2-mf52type-1554.pdf

from machine import ADC
import math

# define adc pin
adc = ADC(2)

# thermistor params
R1 = 10000  # 10 kOhm resistor in circuit
beta = 3950  # from online resource
T0 = 298.15  # reference temp for R1 in Kelvin

def temp_C():
    # reads analog
    raw_value = adc.read_u16()

    # convert ADC value to voltage, 3.3V input
    voltage = raw_value / 65535 * 3.3

    # calculate current thermistor resistance
    resistance = R1 / (3.3 / voltage - 1)

    # steinhart-hart equation, answer in K
    inv_T = 1 / T0 + (1 / beta) * math.log(resistance / R1)
    temperature = 1 / inv_T - 273.15  # convert to Celsius
    formatted_temp = "{:.1f}".format(temperature)
    print(formatted_temp)
    return formatted_temp

temp_C()
