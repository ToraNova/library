################################################################################
# pam.py - inspired by cute pammy from the office
# Pam is a class which implements some of the printing functions
# that I normally would use. the printing functions are only for 
# the standard output and may not do logging as of version 1.0 of this
# 
# @Author ToraNova
# @mailto chia_jason96@live.com
# @version 1.0
################################################################################

################################################################################
# dependencies import
from abc import ABC, abstractmethod
import datetime, inspect
################################################################################


class Pam(ABC):
    '''Pam - printing assistant module, handles all forms of printing thingy
    to lighten load while developping dem programz'''
    
    ################################################################################
    # Printing implementations
    ################################################################################
    def pkgprint(self,*args,**kwargs):
        '''prints the date and the filename and func name of the caller function
        mainly for debugging purposes. use with debugprint()'''
        cfilename, cfuncname = self.callerDetails() #obtain caller details
        print(self.dateDetails(self.d2fstr),cfilename,cfuncname,*args)

    def dprint(self, *args, **kwargs):
        '''prints the date information only. does not include caller and file and
        function name. suitable for verboses'''
        print(self.dateDetails(self.d2fstr),*args)

    def eprint(self, *args, **kwargs):
        '''error printing function. this prints the text in red'''
        print(self.ccode_red_seq + self.dateDetails(self.d2fstr), *args, self.ccode_ntext_seq)
    ################################################################################
        
    ################################################################################
    # Interface methods (use super().shutup() / tell() or verboseonly() )
    ################################################################################
    def shutup(self):
        '''stops the base class for verbose and debug printing'''
        self.verbose = lambda *a: None
        self.debug = lambda *a: None

    def tell(self):
        '''allows the base class for verbose and debug printing'''
        self.verbose = self.dprint
        self.debug = self.pkgprint

    def verboseonly(self):
        '''only allow verboses'''
        self.verbose = self.dprint
        self.debug = lambda *a: None
    ################################################################################

    ################################################################################
    # Constructor. use super().__init__( t/f, t/f, t/f ) to change default behavior
    ################################################################################
    def __init__(self,verbose=True,debug=True,error=True):
        '''use super().__init__() to initialize debugging and verbose mode,
        if super().__init__() is not called, then no debugging or verbose will
        start unless super().tell() or super().verboseonly() is called.'''
        self.verbose = self.dprint if verbose else lambda *a: None
        self.debug = self.pkgprint if debug else lambda *a: None
        self.error = self.eprint if error else lambda *a: None
    ################################################################################
    
    ################################################################################
    # Default setup and internal formatting
    ################################################################################
    error = eprint
    verbose = lambda *a: None
    debug = lambda *a: None

    dfstr = "[%Y/%m/%d %a %H:%M:%S]"
    d2fstr = "[%Y/%m/%d %a %H:%M:%S.%f]"
    ccode_ntext_seq = "\033[0;37;40m" # use this to go back to normal text
    ccode_red_seq = "\033[1;31;40m" # preprends this for red texts
    ################################################################################

    ################################################################################
    # Macros
    ################################################################################
    def dateDetails(self,sformat):
        #easy datetime macro
        return datetime.datetime.now().strftime(sformat)
        
    def callerDetails(self):
        #easy caller filename/funcname macro
        cframe = inspect.stack()[1]
        module = inspect.getmodule(cframe[0])
        cfilename = module.__file__
        cfuncname = cframe.function
        return cfilename, cfuncname
    ################################################################################


# Test class
class Pam_Test(Pam):

    def __init__(self,verbose,debug,error):
        super().__init__(verbose,debug,error) #allow default behavioural changing

    def test(self):
        self.verbose("Hello")
        self.debug("This is a serious debugging message")
        self.error("An error has occurred?!")
        self.verbose("Nope")
        super().shutup()
        self.verbose("this won't come out")
        self.error("Errors are important")
        self.debug("this is silent as well")
        super().tell()
        self.debug("It's okay to say manythings again")
        super().verboseonly()
        self.verbose("verbose")
        self.debug("debug")

# Test script
if __name__ == "__main__":
    
    p = Pam_Test(True,True,True)
    p.test()

