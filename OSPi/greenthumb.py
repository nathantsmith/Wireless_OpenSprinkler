from HTTPRequests import *
import Application
import gv
from ospi import *
import ast

###print gv.hub
"""Conditions
if vwc 1 or 2 < ? auto water for set duration
if vwc 1 or 2 > ? shutoff valves for set duration
if temp1 or temp2 < 32 shutoff everything
"""

#hub example
#testhub = {}
gv.hubnames = ast.literal_eval(gv.hubnames)
print gv.hubnames
testhub = {1:["Sensor1","FFAA000A","10110101",72,74, 30, 30]}
D = 60

if (((testhub[1])[3]) > 32) and (((testhub[1])[4]) > 32):
    print "Temperature is ok. Continuing to water."
    if (((testhub[1])[5]) < 20) or (((testhub[1])[6]) < 20):
        valvecontrol = ((testhub[1])[2])
        valvecontrol = map(int,valvecontrol)
        #run once methodology
        i = 0
        for x in valvecontrol:
            x = x * D
            valvecontrol[i] = x
            i = i + 1
        valvecontrol.append(0)
        runonce(valvecontrol)

        #set station methodology
        #valves=map(int,str((testhub[1])[2]))
        #i=0
        #while i<len(valves):
            #if valves[i] == 1:
                #setstation((i+1), 1, 60)
         #   i = i + 1
        #print valves

    elif (((testhub[1])[5]) > 80) or (((testhub[1])[6]) > 80):
        valves=map(int,str((testhub[1])[2]))
        i=0
        while i<len(valves):
            if valves[i] == 1:
                setstation((i+1), 0, 0)
            i = i + 1
        print valves
    else:
        print "Everything is fine. No changes made."
else: 
    print "Temperature is too low. Shutting down all watering."
    shutdown()
