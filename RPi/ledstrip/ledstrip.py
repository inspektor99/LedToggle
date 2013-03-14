import time
import common

leds = common.LedPixel(32)
leds.allOff()

def pulse():
   colorfade(-1, -1, -1, False)
   colorfade(-1, -1, -1, True)

def colorfade(r, g, b, isback):
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
   colorfade(-1, 0, 0, False)
   colorfade(1, -1, 0, False)
   colorfade(-1, 1, 0, True)
   colorfade(0, 1, -1, False)
   colorfade(0, -1, 1, True)
   colorfade(-1, 0, 1, False)
   colorfade(1, -1, 1, False)
   colorfade(-1, -1, -1, True)
#official WSU crimson
#leds.allColor(152, 30, 50)
#official WSU grey
#leds.allColor(94, 106, 113)  
while True:
   #allcolors()
   leds.goCougs()
   #pulse()
