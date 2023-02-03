# Original code was written by Manodeep:https://www.instructables.com/DHT11-With-Raspberry-Pi-Pico/
# Edited by Alexandros Panagiotakopoulos

# connect the sensor : 
# DHT11             RASPBERRY PI PICO
# left sensor pin   GPIO 28
# VDD/VIN           DIGITAL 3V3 GPIO 36
# GND               DIGITAL GND GPIO 38

from machine import Pin, I2C
import utime as time
from dht import DHT11, InvalidChecksum #the dht sensor library can be found here:https://www.instructables.com/DHT11-With-Raspberry-Pi-Pico/

while True:
    time.sleep(2) #sleep for 2 seconds before taking another measurement
    pin = Pin(28, Pin.OUT, Pin.PULL_DOWN) #declare the Pin 28 (data pin as an output)
    sensor = DHT11(pin) #intialize the sensor pin
    t  = (sensor.temperature) # store the temperature value in
    h = (sensor.humidity) optional code to store the humidity in a value 
    f = t*9/5+32 # From Celsius Fahrenheit Conversion Formula
    print("Temperature in Celsius: {}".format(sensor.temperature)) #print the temperature value
    print("Temperature in Fahrenheit: {}".format(f)) #print the fahreneheit value
    print("Humidity: {} \n".format(sensor.humidity)) #print the humidity value
