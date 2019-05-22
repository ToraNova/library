################################################################################
# dictionary.py
# dictionary.py is a type of controller that stores it's variables in a dictionary
# This is to aid re-usability, reduce code sizes and improve maintainability
# 
# @Author ToraNova
# @mailto chia_jason96@live.com
# @version 1.1
# @date 14 May 2019
# @changelogs
# 1.0: introduced
# 1.1: renamed to dict_con.py from data.py, resturctured the variable package
################################################################################

import csv
################################################################################
# local imports (import as if the library is a sys library)
from pyioneer.support import Pam
from pyioneer.support import lstools
################################################################################

class DictController(Pam):
    '''basic data controller class'''

    def __init__(self,verbose=False,debug=False,owarn=False):
        '''construct a data controller.'''
        super().__init__(verbose=verbose, debug=debug)
        # The primary data dictionary
        self._mp = {} #empty dictionary during initialization
        self.__owarn = self.__overwrites_warning \
                if owarn else lambda *a:None

    def __overwrites_warning(self, dname ):
        '''remap-able warning function'''
        if( self.isLoaded(dname)):
            self.warn(dname,"overwritten onload")

    def load(self,dname,dval):
        '''sets the dname index on the primary dict to dval,
        overrides without warning'''
        self.__owarn(dname)
        self._mp[dname] = dval

    def unload(self,dname=None):
        '''unsets the dname index, the values are set back to None'''
        if(dname==None):
            for v in self._mp.keys():
                del self._mp[v]
        elif( type(dname) == list and len(dname) > 0):
            if( len(dname) == 1):
                del self._mp[dname[0]]
            else:
                for d in dname:
                    if( self.isLoaded(d) ):
                        del self._mp[d]
                    else:
                        self.warn(d,
                                "attempting to unload an already unloaded value")
        else:
            if( self.isLoaded( dname )):
                del self._mp[dname]
            else:
                self.warn(dname,
                        "attempting to unload an already unloaded value")

    def plug(self,target):
        '''allows external dicts to be loaded for the DC to control'''
        if(type(target) != dict):
            self.error("Can't plug a non-dict object to a DataController")
            return
        self._mp = target

    def display(self,dname=None,showtype=False,raw=False):
        '''display the contents of dname (simple printing)'''
        if(dname==None):
            #display all
            self.verbose("Displaying all contents")
            for v in self._mp.keys():
                self.display( v, raw = raw )
        elif( type(dname) == list and len(dname) > 0 ):
            #display all as a list
            self.verbose("Displaying dnames:",dname)
            for v in dname:
                self.display( v, raw = raw )
        else:
            #display singular (this section is recursed)
            if( self.isLoaded(dname) ):
                if(raw):
                    self.raw(dname,
                        type(self._mp[dname]) if showtype else '',
                        self._mp[dname])
                else:
                    self.verbose(dname, 
                        type(self._mp[dname]) if showtype else '',
                        self._mp[dname])
            else:
                self.warn(dname,"not loaded, cannot be displayed")

    # check tests
    def isLoaded(self,dname):
        '''check if the DataController has loaded the data 'dname'
        returns False if dname is none in the primary dictionary
        also works if dname is a list, then checks if all element
        in the list is loaded, return false otherwise'''
        if(type(dname) == list and len(dname) > 0):
            if(len(dname)==1):
                return dname[0] in self._mp
            else:
                flag = True
                for d in dname:
                    if(not d in self._mp ):
                        self.warn(d,"not loaded by the datacontroller")
                        flag = False
                return flag
        else:
            return dname in self._mp

    def get(self,dname):
        '''emulates a standard dictionary behaviour, except it
        prints out a warning if the data is not loaded'''
        if( not self.isLoaded(dname) ):
            self.warn("trying to read unloaded values",dname)
        return self._mp.get(dname)

# Test script
if __name__ == "__main__":

    dc = DictController(True,True,True)
    dc.load('desc','this is a datac')
    dc.load('desc','overwritten')
    dc.load('test','this is a test')
    dc.a = 1
    print(dc.isLoaded('desc'))
    print(dc.isLoaded( ['desc','test']))
    dc.unload(['desc','test'])
    print(dc.isLoaded( ['desc','test']))
    dc.load('var0',1)
    dc.load('var1',2)
    dc.display()
    dc.display('test')
    dc.display( ['var0','var1'] )
    print("Test OK for",__file__)








