################################################################################
# gpam.py - inspired by cute pammy from the office, now global !
# gpam is for functions that do not belong to a class, but still wanna print
# some stuff (verbose, error or logs). gpam provides some help to do that
# warning. high chances that gpam is desirable outside, but it is actually
# intended for internal use
# 
# @Author ToraNova
# @mailto chia_jason96@live.com
# @version 1.1
# @date 13 May 2019
# @changelogs
# 1.0 : introduced
# 1.1 : added getgpam, removed __enable and other intermodule useless crap
################################################################################

################################################################################
# dependencies importation
################################################################################
import datetime, inspect, sys
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
    cdetails = __stackDetails( cstack )
    print(__dateDetails(df),*args, cdetails)

# Shared with Pam
def vprint(*args,cs=ansicolor.Eseq.normtext,df=constring.Dateformt.norm_micros, **kwargs):
    '''prints the date information only. does not include caller and file and
    function name. suitable for verboses, change cs to other colors to enable 
    colored printing'''
    print(cs+__dateDetails(df),*args,ansicolor.Eseq.normtext)

# Shared with Pam
def eprint(*args, df=constring.Dateformt.norm_micros, **kwargs):
    '''error printing function. this prints the text in red'''
    cstack = inspect.stack()
    cdetails = __stackDetails( cstack )
    print(ansicolor.Eseq.defred+__dateDetails(df),\
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
    cdetails = __stackDetails( cstack )
    print(ansicolor.Eseq.bolred+__dateDetails(df),"Exception has occurred.",\
            *args, cdetails, ansicolor.Eseq.normtext)

def nothing(*args, **kwargs):
    '''place holder to do nothing
    alt: lambda *a, **kw : None
    currently not used
    '''
    return None

################################################################################
# Macros
################################################################################
def __dateDetails(sformat):
    #easy datetime macro
    return datetime.datetime.now().strftime(sformat)

def __stackDetails( stack ):
    #format the printing of info of caller function
    ind = 1
    module = inspect.getmodule(stack[ind])
    cfilename = stack[ind].filename
    cfuncname = stack[ind].function
    cfuncline = stack[ind].lineno
    sdetails = "file:{} func({}, line={})".format(cfilename,cfuncname,\
            cfuncline)
    return sdetails
    
################################################################################

# Update 1.1 : Please do not use gpam directly. Please use the export object gpam instead.
# This is so thtat the object can be turned off at will.
# Use getgpam if you wanna use pam, but you are not on the Object Oriented model.

def getgpam( everbose=True, edebug=True, eerror=True, ewarn=True, einfo=True, eraw=True ):
    '''obtain a gpam object that can be controlled easily. This is for users who want to use
    pam but has no objects or is too lazy to create a pam object theirselves. The gpam obj
    can be turned on and off like a pam object (it's just a glorified pam object)

    @example use :
    from pyioneer.support.gpam import getgpam
    pam = getgpam()
    pam.verbose("foobar!")
    pam.quiet()
    pam.verbose("shhh")
    pam.warn("i'm still here")
    pam.verboseonly()
    pam.verbose("ok let's talk")
    '''

    # This is dangerous, do not mess up the imports here as it will likely lead to circular
    # import ( Since PAM depends on GPAM. and now this function is IN GPAM )
    # Justification: the original intent of gpam is to allow global printing with no hassle of
    # oo methods. Thus it is befitting that this function is on gpam
    from pyioneer.support.pam import Pam
    # Creates the Pam object (ironic how Pam depends on GPAM, now they're intertwined
    out_gpam = Pam( everbose, edebug, eerror, ewarn, einfo, eraw )
    # Exports/allow users to obtain the object
    return out_gpam

# Test script
# If you only use gpam without
if __name__ == "__main__":
    
    vprint("verbose")
    wprint("warning")
    eprint("error")
    iprint("info",df=constring.Dateformt.norm)
    rprint("raw")
    dprint("debug")
    exprint("exceptions")
    print("Test OK for",__file__)


