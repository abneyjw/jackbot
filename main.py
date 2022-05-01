import time
import keyboard
import threading
from display import *
from lcd import *
from spotify import *
from weather import *
from followers import *
import RPi.GPIO as GPIO



PREV = 21 
TOGGLE = 17 
SKIP = 22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PREV,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(TOGGLE,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SKIP,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

weatherShow = False

n = 0

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

try:
    time.sleep(1)
    print("HE")
    mySpot.interact('current')
    while True: 
        if GPIO.input(TOGGLE) == GPIO.HIGH:
            mySpot.interact("toggle")
        elif GPIO.input(PREV) == GPIO.HIGH:
            mySpot.interact("prev")
        elif GPIO.input(SKIP) == GPIO.HIGH:
            mySpot.interact("skip")
        elif keyboard.is_pressed('e'):
            break
except KeyboardInterrupt:
    disp.done = True
    print("exiting...")
    x.join()
except TypeError:
    print("No device found")
    x.join()

GPIO.cleanup()     
