################################################################################
# data.py
# the controller class controls data preprocessing, aids re-usability
# to reduce code sizes on the class codes that has tonnes of variables,
# definition and improve maintainability
# 
# @Author ToraNova
# @mailto chia_jason96@live.com
# @version 1.0
# @date 14 May 2019
################################################################################

import csv
################################################################################
# local imports (import as if the library is a sys library)
from pyioneer.support import Pam
from pyioneer.support import lstools
################################################################################

class DataController(Pam):
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
            self.warning("trying to read unloaded values",dname)
        return self._mp.get(dname)

class HomoCSVDataController(DataController):
    '''csv based data controller, reads and loads csv files, assumes csv file is homogenous
    that is all a single data type (naive)''' 
    _default_readkey = "__csv"

    def __init__(self,verbose=False,debug=False,owarn=False):
        '''constructs the HomoCSVDC obj.
        @verbose and debug. print verbose and debug'''
        super().__init__(verbose=verbose,debug=debug,owarn=owarn)

    def read(self,filename, htype=float, dname=_default_readkey,
            skipc = 0, adelimiter=';', aquotechar ='"'):
        '''
        @filename, name of the CSV file,
        @htype the datatype of the homogenous csv file
        @dname which dictionary index is used to store the read data
        @skipc number of lines to skip, use 1 to skip the usual headers
        @adelimiter and aquotechar delimiter and quotechar char
        '''
        try:
            with open(filename) as dataset:
                self._mp[dname] = []
                reader = csv.reader(dataset, delimiter=adelimiter, quotechar=aquotechar)
                #skips over( headers or unwanted first few rows)
                for index in range(skipc):
                    next(reader)
                rin_list = list(reader) #read in the csv file
                if(len(rin_list) <= 0):
                    self.error("reading 0 rows, aborting.")
                    del self._mp[dname]
                else:
                    for index,row in enumerate(rin_list):
                        self._mp[dname].append( [htype(i) for i in row] )
        except Exception as e:
            self.expt(str(e))
            self.unload(dname)

    def isRead(self,dname=_default_readkey):
        '''checks if reading is successfuly conducted on the default key'''
        return self.isLoaded(dname)

    def showcase(self,dname=_default_readkey):
        '''prints out what the CSV reader has read from the default key'''
        self.display(dname)

    def size(self,dname=_default_readkey):
        '''returns a tuple of the row,col size of the read in csvfile'''
        if( self.isRead( dname) ):
            return len(self._mp[dname]),len(self._mp[dname][0])
        else:
            return 0,0


# Test script
if __name__ == "__main__":

    dc = DataController(True,True,True)
    hc = HomoCSVDataController(True,True,True)
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
    hc.load('desc','this is a homocsvdatac')
    hc.load('test','this is a test2')

    dc.display()
    dc.display('test')

    hc.read( "/home/cjason/library/guides/python/pysample/datagen/data0.csv", float)

    print( hc.isRead())
    print( hc.size()[0])
    dc.display( ['var0','var1'] )
    hc.display( ['test'] )

    print("Test OK for",__file__)








