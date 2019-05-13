# 2019 Toranova mailto: chia_jason96@live.com
# Event based threads with threading events

import threading
import time

class EventThreads(threading.Thread):

    def __init__(self):
        # initilize the threading obj
        threading.Thread.__init__(self)
        self._kill_event = threading.Event() #allows stopping, this flag is the stop flag
        self._msg_avail = threading.Event() #allows message pasing to the thread

        #clears the event flags
        self._kill_event.clear()
        self._msg_avail.clear()
        

    def killthread(self):
        # kills the thread
        self._kill_event.set()

    def resuthread(self):
        # resurrects the thread LAZARUS!
        self._kill_event.clear()

    def pushmsg(self,msg_string):
        # passes a variable into the thread during thread execution
        self.push_string = msg_string
        self._msg_avail.set() #set the flag to allow the main body to run

    def run(self):
        # main thread body

        if(not self._kill_event.is_set()):

            ########################################################################################
            # SETUP CODE # TODO
            ########################################################################################
            printf("Starting EventThread")

            ########################################################################################
            try:
                while not self._kill_event.is_set() :

                    self._msg_avail.wait() #threading block mechanism
                    self._msg_avail.reset()
                    

                    ########################################################################################
                    # Main Loop CODE # TODO
                    ########################################################################################
                    printf("Msg avail event raised:",self.push_string)

                    ########################################################################################

            except Exception as e:
                printf("Exception has occurred:",str(e))
            finally:
        else:
            printf("Thread killed before start")
