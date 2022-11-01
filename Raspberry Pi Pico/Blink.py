from machine import Pin
import time

led = Pin(25, Pin.OUT) #declare the LED AS AN OUTPUT
while True:
    #turn on the LED
    led.value(1) #set the LED to ON
    print("LED ON") #print a message into the console
    time.sleep(1) #sleep for 1 second
    #turn off the LED
    print("LED OFF") #set the LED to OFF
    led.value(0) #turn off the LED
    time.sleep(1) #sleep for 1 second
