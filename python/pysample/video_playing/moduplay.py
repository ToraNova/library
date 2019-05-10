#!/usr/bin/python3

#simple python wrapper which uses mplayer
#sudo apt install mplayer

import subprocess
class omxhandler():
	filemapping = {
		200:'videos/tcm0.mp4'
	}
	def __init__(self,player):
		self.currentVisual = False
		self.player = player

	def play(self,target):
		#launches a new video
		self.currentVisual = subprocess.Popen([self.player,self.filemapping[target] ],
			stdout=subprocess.PIPE, stderr=subprocess.PIPE,
			stdin=subprocess.PIPE)
		return True

	def pause(self):
		if(self.currentVisual):
			#pauses the current video
			#call this again to resume
			self.currentVisual.stdin.write(b'p')
			self.currentVisual.stdin.flush()
			return True #success
		else:
			return False #fail

	def stop(self):
		if(self.currentVisual):
			#stops the current video
			self.currentVisual.stdin.write(b'q')
			self.currentVisual.stdin.flush()

			self.currentVisual = False
			return True #success
		else:
			return False #fail
					
#handler = omxhandler()
#handler.start()

#handler.play(201)
#handler.pause()
#handler.stop()
if __name__ == "__main__":

	p = omxhandler('mplayer')
	while True:
		
		user_in = input("Please enter command:")
	
		if(user_in == "200"):
			p.play(200)
		elif(user_in == "pause"):
			p.pause()
		elif(user_in == "exit"):
			p.stop()
		elif(user_in == "resume"):
			p.pause()
		else:
			print("You have not specified a play_ command or have specified an invalid command")
	
			
