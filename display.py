from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
import lcd
import time
import math
from songtracking import *


class Display:
    done = False
    pastId = ""

    music = [(4,0),(4,1),(5,1),(4,2),(5,2),(6,2),(4,3),(6,3),(2,4),(3,4),(4,4),
            (1,5),(2,5),(3,5),(4,5),(1,6),(2,6),(3,6),(4,6),(2,7),(3,7)]

    house = [(3,1),(4,1),(2,2),(3,2),(4,2),(5,2),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),
            (0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),(1,5),(2,5),(3,5),(4,5),
            (5,5),(6,5),(1,6),(2,6),(5,6),(6,6),(1,7),(2,7),(5,7),(6,7)]

    sun = [(1,1),(3,1),(4,1),(6,1),(5,2),(2,2),(1,3),(6,3),(1,4),(6,4),
            (2,5),(5,5),(1,6),(3,6),(4,6),(6,6)]


    twitch = [(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(0,1),(1,1),(7,1),
            (0,2),(1,2),(3,2),(5,2),(7,2),(0,3),(1,3),(3,3),(5,3),(7,3),
            (0,4),(1,4),(7,4),(0,5),(1,5),(2,5),(5,5),(6,5),(2,6),(3,6),(4,6),
            (5,6),(3,7)]

    mode = ""
    img = []

    serial = spi(port=0,device=0,gpio=noop())
    device = max7219(serial,rotate=2)
   

    def setup(self, mySpot, temp, vibe):
        lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
        self.vibe = vibe
        self.st = songTracking()
        #self.st.rec(self.vibe, mySpot)
        while (not self.done):
            try:   
                time.sleep(0.1)
                self.run()
                if(self.mode == 1):
                    self.displaySong(mySpot,temp)
                else:
                    self.displayHome()
            except Exception as e:
                print(e)
        self.close()
    
    def displayHome(self):
        lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
        lcd.lcd_string("Which way",2)
        lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
        lcd.lcd_string("western man?",2)
        self.img = self.house

    def displaySong(self, mySpot, temp):
        lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
        self.img = self.music
        if(mySpot.playing()):
            time.sleep(0.01)
            lcd.lcd_string((mySpot.song()),2)
            prog = (mySpot.progress()/.07)
            progString = "|"
            progString = progString + (math.floor(prog)*'#')
            progString = progString + (int(14-math.floor(prog))*'-') + '|'
            time.sleep(0.1)
            lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
            lcd.lcd_string(progString,2)
            if (prog > 8):
                self.myId = mySpot.id()
                if (not (self.myId == self.pastId)):
                    self.st.track(self.vibe,mySpot)
                    self.pastId = self.myId
                    
        else:
            time.sleep(0.01)
            lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
            lcd.lcd_string('--paused--',2)

    def close(self):
        time.sleep(0.01)
        lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
        lcd.lcd_string("",2)
        lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
        lcd.lcd_string("Goodbye!",2)
        time.sleep(3)
        lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
        lcd.lcd_string("",2)

    def run(self):
        with canvas(self.device) as draw:
            draw.point(self.img, fill=(0xFFFFFF))
