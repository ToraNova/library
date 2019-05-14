################################################################################
# pam.py - inspired by cute pammy from the office
# Pam is a class which implements some of the printing functions
# that I normally would use. the printing functions are only for 
# the standard output and may not do logging as of version 1.0 of this
# 
# @Author ToraNova
# @mailto chia_jason96@live.com
# @version 1.0
# @date 13 May 2019
################################################################################

################################################################################
# dependencies import
from abc import ABC, abstractmethod
import datetime, inspect
################################################################################
# local imports (import as if the library is a sys library)
from pyioneer.constant import ansicolor, constring
from pyioneer.support import gpam
################################################################################

class Pam(ABC):
    '''Pam - printing assistant module, handles all forms of printing thingy
    to lighten load while developping dem programz'''
        
    ################################################################################
    # Interface methods (use super().shutup() / tell() or verboseonly() )
    ################################################################################
    def shutup(self):
        '''stops the base class for verbose and debug printing (and raw)'''
        self.verbose = lambda *a: None
        self.debug   = lambda *a: None
        self.rawpr   = lambda *a: None

    def tell(self):
        '''allows the base class for verbose and debug printing (and raw)'''
        self.verbose = gpam.gpam_vprint
        self.debug   = gpam.gpam_dprint
        self.rawpr   = gpam.gpam_rprint

    def verboseonly(self):
        '''only allow verboses'''
        self.verbose = gpam.gpam_vprint
        self.rawpr   = lambda *a: None
        self.debug   = lambda *a: None
    ################################################################################

    ################################################################################
    # Constructor. use super().__init__( t/f, t/f, t/f ) to change default behavior
    ################################################################################
    def __init__(self,verbose=True,debug=True,warn=True,error=True,raw=True):
        '''use super().__init__() to initialize debugging and verbose mode,
        if super().__init__() is not called, then no debugging or verbose will
        start unless super().tell() or super().verboseonly() is called.'''
        self.verbose = gpam.gpam_vprint if verbose else lambda *a: None
        self.debug   = gpam.gpam_dprint if debug else lambda *a: None
        self.error   = gpam.gpam_eprint if error else lambda *a: None
        self.warn    = gpam.gpam_wprint if warn else lambda *a:None
        self.rawpr   = gpam.gpam_rprint if raw else lambda *a:None
    ################################################################################
    
    ################################################################################
    # Default setup
    ################################################################################
    error = gpam.gpam_eprint
    warn = gpam.gpam_wprint
    verbose = lambda *a: None
    debug = lambda *a: None
    ################################################################################

# Test class
class Pam_Test(Pam):

    def __init__(self,verbose,debug,warn,error,raw):
        super().__init__(verbose,debug,warn,error,raw) #allow default behavioural changing

    def test(self):
        self.verbose("Hello")
        self.debug("This is a serious debugging message")
        self.error("An error has occurred?!")
        self.verbose("Nope")
        self.rawpr("THIS IS RAWWWWWRRRR")
        self.warn("Warning. Yellow alert!")
        super().shutup()
        self.verbose("this won't come out")
        self.error("Errors are important")
        self.debug("this is silent as well")
        self.rawpr("ok i shutup")
        super().tell()
        self.debug("It's okay to say manythings again")
        super().verboseonly()
        self.verbose("verbose")
        self.debug("debug")

# Test script
if __name__ == "__main__":
    
    p = Pam_Test(True,True,True,True,True)
    p.test()
    gpam.disable_gpam()
    p.test() # disabling gpam is useless eventhough pam uses it

