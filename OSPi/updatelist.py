from ospi import *
import ast
import Adafruit_BBIO.UART as UART
import serial
import time

UART.setup("UART1")
UART.setup("UART2")

ser1 = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser2 = serial.Serial(port = "/dev/ttyO2", baudrate=9600)

if(ser1.isOpen()==False):
    ser1.open()
if(ser2.isOpen()==False):
    ser2.open()

while 1:
    gv.hubnames = data('hubnames')
    
    gv.hubnames = ast.literal_eval(gv.hubnames)
    
    uartstring = ser2.readline()
    uartstring = uartstring.replace("\r\n", "")
    uartlist = uartstring.split(",")

    i=0
    for x in gv.hubnames:
        if (uartlist[0] == x[1]):
            if (len(gv.hubnames[i]))==3:
                gv.hubnames[i].extend(uartlist[1:5])
            elif (len(gv.hubnames[i]))==7:
                for j in range(3,7):
                    ((gv.hubnames[i])[j]) = uartlist[j-2]
        i = i + 1

    hubnames = str(gv.hubnames)
    save('hubnames', hubnames)
