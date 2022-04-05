from ctypes import windll
import time
import keyboard
import threading
from spotify import *
from weather import *
windll.shcore.SetProcessDpiAwareness(1)

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




try:
    if(mySpot is None):
        print("valid")
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


    




        
