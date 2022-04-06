import time
import keyboard
import threading
from spotify import *
from weather import *

n = 0

stopSpot = False
toggleSpot = False
skipSpot = False
prevSpot = False

f = open("currents.txt")
content = f.readlines()
print("Current Temperature: " + content[0].strip() + "° F")
f.close()

mySpot = Spotify()
mySpot.setup()


nice = [1,2,3,4,5,14,21,30,32,33,34]
cozy = [6,7,8,11,12,13,18,35,36,37,38,39,40]
storm = [15,16,17,24,25,26,41,42]
winter = [19,20,21,22,23,29,31,43,44]

try:
    mySpot.interact('current')
    while True:
        if keyboard.is_pressed('e'):
            break
        elif keyboard.is_pressed('t'):
            mySpot.interact("toggle")
        elif keyboard.is_pressed('n'):
            mySpot.interact("skip")
        elif keyboard.is_pressed('p'):
            mySpot.interact("prev")
        elif keyboard.is_pressed('c'):
            mySpot.interact("current")
except KeyboardInterrupt:
    print("exiting...")
except TypeError:
    print("No device found")

    




        
