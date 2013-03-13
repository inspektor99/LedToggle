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
		self.allColor(0x00, 0x00, 0x00)
	
	def allColor(self, r, g, b):
		for i in range(self.NUM_LEDS - 1):
			self.leds[i * 3 + 0] = r
			self.leds[i * 3 + 1] = g
			self.leds[i * 3 + 2] = b
		self.writeAll() 

	def goHawks(self):
		self.allOff()
		for i in range(self.NUM_LEDS - 1):
			if i % 3 == 0:
				self.leds[i * 3 + 1] = 0xFF
			else:
				self.leds[i * 3 + 2] = 0xFF
			self.writeAll()
			time.sleep(.1)

