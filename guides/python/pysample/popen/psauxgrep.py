#!/usr/bin/python3

'''this scripts shows how to use grep and pipe in python'''

from subprocess import Popen, PIPE
import time

if __name__ == "__main__":

    target_process = 'mosquitto'
    ps = Popen(['ps','aux'],\
            stdout=PIPE)
    vgrep = Popen(['grep','-v','grep'],\
            stdin=ps.stdout, stdout=PIPE)
    grep = Popen(['grep',target_process],
            stdin=vgrep.stdout,stdout=PIPE)
    try:
        out,err = grep.communicate(timeout=5)
        if(len(out) <=0):
            print (False) #program not running
        else:
            print (True) #positive
    except Exception as e:
        print("Exception as occurred:",str(e))

