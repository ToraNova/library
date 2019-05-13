import time
from memory_profiler import profile

# run this script with 
# python3 -m memory_profiler <name of this script>

class timewith():
    def __init__(self, name=''):
        self.name = name
        self.start = time.time()

    @property
    def elapsed(self):
        return time.time() - self.start

    def checkpoint(self, name=''):
        print('{timer} {checkpoint} took {elapsed} seconds'.format(
            timer=self.name,
            checkpoint=name,
            elapsed=self.elapsed,
        ).strip())

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.checkpoint('finished')
        pass


@profile
def testfunc():
	'''the function that we are interested in profiling
	both exec_time and memory'''
	# USER CUSTOMISABLE CODE
	# ----------------------
	
	L = numpy.linalg.inv(df)

	# /end of USER CUSTOMISABLE CODE
	# please do not edit anything within
	# the user customisable code section
	# to ensure that the memory / time 
	# profiler works
	# ------------------------------

if __name__ == "__main__":
	
	# setup code here
	# USER CUSTOMISABLE CODE
	# ----------------------
	import pandas as pd
	import numpy
	size = 4000
	k = [p for p in range(size)]
	df = pd.DataFrame( numpy.random.randint(0,100,size=(size,size)) )
	print(df)
	# /end of USER CUSTOMISABLE CODE
	# please do not edit anything within
	# the user customisable code section
	# to ensure that the memory / time 
	# profiler works
	# ------------------------------
	
	timer = timewith("Numpy inverse on pandas dataframe")
	testfunc()
	timer.checkpoint("done")
	
	
# 100 cycles
# minimum ex. time out for dsize 100  (0.0012982)
# minimum ex. time out for dsize 2000 (0.0480921)



