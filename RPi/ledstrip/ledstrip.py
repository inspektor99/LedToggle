import time
import common

leds = common.LedPixel(32)
leds.allOff()

def pulse():
   for dir in range(2):
      for r in range(128):
         color = 0x00 | abs(128 * dir - r)
         leds.allColor(color, color, color)
         time.sleep(.001)

def colortest(): 
   for r in range(256):
      red = 0x00 | r
      leds.allColor(0xFF, red, 0x00)
      time.sleep(.001)

while True:
   pulse()
   leds.goHawks()
   pulse()
   pulse()
   colortest()
   pulse()
