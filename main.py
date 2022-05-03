import time
import keyboard
import threading
from display import *
from lcd import *
from spotify import *
from weather import *
from followers import *
from matrix import *
import RPi.GPIO as GPIO



PREV = 21 
TOGGLE = 17 
SKIP = 22
MODE_CHANGE = 27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PREV,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(TOGGLE,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SKIP,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(MODE_CHANGE,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

weatherShow = False

modes=["home","music","weather","misc"]

currMode = 0

f = open("/home/pi/jackbot/currents.txt")
content = f.readlines()
temp = content[0].strip()
print("Current Temperature: " + temp + "° F")
currentVibe = int(content[2].strip())
f.close()

mySpot = Spotify()
mySpot.setup()

lcd_init()
#lcd_byte(LCD_LINE_1, LCD_CMD)
time.sleep(0.01)
#lcd_string("prev toggle skip",2)
#lcd_byte(LCD_LINE_2, LCD_CMD)

t = TwitchCount()
print(t.count())

disp = Display()
x=threading.Thread(target=disp.setup, args=(mySpot,temp,currentVibe), daemon=True)
x.start()

#matrix = Matrix()
#y=threading.Thread(target=matrix.run, daemon=True)
#y.start()


try:
    time.sleep(.01)
    mySpot.interact('current')
    while True: 
        if GPIO.input(TOGGLE) == GPIO.HIGH:
            mySpot.interact("toggle")
        elif GPIO.input(PREV) == GPIO.HIGH:
            mySpot.interact("prev")
        elif GPIO.input(SKIP) == GPIO.HIGH:
            mySpot.interact("skip")
        elif GPIO.input(MODE_CHANGE) == GPIO.HIGH:
            if(currMode == 3):
                currMode = 0
            else:
                currMode = currMode + 1
            print(modes[currMode])
            disp.mode = currMode
            time.sleep(1)
except KeyboardInterrupt:
    disp.done = True
    print("exiting...")
    x.join()
except TypeError:
    print("No device found")
    x.join()

GPIO.cleanup()     
