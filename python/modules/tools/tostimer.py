#--------------------------------------------------
# tostimer.py
# tostimer is a one shot timer used for timing activities.
# it functions like a seperate thread, allowing the
# main program to continue execution.
# created 12/12/2018
#--------------------------------------------------

import threading
import time

class ToraTime(threading.Thread):
	
	#moduename and a pkgprint define
	moduname = "toratime"
	def pkgprint(self,*args,**kwargs):
		print("[{}]".format(self.moduname),*args)

	# THIS IS A ONE SHOT TIMER
	incr = 0.01 # 1s per counter
	def __init__(self,tora_id,a_time,verbose=False):
		#a_time is in scale of 0.1s'
		threading.Thread.__init__(self)
		self.id = tora_id
		self.tim_param = a_time
		self.rflag = False #timer is not running
		self.verboseprint = self.pkgprint if verbose else lambda *a, **k: None
		
	def run(self):
		self.rflag = True
		self.verboseprint("Starting ToraTime {} for ".format(self.id),self.tim_param, "*10ms")
		counter = 0 
		while( counter < self.tim_param):
			counter += 1
			time.sleep(self.incr)
			self.verboseprint("ToraTime count: ",counter)
		self.rflag = False
		self.verboseprint("ToraTime {} has stopped".format(self.id))
	

if __name__ == "__main__":
	
	t = ToraTime(0,0)
	while True:
		if(t.rflag):
			pass #do nothing if t is running
		else:
			tim_param = input("Please enter tim_param :")
			t = ToraTime(1,int(tim_param),True)
			t.start()
			
		
	
	
	

	
