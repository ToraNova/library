################################################################################
# sanitize.py
# sanitize.py is to define some standard sanitization functions to check for
# invalid or malicious inputs
# 
# @Author ToraNova
# @mailto chia_jason96@live.com
# @version 1.1
# @date 22 May 2019
# @changelogs
# 1.0: introduced
################################################################################

def isList( arg, argtype=None, minlen=1 ):
    '''check if arg is a list of type argtype. if argtype is none, then it allows anykind
    of lists (str,int,float) all OK. if argtype is str, then the list must be homogeneously
    string'''
    if not isinstance(arg,list):
        # first level check
        return False
    if argtype is not None:
        # second level check
        for a in arg:
            if not isinstance(a,argtype):
                return False
    return len(arg) > minlen

def isMatrix( arg, argtype=None, minrow=1, mincol=1):
    '''check if arg is a list of lists, that each row must have the same number of column
    it acts similarly like isList'''
    if not isList( arg, argtype, minrow):
        # first level check
        return False
    fnum = len( arg[0] )
    for r in arg:
        # second level
        if len(r) != fnum or isList(r,argtype,fnum):
            return False
    return fnum > mincol



    

