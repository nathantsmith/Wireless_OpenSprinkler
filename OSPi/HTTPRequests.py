import urllib2

def setstation(station, status, duration):
	setmode("manual")
	station = str(station)
	status = str(status)
	duration = str(duration)
	cite = urllib2.urlopen('http://localhost:8080/sn' + station + '=' + status + '&t=' + duration)
	cite.close()

def setmode(mode):
	if mode == "auto":
		modeset = urllib2.urlopen('http://localhost:8080/cv?pw=opendoor&en=&mm=0&rd=&wl=&rbt=0')
		modeset.close()
	elif mode == "manual":
		modeset = urllib2.urlopen('http://localhost:8080/cv?pw=opendoor&en=&mm=1&rd=&wl=&rbt=0')
		modeset.close()

def startup():
	startup = urllib2.urlopen('http://localhost:8080/cv?pw=opendoor&en=1')
	startup.close()

def shutdown():
	shutdown = urllib2.urlopen('http://localhost:8080/cv?pw=opendoor&en=0')
	shutdown.close()

def runonce(runOnceArray):
        runOnceArray = str(runOnceArray).replace(" ","")
	runonce = urllib2.urlopen('http://localhost:8080/cr?pw=opendoor&t=' + runOnceArray)
	runonce.close()

def getstationstatus():
	getstatus =  urllib2.urlopen('http://localhost:8080/js?pw=opendoor')
	print getstatus.read()
	getstatus.close()

def getstationnames():
	getnames = urllib2.urlopen('http://localhost:8080/jn?pw=opendoor')
        print getnames.read()
	getnames.close()

def getcontrollervariables():
	getcontroller = urllib2.urlopen('http://localhost:8080/jc?pw=opendoor')
	print getcontroller.read()
	getcontroller.close()

def resetstations():
	resetstations = urllib2.urlopen('http://localhost:8080/cv?pw=opendoor&rsn=1')
	resetstations.close()

def moveupprogram(program):
    program = str(program)
    print program
    programup = urllib2.urlopen('http://localhost:8080/up?pw=opendoor&pid=' + program)
    programup.close()


#moveupprogram(1)
#array = [60,60,60,60,60,60,60,60,0]
#runonce(array)

#test = urllib2.urlopen('http://localhost:8080/cr?pw=opendoor&t=[60,0,60,0,60,0,600,0]')
#test.close()

#i = 1
#while i<=8:
#    setstation(i,1,60)
#    i = i + 1
#time.sleep(20)
#setmode("auto")
