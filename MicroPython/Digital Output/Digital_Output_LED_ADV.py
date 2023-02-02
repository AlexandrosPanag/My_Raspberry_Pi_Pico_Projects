# This code was created by Alexandros Panagiotakopoulos

from machine import Pin, Timer
led = Pin(2, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle() #tobble the LED on/off

timer.init(freq=1, mode=Timer.PERIODIC, callback=blink) #call the blink function and blink infinitely!

# with freq the frequency (time) can be adjusted
# periodic timer stays active infinitely by default for more information about the timer
# library you can check out: https://blog.logrocket.com/understanding-flutter-timer-class-timer-periodic/
