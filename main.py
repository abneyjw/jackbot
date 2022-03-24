from ctypes import windll
import time
from spotify import *
from weather import *
windll.shcore.SetProcessDpiAwareness(1)

n = 0

mySpot = Spotify()
mySpot.setup()

while True:
    time.sleep(1)
    myText = mySpot.current()
    if(not mySpot.playing()):
        myText = myText + " (paused)"
    n = 0
    print(myText)
    
