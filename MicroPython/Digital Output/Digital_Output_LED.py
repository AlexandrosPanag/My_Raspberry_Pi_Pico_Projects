from machine import Pin
import time

led = Pin(2, Pin.OUT) #declare the digital output (OUT) in GPIO2

while True:
        led.toggle() #toggle the led on and off
        time.sleep(1) #sleep for 1 second