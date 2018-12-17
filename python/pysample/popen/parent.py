#!/usr/bin/python3

import sys
import time
import subprocess

if __name__ == "__main__":

	while True:
		print("Launching child process")
		childproc = subprocess.Popen(['./child.py','000'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		try:
			out,err = childproc.communicate(timeout=5)
			print("STDOUT:",out,"/ STDERR:",err)
		except Exception as e:
			print("Exception has occurred:",str(e))
			out,err = childproc.communicate()
			print("STDOUT:",out,"/ STDERR:",err)
			

