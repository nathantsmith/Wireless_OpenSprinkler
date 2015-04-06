import Adafruit_BBIO.UART as UART
import Adafruit_BBIO.GPIO as GPIO
import serial
import time
import gv

UART.setup("UART1")
ser1 = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser1.close()
ser1.open()

class WhiskerRF(object):
	def __init__(self, name, mac):
		#global ser1
		self.name = name
		self.mac = mac
		ser1.write(name + '\r\n')
		ser1.write("MAC: 0x" + "ATTM01".encode("hex").upper() + (mac).encode("hex").upper() + '\r\n')
		ser1.write("Set Master: 0x" + "ATMA".encode("hex").upper() + '\r\n')
	def setMac(self):
		#global ser1
		ser1.write("MAC: 0x" + "ATTM01".encode("hex").upper() + (self.mac).encode("hex").upper() + '\r\n')
	def setMaster(self):
		#global ser1
		ser1.write("Set Master: 0x" + "ATMA".encode("hex").upper() + '\r\n')
	def readADC(self, input):
		#global ser1
		self.input = input
		if input < 4:
			ser1.write("Read ADC AIN%d: 0x" % (input) + ("ATRA%d" % (input + 23)).encode("hex").upper() + '\r\n')
		else:
			print "Error: Not a Valid Analog Input" 
	def setDigital(self, output, level):
		#global ser1
		self.level = level
		self.output = output
		if output <= 2:
			if level == "High":
				ser1.write("Setting Digital Output %d to %s: " % (output, level) + "0x" + ("ATSD%d%d" % (output, 1)).encode("hex").upper() + '\r\n')
			elif level == "Low":
				ser1.write("Setting Digital Output %d to %s: " % (output, level) + "0x" + ("ATSD%d%d" % (output, 0)).encode("hex").upper() + '\r\n')
			else:
				print "Invalid Level"
		else:
			print "Error: Invalid Output"			
	def reset(self):
		print "Resetting"
		print "This is where the reset pin would be brought to ground"
		ser1.write("+++\r\n")
