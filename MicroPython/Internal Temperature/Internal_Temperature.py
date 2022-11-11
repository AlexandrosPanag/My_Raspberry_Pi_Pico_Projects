# This code was edited by Alexandros Panagiotakopoulos

import machine #import machine library
import utime #import utime
  
sensor_temp = machine.ADC(4) #read the internal temperature
conversion_factor = 3.3 / (65535) #convert the temperature
 
while True: 
    reading = sensor_temp.read_u16() * conversion_factor #read and convert the temperature 
    temperature = 27 - (reading - 0.706)/0.001721 #read and convert the temperature 
    print("The current temperature is: {}".format(temperature)) #print the temperature
    utime.sleep(5) #sleep for 5 seconds
