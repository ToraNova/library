#!/usr/bin/python3

from subprocess import Popen, PIPE
import time

if __name__ == "__main__":

    proc = Popen(['ping','localhost'],stdout=PIPE)
    runflag = True
    while runflag:
        try:
            #this blocks when there is no input
            # one could also use 
            # proc.stdout.readline()
            for line in proc.stdout:
                print("POPING STDOUT:",line)
                if( len(line) <= 0):
                    proc.terminate()
                    time.sleep(1)
                    print("linelen <= 0, aborting")
                    runflag = False
                    break
            time.sleep(0.5)
        except KeyboardInterrupt:
            print("Exit")
        except Exception as e:
            print("Exception has occurred:",str(e))
        finally:
            proc.terminate()
            time.sleep(0.1)
            print("Terminated")
            exit()
