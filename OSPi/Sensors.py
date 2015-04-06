from WhiskerRF import *
import Adafruit_BBIO.UART as UART
import Adafruit_BBIO.GPIO as GPIO
import serial
import time
import gv

UART.setup("UART1")
ser1 = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser1.close()
ser1.open()

class Sensors(WhiskerRF):
	def __init__(self, name, mac):
		global ser1
		self.name = name
		self.mac = mac
		ser1.write(name + '\r\n')
		ser1.write("MAC: 0x" + "ATTM01".encode("hex").upper() + (mac).encode("hex").upper() + '\r\n')
		ser1.write("Set Master: 0x" + "ATMA".encode("hex").upper() + '\r\n')
	def readtemp(self, sensor):
		global ser1
		if sensor == 1:
			#self.temp1 = 72
			self.temp1 = self.readADC(0)
			return self.temp1
			#return "Temperature (F): %d" %self.temp1
            #gv.temp1 = 72
		elif sensor == 2:
			self.temp2 = self.readADC(1)
			return self.temp2
		else:
			print "Error: Invalid Sensor"
	def readmoisture(self, sensor):
		global ser1
		if sensor == 1:
			self.moisture1 = self.readADC(2) #* self.temp1
			return self.moisture1
		elif sensor == 2:
			self.moisture2 = self.readADC(3)
			return self.moisture2
		else:
			print "Error: Invalid Sensor"
	def update(self):
		self.readtemp(1)
		self.readtemp(2)
		self.readmoisture(1)
		self.readmoisture(2)
