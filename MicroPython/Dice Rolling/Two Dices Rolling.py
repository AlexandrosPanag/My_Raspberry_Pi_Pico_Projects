# By Alexandros Panagiotakopoulos

from machine import Pin, I2C
import random
import utime as time

cnt=1 #create a counter to print dice rolls
while True:
    print("You have rolled the dices:",cnt,"times\n\n")
    dice1 = random.randint(1, 6)
    print("The first dice result was:",dice1)
    time.sleep(1)
    dice2 = random.randint(1, 6)
    print("The result second dice result was:",dice2,"\n")
    if(dice1==dice2):
        print("You have rolled doubles!\n")
    cnt=cnt+1
    time.sleep(10)