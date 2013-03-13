import time
import common

leds = common.LedPixel(32)
leds.allOff()

def pulse():
   for dir in range(2):
      for r in range(128):
         color = abs(128 * dir - r)
         leds.allColor(color, color, color)
         time.sleep(.001)

def colortest(isr, isg, isb): 
   for color in range(256):
      red = isr * color
      green = isg * color
      blue = isb * color
      leds.allColor(red, green, blue)
      time.sleep(.001)

def togglecolor(r, g, b, isback):
   red = r * 255
   green = g * 255
   blue = b * 255
   for c in range(256):
      if isback == True:
         c = 255 - c
      if r == -1:
         red = c
      if g == -1:
         green = c
      if b == -1:
         blue = c

      leds.allColor(red, green, blue)
      time.sleep(.005)

def allcolors():
   leds.allOff()
   togglecolor(-1, 0, 0, False)
   togglecolor(1, -1, 0, False)
   togglecolor(-1, 1, 0, True)
   togglecolor(0, 1, -1, False)
   togglecolor(0, -1, 1, True)
   togglecolor(-1, 0, 1, False)
   togglecolor(1, -1, 1, False)
   togglecolor(-1, -1, -1, True)
   
while True:
   allcolors()
