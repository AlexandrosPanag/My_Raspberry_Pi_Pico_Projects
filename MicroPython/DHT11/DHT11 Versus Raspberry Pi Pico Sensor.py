# By Alexandros Panagiotakopoulos

from machine import Pin, I2C
import utime as time
from dht import DHT11, InvalidChecksum #the dht sensor library can be found here:https://www.instructables.com/DHT11-With-Raspberry-Pi-Pico/

sensor_temp = machine.ADC(4) #read the internal temperature
conversion_factor = 3.3 / (65535) #convert the temperature
 
 
while True:
    time.sleep(2) #sleep for 2 seconds before taking another measurement
    pin = Pin(28, Pin.OUT, Pin.PULL_DOWN) #declare the Pin 28 (data pin as an output)
    sensor = DHT11(pin) #intialize the sensor pin
    t  = (sensor.temperature) # store the temperature value in
    #h = (sensor.humidity) optional code to store the humidity in a value 
    f = t*9/5+32 # From Celsius Fahrenheit Conversion Formula
    print("DHT11 TEMPERATURE: {}".format(sensor.temperature)) #print the temperature value
    reading = sensor_temp.read_u16() * conversion_factor #read and convert the temperature 
    temperature = 27 - (reading - 0.706)/0.001721 #read and convert the temperature 
    print("BUILT-IN SENSOR RESULTS: {}".format(temperature)) #print the temperature
    print("\n")
