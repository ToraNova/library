################################################################################
# datcontrol.py
# datcontrol.py is the base controller classes that stores it's variables in a 
# controlled manner
# This is to aid re-usability, reduce code sizes and improve maintainability
# 
# @Author ToraNova
# @mailto chia_jason96@live.com
# @version 1.1
# @date 14 May 2019
# @changelogs
# 1.0: introduced
# 1.1: renamed to datcontrol.py from data.py, resturctured the variable package
################################################################################

import csv
################################################################################
# local imports (import as if the library is a sys library)
from pyioneer.support import Pam
from pyioneer.support import lstools
from pyioneer.variable.sanitize import isList, isMatrix
################################################################################

class DictController(Pam):
    '''basic data controller class, stores data as a dictionary'''
    _default_ktype = str

    def __init__(self,verbose=False,debug=False,owarn=False):
        '''construct a data controller.'''
        super().__init__(verbose=verbose, debug=debug)
        # The primary data dictionary
        self._mp = {} #empty dictionary during initialization
        self.__lwarn = self.__isloaded_warning \
                if owarn else lambda *a:None

    def __keytype_error(self):
        self.error("dname must be of type or list of type :{}! Aborting unload.".format(\
                type(self._default_ktype)))

    def __isloaded_warning(self, dname, load=True ):
        '''remap-able warning function
        @load true - warn if loaded (overwriting ?)
        @load false - warn if unloaded (unloaded-gets ?)
        '''
        if( self.isLoaded(dname) and load ):
            self.warn(dname,"overwritten on load")
            return True #warning triggered
        if( not self.isLoaded(dname) and not load):
            self.warn(dname,"getting previously unloaded data")
            return True #warning triggered
        return False #warning not triggered

    def load(self,dname,dval):
        '''sets the dname index on the primary dict to dval,
        overrides without warning'''
        if( isList( dname, self._default_ktype ) and isList( dval ) ):
            if( len(dname) != len(dval) ):
                self.error("Unabled to load with list. dname and dval diff lengths!")
                return
            for i,d in enumerate(dname):
                self.load(d, dval[i])
        elif( isinstance( dname, self._default_ktype )):
            self.__lwarn(dname, load=True)
            self._mp[dname] = dval
        else:
            self.__keytype_error()

    def get(self,dname):
        '''obtains the data keyed by dname. this function is recursive when dname
        is a list of strs which will invoke the function to return a list of vals
        specified in the order of dname'''
        if( isList( dname, self._default_ktype)):
            out = []
            for d in dname:
                out.append( self.get(dname)) #recursion
            return out
        elif( isinstance(dname, self._default_ktype)):
            self.__lwarn(dname, load=False) # use isloaded with single label
            return self._mp.get(dname)
        else:
            self.__keytype_error()

    def getrows(self, rn, dname):
        '''obtains the ith element of dname if dname IS indeed a list. returns None
        otherwise and prints out an error'''
        if( isList( self.get(dname))):
            if( isList( rn )):
                out = []
                for d in rn:
                    out.append(self.getrows(d,dname)) #recursion
                return out
            elif( isinstance( rn, int)):
                if( self.isLoaded(dname) and rn >= len(self._mp[dname])):
                    self.error(rn,"is larger than length of",dname,":skip")
                else:
                    return self.get(dname)[rn]
            else:
                self.error("Error occurred on getrows() check:",rn)
                self.display(dname,showtype=True)
        else:
            self.error(dname,"does not have the structure of a list.")
        return None

    def getcols(self, rn, dname, pre_transposed=None):
        '''obtains the ith row of dname if dname IS indeed a matrix. returns None otherwise
        and prints out an error. The pre_tranposed is to speed up computation'''
        if( isMatrix( self.get(dname))):
            #proceed if true. else no point getting columns
            if( isList( rn)):
                out = []
                pre_transposed = lstools.transpose_2dlist( self.get(dname))
                if( pre_transposed is None):
                    self.error("Transposed failed. Aborting")
                    return None
                for d in rn:
                    out.append( self.getcols(d,dname,pre_transposed) )
                return out
            elif( isinstance(rn, int)):
                if( pre_transposed is None):
                    pre_transposed = lstools.transpose_2dlist( self.get(dname))
                if(rn >= len(pre_transposed[0])):
                    self.error(rn,"is larger than colsize of",dname,":skip")
                else:
                    return pre_transposed[rn]
            else:
                self.error("Error occurred on getcols() check:",rn)
                self.display(dname,showtype=True)
        else:
            self.error(dname,"does not have the structure of a matrix.")
        return None

    def size(self,dname):
        '''returns the size of dname if it is an array, or array of arrays
        if dname is not loaded, returns 0,0'''
        if( isList(dname, self._default_ktype)):
            out = []
            for d in dname:
                out.append( self.size(d)) #recursive
        elif( isinstance( dname, self._default_ktype)):
            if( isMatrix( self.get(dname) )):
                return len(self._mp[dname]),len(self._mp[dname][0])
            elif( isList( self.get(dname))):
                return len(self._mp[dname]),0
            else:
                return 0,0

    def unload(self,dname=None):
        '''unsets the dname index, the values are set back to None
        please use unload instead of doing something like self._mp[dname]=None
        because this allows the isLoaded to pass even if val is None'''
        if(dname is None):
            for v in self._mp.keys():
                del self._mp[v]
        elif( isList(dname, self._default_ktype ) ):
            for d in dname:
                self.unload(d) #recursion
        elif( isinstance(dname, self._default_ktype ) ):
            if( self.isLoaded( dname )):
                del self._mp[dname]
            else:
                self.warn(dname,
                        "attempting to unload an already unloaded value")
        else:
            self.__keytype_error()

    def display(self,dname=None,showtype=False,raw=False):
        '''display the contents of dname (simple printing)'''
        if(dname is None):
            #display all
            self.verbose("Displaying all contents")
            for v in self._mp.keys():
                self.display( v, raw = raw )
        elif( isList(dname,self._default_ktype) ):
            #display all as a list
            self.verbose("Displaying dnames:",dname)
            for v in dname:
                self.display( v, showtype=showtype, raw = raw ) #recursion
        elif( isinstance(dname, self._default_ktype) ):
            #display singular (this section is recursed)
            if(raw):
                self.raw(dname,
                    type(self.get(dname)) if showtype else '',
                    self.get(dname))
            else:
                self.verbose(dname, 
                    type(self.get(dname)) if showtype else '',
                    self.get(dname))
        else:
            self.__keytype_error()

    # check tests
    def isLoaded(self,dname):
        '''check if the DataController has loaded the data 'dname'
        returns False if dname is none in the primary dictionary
        also works if dname is a list, then checks if all element
        in the list is loaded, return false otherwise'''
        if( isList(dname,self._default_ktype)):
            flag = True
            for d in dname:
                if( self._mp.get(d) is None ):
                    self.warn(d,"not loaded by the datacontroller")
                    flag = False
            return flag
        else:
            return self._mp.get(dname) is not None #return true if it is not none

    def plug(self,target):
        '''allows external dicts to be loaded for the DC to control'''
        if(type(target) != dict):
            self.error("Can't plug a non-dict object to a DictController")
            return
        self._mp = target


# Test script
if __name__ == "__main__":

    dc = DictController(True,True,True)
    testmat = [[1,2,3],[4,5,6],[7,8,9]]
    testls = ['abc','def','dea']
    dc.load('m0',testmat)
    dc.load('l0',testls)
    dc.load('st','test string')
    dc.load('test','this is a test')
    dc.load('desc','this is a description')
    dc.load('desc','overwritten')
    dc.load(['t0','t1','t2'],[1,2,3])
    print(dc.isLoaded('desc'))
    print(dc.isLoaded( ['desc','test'] ))
    print(dc.size(['m0','l0']))
    print(dc.getrows(1,'m0'))
    print(dc.getcols(1,'m0'))
    print(dc.getrows([1,2],'l0'))
    dc.unload('test')
    print(dc.get('test'))
    dc.load('test','try again')
    print(dc.get('test'))
    dc.display('test') #same effect as above
    dc.display(['t0','t1','t2'])
    dc.display(['m0','l0'], raw = True, showtype=True)
    print("Test OK for",__file__)








