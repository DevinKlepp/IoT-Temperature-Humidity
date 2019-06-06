# Temperature and Humidity sensor program using DHT11 by Adafruit using
# Adafruit Python DHT Sensor Library
# https://github.com/adafruit/Adafruit_Python_DHT

import time
import datetime
import Adafruit_DHT


sensor = Adafruit_DHT.DHT11
pin = 17
while True:
    hum, temp = Adafruit_DHT.read_retry(sensor, pin)
    print("The temperature is " + str(temp) + "C, " + str(temp * (9.0 / 5.0) + 32.0) + "F with a humidity of " + str(hum) + "%")
    currenttime = datetime.datetime.now()
    print("Recorded at " +  str(currenttime))
    time.sleep(5)
