# By Alexandros Panagiotakopoulos

from machine import Pin, I2C
import random
import utime as time

cnt=1 #create a counter to print dice rolls
while True:
    dice1 = random.randint(1, 6)
    print("You have rolled the dice:",cnt,"times")
    print("The result was:",dice1)
    time.sleep(10)
    cnt=cnt+1
