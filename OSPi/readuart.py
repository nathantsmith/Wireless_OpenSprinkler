import Adafruit_BBIO.UART as UART
import serial
import time

UART.setup("UART1")
UART.setup("UART2")

ser1 = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser2 = serial.Serial(port = "/dev/ttyO2", baudrate=9600)
if(ser1.isOpen()==False):
    ser1.open()
    print "ser1 open"
if(ser2.isOpen()==False):
    ser2.open()

#test = ser1.readline()
#print test
while 1:
    test = ser2.readline()
    print test
