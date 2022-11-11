# This code was edited by Alexandros Panagiotakopoulos

from machine import Pin #importing the necessary libraries
import time

led = Pin(25, Pin.OUT) #declare the pin as an output


# Start blinking the LED by toggling its value every second.
while True: # begin eternal loop this code runs forever
    print("- LED OFF")
    led.value(0) # turn off the LED
    time.sleep(1)  # delay 1 second

    print("- LED ON") # print LED on
    led.value(1) # turn on the LED
    time.sleep(1) # delay 1 second