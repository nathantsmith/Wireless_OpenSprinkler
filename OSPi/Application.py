from Sensors import *
import gv

datafile = open('sensorlist.txt')
data = []
for row in datafile:
    data.append(row.strip().split(' '))

sensorData = {}	
with open('sensorlist.txt') as file:
    for num, line in enumerate(file, 1):
        datanum = num - 1
        sensorData[datanum] = data[datanum]

gv.sensor = []
i=0
while i<len(sensorData):
#    gv.sensor.append(Sensors(((sensorData[i])[0]), ((sensorData[i])[1])))
#    gv.sensor[i].update()
    i = i + 1

gv.hub = {}
gv.hub = sensorData
i = 0
while i<len(sensorData):
    gv.hub[i].append("temp1")
    gv.hub[i].append("temp2")
    gv.hub[i].append("vwc1")
    gv.hub[i].append("vwc2")
    gv.hub[i].append("vctrl")
    i = i + 1
#print gv.hub

#class test():
#    gv.test=self.readtemp(1)

#sensor[0].update()
#sensor[0].readtemp(1)
#sensor[0].readmoisture(1)
#sensor[0].readADC(1)
#sensor[0].setMac()
#sensor[0].setMaster()
