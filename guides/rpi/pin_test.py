#!/usr/bin/python3

# Simple python-gpio for raspberry pi GPIO detection
# uses callback events

import time, sys
import RPi.GPIO as gpio

if __name__ == "__main__":

	if( len(sys.argv) < 2):
		testpin = 17 #default
	else:
		try:
			testpin = int(sys.argv[1])
		except Exception:
			testpin = 17
		
	print("Testing pin",testpin," on gpio.BCM")
	gpio.setmode(gpio.BCM) #setup board configuration mode
	gpio.setup(testpin, gpio.IN, pull_up_down = gpio.PUD_UP)

	try:	
		while True:	
			print("pin",testpin,gpio.input(testpin))
			time.sleep(0.5)
	except KeyboardInterrupt:
		print("End test.")
	finally:
		gpio.cleanup()
		exit(0)
	
	
