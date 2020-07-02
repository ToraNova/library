#!/usr/bin/python3

import threading
import time

exitFlag = 0

class TestThread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		#overriden method called on .start()
		print("Starting " + self.name)
		print_time(self.name, 5, self.counter)
		print("Exiting " + self.name)

def print_time(threadName, counter, delay):
	while counter:
		if exitFlag:
			threadName.exit()
		time.sleep(delay)
		print("%s: %s" % (threadName, time.ctime(time.time())))
		counter -= 1

if __name__ == "__main__":

	# Create new threads
	thread1 = TestThread(1, "Thread-1", 1)
	thread2 = TestThread(2, "Thread-2", 2)

	# Start new Threads
	thread1.start()
	thread2.start()

        # wait for threads to stop
        thread1.join()
        thread2.join()

	print("Exiting Main Thread")
