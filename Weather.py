#!/usr/bin/python

from Adafruit_BMP085 import BMP085
import time
import subprocess
import re
import sys
import time
import datetime
import rrdtool
import os

# Initialise the BMP085 and use STANDARD mode (default value)
# bmp = BMP085(0x77, debug=True)
bmp = BMP085(0x77)

# To specify a different operating mode, uncomment one of the following:
# bmp = BMP085(0x77, 0)  # ULTRALOWPOWER Mode
# bmp = BMP085(0x77, 1)  # STANDARD Mode
# bmp = BMP085(0x77, 2)  # HIRES Mode
# bmp = BMP085(0x77, 3)  # ULTRAHIRES Mode

rrdpath = os.path.dirname(__file__) + '/weather.rrd'

# DElay in secons
delay = 60

while True:
	temp2 = bmp.readTemperature()
	# Read the current barometric pressure level
	pressure = bmp.readPressure()

	# To calculate altitude based on an estimated mean sea level pressure
	# (1013.25 hPa) call the function as follows, but this won't be very accurate
	altitude = bmp.readAltitude()

	# To specify a more accurate altitude, enter the correct mean sea level
	# pressure level.  For example, if the current pressure level is 1023.50 hPa
	# enter 102350 since we include two decimal places in the integer value
	# altitude = bmp.readAltitude(102350)

	output = subprocess.check_output([os.path.dirname(__file__) + "/Adafruit_DHT", "2302", "4"]);
	matches = re.search("Temp =\s+([0-9.]+)", output)
	if (not matches):
	      time.sleep(3)
	      continue
	temp = float(matches.group(1))

	# search for humidity printout
	matches = re.search("Hum =\s+([0-9.]+)", output)
	if (not matches):
	      time.sleep(3)
	      continue
	humidity = float(matches.group(1))

	#print "Temperature: %.1f C" % temp
	#print "Humidity:    %.1f %%" % humidity

	#print "Temperature: %.2f C" % temp2
	#print "Pressure:    %.2f hPa" % (pressure / 100.0)
	#print "Altitude:    %.2f" % altitude
	timeString = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
	print "%s %.1fC %.1fC %.1f%% %.1fhPa" % (timeString, temp, temp2, humidity, pressure)	
	try:
		ret = rrdtool.update(rrdpath,'N:' + `temp` + ':' + `temp2` + ':' + `humidity` + ':' + str(pressure))
	except:
		if ret: 
			print rrdtool.error()
	time.sleep(delay)
