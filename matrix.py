from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
import time

class Matrix:
    def run(self):
        serial = spi(port=0,device=0,gpio=noop())
        device = max7219(serial,rotate=2)
        
        for i in range(0,4):
            with canvas(device) as draw:
                draw.rectangle([3-i,3-i,4+i,4+i], outline="white",fill = "black")
            time.sleep(0.1)

        music = [(4,0),(4,1),(5,1),(4,2),(5,2),(6,2),(4,3),(6,3),(2,4),(3,4),(4,4),
                (1,5),(2,5),(3,5),(4,5),(1,6),(2,6),(3,6),(4,6),(2,7),(3,7)]


        with canvas(device) as draw:
            draw.point(music, fill=(0xFFFFFF))
            time.sleep(10)

