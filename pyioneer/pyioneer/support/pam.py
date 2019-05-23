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

class Pam:
    '''Pam - printing assistant module, handles all forms of printing thingy
    to lighten load while developping dem programz'''

    nothing = lambda *a : None
        
    ################################################################################
    # Interface methods (use super().shutup() / tell() or verboseonly() )
    ################################################################################
    def controlpam(self, verbose=True, debug=True, error=True, warn=True, info=True, raw=True):
        '''main control function to toggle on/off behaviours for printing/loggin'''
        self.verbose = gpam.vprint if verbose else  self.nothing
        self.debug   = gpam.dprint if debug else    self.nothing
        self.error   = gpam.eprint if error else    self.nothing
        self.warn    = gpam.wprint if warn else     self.nothing
        self.info    = gpam.iprint if verbose else  self.nothing
        self.raw     = gpam.rprint if raw else      self.nothing

    def shutup(self):
        '''stops ALL printing, except EXCEPTIONS'''
        self.controlpam( False, False, False, False ,False, False)

    def quiet(self):
        '''suppress all verbose,warning, info raw. Errors and exception still displays'''
        self.controlpam( False, False, True, True, False, False)

    def sorry(self):
        '''enable all printing for the module'''
        self.controlpam( True, True, True, True, True, True)

    def verboseonly(self):
        '''only allow verboses (exception,warning and errrors are always enabled)'''
        self.controlpam( True, False, True, True, True, False) 

    ################################################################################

    ################################################################################
    # Constructor. use super().__init__( t/f, t/f, .., t/f ) to change default behavior
    # please do not rmb the sequence, use the names instead.
    ################################################################################
    def __init__(self, verbose=True, debug=True, error=True, warn=True, info=True, raw=True):
        '''use super().__init__() to initialize debugging and verbose mode,
        if super().__init__() is not called, then no debugging or verbose will
        start unless super().tell() or super().verboseonly() is called.'''
        self.controlpam( verbose, debug, error, warn, info, raw )
    ################################################################################
    
    ################################################################################
    # Default setup
    ################################################################################
    expt    = gpam.exprint
    error   = gpam.eprint
    warn    = gpam.wprint
    verbose     = nothing
    debug       = nothing
    raw         = nothing
    info        = nothing
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
        self.raw("THIS IS RAWWWWWRRRR")
        self.warn("Warning. Yellow alert!")
        super().shutup()
        self.verbose("this won't come out")
        self.error("Errors are important")
        self.debug("this is silent as well")
        self.raw("ok i shutup")
        super().sorry()
        self.debug("It's okay to say manythings again")
        super().verboseonly()
        self.verbose("verbose")
        self.debug("debug")
        self.info("infoooooo")
        self.verbose( "verbose without date")
        self.expt("test")

# Test script
if __name__ == "__main__":
    
    p = Pam_Test(True,True,True,True,True)
    p.test()
    print("Test OK for",__file__)

