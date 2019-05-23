#!/usr/bin/python3

'''subquitto.py is my attempt to run a mosquitto broker with python
this allows me to configure the client using python and ultimately
be able to run it as a web service

requires mosquitto to be installed and the executable location
set to the system PATH'''

# TODO: Please read on this
# http://www.steves-internet-guide.com/mosquitto-logging/
from subprocess import Popen, PIPE
import time

if __name__ == "__main__":

    mqbroker = Popen(['mosquitto'],stdout=PIPE)
    runflag = True
    while runflag:
        try:
            #this blocks when there is no input
            for line in mqbroker.stdout:
                print("mosquitto:",line)
                if( len(line) <= 0):
                    mqbroker.terminate()
                    time.sleep(1)
                    print("Outlen <= 0, aborting")
                    runflag = False
                    break
            print("...")
            time.sleep(0.1)
        except KeyboardInterrupt:
            print("Exit")
        except Exception as e:
            print("Exception has occurred:",str(e))
        finally:
            mqbroker.terminate()
            time.sleep(2)
            print("Terminated")
            exit()
