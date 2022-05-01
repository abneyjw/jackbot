import lcd
import time
import math
from songtracking import *


class Display:
    done = False


    def setup(self, mySpot, temp, vibe):
        lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
        self.vibe = vibe
        st = songTracking()
        st.track(self.vibe,mySpot)
        while (not self.done):
            try:   
                time.sleep(0.1)
                self.display(mySpot,temp)
            except TypeError as e:
                print(e)
        self.close()

    def display(self, mySpot, temp):
        lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
        if(mySpot.playing()):
            time.sleep(0.1)
            lcd.lcd_string((mySpot.song()),2)
            prog = (mySpot.progress()/.07)
            progString = "|"
            progString = progString + (math.floor(prog)*'#')
            progString = progString + (int(14-math.floor(prog))*'-') + '|'
            time.sleep(0.1)
            lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
            lcd.lcd_string(progString,2)
        else:
            time.sleep(0.1)
            lcd.lcd_string((temp + ' F'),2)
            time.sleep(0.1)
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


