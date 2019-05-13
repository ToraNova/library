#!/usr/bin/python3

#simple python wrapper which uses mplayer
#sudo apt install mplayer

import subprocess

if __name__ == "__main__":
	
	#main loop
	currentVisual = False
	while True:
		
		user_in = input("Please enter command:")

		if(user_in == "play_tcm"):
			print("Starting video")
			currentVisual = subprocess.Popen(['mplayer','tcm0.mp4'],stdout=subprocess.PIPE, stderr=subprocess.PIPE,
			stdin=subprocess.PIPE)
			#out,err = currentVisual.communicate()
		elif(user_in == "pause" and currentVisual):
			print("Attempting to pause")
			currentVisual.stdin.write(b'p')
			currentVisual.stdin.flush()
		elif(user_in == "exit" and currentVisual):
			print("Attempting to quit")
			currentVisual.stdin.write(b'p')
			currentVisual.stdin.flush()
			currentVisual = False
		elif(user_in == "resume" and currentVisual):
			print("Resuming")
			currentVisual.stdin.write(b'p')
			currentVisual.stdin.flush()
		else:
			print("You have not specified a play_ command or have specified an invalid command")
	
			
