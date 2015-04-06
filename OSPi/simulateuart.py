import Adafruit_BBIO.UART as UART
import serial
import time

UART.setup("UART1")
UART.setup("UART2")
UART.setup("UART4")
UART.setup("UART5")

#serusb = serial.Serial(port = "/dev/ttyUSB0", baudrate=115200)
ser1 = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser2 = serial.Serial(port = "/dev/ttyO2", baudrate=9600)
ser4 = serial.Serial(port = "/dev/ttyO4", baudrate=9600)
ser5 = serial.Serial(port = "/dev/ttyO5", baudrate=9600)

if(ser1.isOpen()==False):
	ser1.open()
if(ser2.isOpen()==False):
	ser2.open()
if(ser4.isOpen()==False):
	ser3.open()
if(ser5.isOpen()==False):
	ser4.open()

#serusb.write("+++")
while 1:
    ser1.write("MAC Address 1,71,71,61,61\r\n")
    print "Sent MAC Address 1"
    time.sleep(5)
    ser1.write("MAC Address 2,72,72,62,62\r\n")
    print "Sent MAC Address 2"
    time.sleep(5)
    ser1.write("MAC Address 3,73,73,63,63\r\n")
    print "Sent MAC Address 3"
    time.sleep(5)
#while 1:
#	input = raw_input(">> ")
#	if input == 'exit':
#		ser1.close()
#		ser2.close()
#		ser4.close()
#		ser5.close()
#		exit()
#	else:
#		ser2.write(input + '\n')
#		out = ''
#		time.sleep(1)
#		while ser2.inWaiting() > 0:
#			out += ser2.read(1)
#		if out != '':
#			print ">> " + out
