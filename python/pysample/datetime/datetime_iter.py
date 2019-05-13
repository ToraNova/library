#!/usr/bin/python3

#235945
#235946
#.
#.
#235959
#000000

class t24h_itero():
	#class to iterate a 24hr format string
	hour = None
	minu = None
	seco = None

	def __init__(self,start):
		#constructor to init
		self.hour = int(start[:2])
		self.minu = int(start[2:4])
		self.seco = int(start[-2:])
		self.cycle = 0

	def getTime(self):
		out = ''
		if(self.hour < 10):
			out += '0'
		out += str(self.hour)
		if(self.minu < 10):
			out += '0'
		out += str(self.minu)
		if(self.seco < 10):
			out += '0'
		out += str(self.seco)
		return out

	def iter(self):
		self.seco += 1
		if(self.seco > 59):
			self.seco = 0
			self.minu += 1
			if(self.minu > 59):
				self.minu = 0
				self.hour += 1
				if(self.hour > 23):
					self.hour = 0
					self.cycle += 1
		return	 		

if __name__ == "__main__":

	t = t24h_itero("235959")
	endT = "000102"
	
	while( t.getTime() != endT):
		print(t.getTime())
		t.iter()
	
