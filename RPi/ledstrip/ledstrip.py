import time
import common

leds = common.LedPixel(32)
leds.allOff()

def pulse():
   for dir in range(2):
      for r in range(128):
         color = 0x00 | abs(128 * dir - r)
         leds.allColor(color, 0x00, color)
         time.sleep(.001)

while True:
   pulse()
