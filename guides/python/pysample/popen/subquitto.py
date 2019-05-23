#!/usr/bin/python3

'''subquitto.py is my attempt to run a mosquitto broker with python
this allows me to configure the client using python and ultimately
be able to run it as a web service

requires mosquitto to be installed and the executable location
set to the system PATH'''

from subprocess import Popen, PIPE
import time

if __name__ == "__main__":

    mqbroker = Popen(['mosquitto'],\
            stdout=PIPE)
    while True:
        try:
            #this blocks when there is no input
            bout = mqbroker.stdout.readline()
            if( len(bout) <= 0):
                mqbroker.terminate()
                time.sleep(1)
                print("Outlen <= 0, aborting")
                break
            print(bout)
            time.sleep(0.1)
        except KeyboardInterrupt:
            mqbroker.terminate()
            time.sleep(2)
            print("Terminated")
            exit()
        except Exception as e:
            print("Exception has occurred:",str(e))
