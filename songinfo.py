import lcd
import time

class SongInfo:
    def setup(self, mySpot):
        lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
        while True:
            time.sleep(2)
            lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
            lcd.lcd_string(mySpot.song(),2)
    def display(self, mySpot):
        time.sleep(1)
        lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
        lcd.lcd_string(mySpot.song(),2)
    def dispWeather(self, temp):
        lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
        lcd.lcd_string((temp + ' F'),2)
