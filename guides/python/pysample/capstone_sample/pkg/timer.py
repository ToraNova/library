#!/usr/bin/python3

import threading
import time
from pkg import fileman
import os

class ToraTime(threading.Thread):
	# THIS IS A ONE SHOT TIMER
	incr = 0.001 # 1 ms per counter
	def __init__(self,a_time,a_print=True):
		threading.Thread.__init__(self)
		self.tim_param = 0
		self.tim_param = a_time
		self.rf = False #timer is not running
		self.print = a_print
		
	def run(self):
		self.rf = True
		fileman.createFiles(['t.run'],'flags')
		print("Starting ToraTime for ",self.tim_param, "ms")
		counter = 0 
		while( counter < self.tim_param):
			counter += 1
			time.sleep(self.incr)
			if(self.print):
				print("ToraTime :",counter)
		self.rf = False
		print("ToraTime has stopped")
		os.remove(os.path.join('flags','t.run'))
	

if __name__ == "__main__":
	
	t = ToraTime(0)
	while True:
		if(t.rf):
			pass #do nothing if t is running
		else:
			tim_param = input("Please enter tim_param:")
			t = ToraTime(int(tim_param))
			t.start()
			
		
	
	
	

	
