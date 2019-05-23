#!/usr/bin/python3

'''kill_mosquitto is an attempt to kill a process with python'''

from subprocess import Popen, PIPE
import time

if __name__ == "__main__":

    getpid = Popen(['pgrep','mosquitto'],stdout=PIPE)
    pid = getpid.stdout.readline()[:-1] #ignore the last character
    term = Popen(['kill','-s','SIGTERM',pid])
    term.wait()
