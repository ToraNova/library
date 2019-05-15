################################################################################
# gpam.py - inspired by cute pammy from the office, now global !
# gpam is for functions that do not belong to a class, but still wanna print
# some stuff (verbose, error or logs). gpam provides some help to do that
# warning. high chances that gpam is desirable outside, but it is actually
# intended for internal use
# 
# @Author ToraNova
# @mailto chia_jason96@live.com
# @version 1.0
# @date 13 May 2019
################################################################################

################################################################################
# dependencies importation
################################################################################
import datetime, inspect
################################################################################
# local imports (import as if the library is a sys library)
from pyioneer.constant import ansicolor, constring
################################################################################

'''the general global printing assistant module (PAM) functions
may supply any amount of arguments, set df to the date format.
if df is not a string, then date printing is disabled'''

# Shared with Pam
def rprint(*args, **kwargs):
    '''raw print function, no dates included, just print rawly'''
    print(*args)

# Shared with Pam
def dprint(*args, df=constring.Dateformt.norm_micros, **kwargs):
    '''prints the date and the filename and func name of the caller function
    mainly for debugging purposes. use with debugprint()'''
    cstack = inspect.stack()
    cdetails = gpam_stackDetails( cstack )
    print(gpam_dateDetails(df),*args, cdetails)

# Shared with Pam
def vprint(*args,cs=ansicolor.Eseq.normtext,df=constring.Dateformt.norm_micros, **kwargs):
    '''prints the date information only. does not include caller and file and
    function name. suitable for verboses, change cs to other colors to enable 
    colored printing'''
    print(cs+gpam_dateDetails(df),*args,ansicolor.Eseq.normtext)

# Shared with Pam
def eprint(*args, df=constring.Dateformt.norm_micros, **kwargs):
    '''error printing function. this prints the text in red'''
    cstack = inspect.stack()
    cdetails = gpam_stackDetails( cstack )
    print(ansicolor.Eseq.defred+gpam_dateDetails(df),\
             *args, cdetails, ansicolor.Eseq.normtext)

# Shared with Pam
def wprint(*args, df=constring.Dateformt.norm_micros, **kwargs):
    '''warning printing function. this prints the text in yellow'''
    vprint( *args, cs=ansicolor.Eseq.defyel, df=df)

# Shared with Pam
def iprint(*args, df=constring.Dateformt.norm_micros, **kwargs):
    '''info print, this is printed as a different color to highlight details'''
    vprint( *args, cs=ansicolor.Eseq.defcya, df=df)

# Shared with Pam
def exprint(*args, df=constring.Dateformt.norm_micros, **kwargs):
    '''prints the args, but with prepended Exception has occurred'''
    cstack = inspect.stack()
    cdetails = gpam_stackDetails( cstack )
    print(ansicolor.Eseq.bolred+gpam_dateDetails(df),"Exception has occurred.",\
            *args, cdetails, ansicolor.Eseq.normtext)

################################################################################
# Default setups
################################################################################
error   = eprint
warn    = wprint
verbose = vprint
debug   = dprint
raw     = rprint
info    = iprint
expt    = exprint

################################################################################
# Macros
################################################################################
def gpam_dateDetails(sformat):
    #easy datetime macro
    return datetime.datetime.now().strftime(sformat)

def gpam_stackDetails( stack ):
    ind = 1
    module = inspect.getmodule(stack[ind])
    cfilename = stack[ind].filename
    cfuncname = stack[ind].function
    cfuncline = stack[ind].lineno
    sdetails = "file:{} func({}, line={})".format(cfilename,cfuncname,\
            cfuncline)
    return sdetails
    
################################################################################

def enable_gpam():
    # this enables the correct gpam function to be mapped
    global verbose
    global debug
    global raw
    global info
    verbose = vprint
    debug   = dprint
    raw     = rprint
    info    = iprint

def disable_gpam():
    # this disabled, gpam are now mapped to lambda nones
    # gpam_error cannot be disabled. We do not encourage hiding errors
    global verbose
    global debug
    global raw
    global info
    verbose = lambda *a: None
    debug   = lambda *a: None
    raw     = lambda *a: None
    info    = lambda *a: None

# Test script
if __name__ == "__main__":
    
    warn("Warning")
    error("to err is human")
    verbose("verbose is enabled by default")
    disable_gpam()
    verbose("silenced")
    debug("silenced x2")
    error("can't silence me")
    raw("raw test 1")
    enable_gpam()
    verbose("ok' we're back",df=constring.Dateformt.norm)
    raw("raw test 2")

