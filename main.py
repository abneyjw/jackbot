import time
import keyboard
import threading
from songinfo import *
from lcd import *
from spotify import *
from weather import *
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
f.close()

mySpot = Spotify()
mySpot.setup()

nice = [1,2,3,4,5,14,21,30,32,33,34]
cozy = [6,7,8,11,12,13,18,35,36,37,38,39,40]
storm = [15,16,17,24,25,26,41,42]
winter = [19,20,21,22,23,29,31,43,44]

lcd_init()
lcd_byte(LCD_LINE_1, LCD_CMD)
time.sleep(0.01)
lcd_string("prev toggle skip",2)
lcd_byte(LCD_LINE_2, LCD_CMD)

songInfo = SongInfo()
songInfo.display(mySpot)

try:
    mySpot.interact('current')
    while True: 
        if GPIO.input(TOGGLE) == GPIO.HIGH:
            mySpot.interact("toggle")
            time.sleep(0.01)
            if(weatherShow):
                songInfo.display(mySpot)
                weatherShow = False
            else:
                songInfo.dispWeather(temp)
                weatherShow = True
        elif GPIO.input(PREV) == GPIO.HIGH:
            mySpot.interact("prev")
            time.sleep(0.01)
            songInfo.display(mySpot)
        elif GPIO.input(SKIP) == GPIO.HIGH:
            mySpot.interact("skip")
            time.sleep(0.01)
            songInfo.display(mySpot)
        elif keyboard.is_pressed('e'):
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

GPIO.cleanup()     
