#!/usr/bin/python3
import time

def dangerous(a,b):
	if(b==0):
		#do something
		raise ZeroDivisionError('b must not be zero')
	out = a/b
	return out

if __name__ == "__main__":
	
	for i in range(5):
		try:
			time.sleep(0.5)
			print(dangerous(i,0))
			print('hi')
		except ZeroDivisionError:
			print("You are stupid")
		except KeyboardInterrupt:
			print("Halted")



	
