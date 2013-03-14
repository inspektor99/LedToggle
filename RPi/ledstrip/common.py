import time

class LedPixel:
   dev = "/dev/spidev0.0"
   spidev = file(dev, "wb")

   NUM_LEDS = 32
   def __init__(self, numleds):
      self.NUM_LEDS = numleds
      self.leds = bytearray(3 * self.NUM_LEDS)
	
   def writeAll(self):
      self.spidev.write(self.leds)
      self.spidev.flush()

   def allOff(self):
      self.allColor(0, 0, 0)

   #NOTE: this does not write to strip
   def colorLed(self, index, r, g, b):
      self.leds[index * 3 + 0] = 0x00 | r
      self.leds[index * 3 + 1] = 0x00 | g
      self.leds[index * 3 + 2] = 0x00 | b
      
   def allColor(self, r, g, b):
      for i in range(self.NUM_LEDS - 1):
         self.colorLed(i, r, g, b)
      self.writeAll() 

   def goCougs(self):
      self.allOff()
      for i in range(self.NUM_LEDS - 1):
         if i % 4 == 0:
            #self.colorLed(i, 0, 255, 0)
            self.colorLed(i, 94, 106, 113)
         else:
            self.colorLed(i, 152, 30, 50)
            #self.colorLed(i, 0, 0, 255)
         self.writeAll()
         time.sleep(.1)
      for j in range(self.NUM_LEDS - 1):
         #self.colorLed(self.NUM_LEDS - 1 - j, 0, 0, 0)
         self.colorLed(j, 0, 0, 0)
         self.writeAll()
         time.sleep(.1)

