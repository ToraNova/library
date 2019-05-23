################################################################################
# csvcontrol.py
# csvcontrol is a subclass of the controller which handles csv files. it comes
# with some on board functionalities such as build and uses analytics from the
# analytic subpackage to perform statistical analysis on the data that it has
# loaded
# 
# @Author ToraNova
# @mailto chia_jason96@live.com
# @version 1.1
# @date 14 May 2019
# @changelogs
# 1.0 : introduced
# 1.1 : renamed to csvcontrol from previously data.py
#       implemented CSVController, HomoCSVController and declares HeteCSVController
################################################################################

import csv
################################################################################
# local imports (import as if the library is a sys library)
from pyioneer.support import Pam, lstools
from pyioneer.variable.control import DictController
from pyioneer.variable.sanitize import isList
from pyioneer.variable.analytics import Statsmachine
################################################################################

class CSVController(DictController):
    '''csv based data controller, reads and loads csv files literally and store the fields
    as strings. no attempts to type cast it. This is a very pure class, please use to implement
    something more specific like HomoCSVController which treats all variables as the same type
    and attempts to typecast it'''
    _default_readkey = "__csv"

    def __init__(self,verbose=False,debug=False,owarn=False):
        '''construct the CSVC obj.'''
        super().__init__(verbose=verbose,debug=debug,owarn=owarn)

    def read(self,filename, dname=_default_readkey, skipc=0, adelimiter=';', aquotechar ="\""):
        '''
        @filename, name of the CSV file,
        @dname which dictionary index is used to store the read data
        @skipc number of lines to skip, use 1 to skip the usual headers
        @adelimiter and @aquotechar delimiter and quotechar char
        '''
        try:
            with open(filename) as dataset:
                reader = csv.reader(dataset, delimiter=adelimiter, quotechar=aquotechar)
                #skips over( headers or unwanted first few rows)
                for index in range(skipc):
                    next(reader)
                rin_list = list(reader) #read in the csv file
                if(len(rin_list) <= 0):
                    self.error("Reading 0 rows, aborting.")
                    del self._mp[dname]
                else:
                    self.verbose("Reading {} rows.".format(len(rin_list)))
                    self.load(dname, rin_list)
        except Exception as e:
            # forces the read operation to be atomic. either it succeed or fail
            self.expt(str(e))
            self.unload(dname)

    def findEmpty(self, dname=_default_readkey):
        '''finds the rows in dname which has fields that has str of length 0,
        returns the row number and colnum in a list
        one can use it with getrows:
        missing = findEmpty()
        misrows = getrows( [ m[0] for m in missing])
        '''
        sz = self.size(dname)
        rows = self.getrows([i for i in range(sz[0])] , dname)
        outlist = []
        for rdx,r in enumerate(rows):
            for kdx,k in enumerate(r):
                if len(k) <= 0:
                    outlist.append( (rdx,kdx) )
        return outlist

    def isRead(self,dname=_default_readkey):
        '''checks if reading is successfuly conducted on the default key'''
        return self.isLoaded(dname)

    def showcase(self,dname=_default_readkey):
        '''prints out what the CSV reader has read from the default key'''
        sz = self.size(dname)
        self.verbose("Size of dname:",sz)
        rows = self.getrows([i for i in range(sz[0])] , dname)
        for r in rows:
            self.raw(r)

    def dsummary(self, dname=_default_readkey):
        # obtain a summary on all columns
        sz = self.size(dname)
        cols = self.getcols( [i for i in range(sz[1])] , dname)
        out = [ Statsmachine(c) for c in cols ]
        return out

    def getrows( self, rn , dname=_default_readkey):
        '''obtains the rows'''
        return super().getrows( rn, dname)

    def getcols( self, rn, dname=_default_readkey, pre_transposed=None):
        '''obtains the column'''
        return super().getcols( rn ,dname, pre_transposed)

    def size(self,dname=_default_readkey):
        '''returns a tuple of the row,col size of the read in csvfile'''
        return super().size(dname)

class HomoCSVController(CSVController):
    '''csv based data controller, reads and loads csv files, assumes csv file is homogenous
    that is all a single data type (naive)''' 

    def __init__(self,verbose=False,debug=False,owarn=False):
        '''constructs the HomoCSVC obj.
        @verbose and debug. print verbose and debug'''
        super().__init__(verbose=verbose,debug=debug,owarn=owarn)

    def typecast(self, typearg = float, dname=CSVController._default_readkey):
        '''attempts to typecast the read elements into a homogenous arrays of array,
        assumes all data type are the same 
        @typearg - the type of python types to cast the fields onto
        @dname - the data lookup to use'''
        if(not self.isRead(dname)):
            self.error("Unable to perform typecasting. CSV not read.")
            return
        fallback = self._mp[dname]
        for idx,row in enumerate(self._mp[dname]):
            try:
                self._mp[dname][idx] = [ typearg(i) for i in row ]
            except Exception as e:
                self.expt("Error typecasting",row,str(e))
                self._mp[dname] = fallback
                return

class HeteCSVController(CSVController):
    '''csv based data controller, reads and loads csv files, assumes csv file is heterogenous
    that and does not attempt to convert them to python types (yet)''' 

    def __init__(self,verbose=False,debug=False,owarn=False):
        '''constructs the HomoCSVC obj.
        @verbose and debug. print verbose and debug'''
        super().__init__(verbose=verbose,debug=debug,owarn=owarn)

    def typecast(self, arglist, dname = CSVController._default_readkey):
        pass

    def fieldsub(self, lksub, dname = CSVController._default_readkey):
        pass

# Test script
if __name__ == "__main__":

    cc = CSVController(True,True,True)
    cc.read("/home/cjason/library/guides/python/pysample/datagen/data0.csv")
    cc.showcase()
    print()
    cc.dsummary()
    print()
    print( cc.getrows( [0,2] ) )
    print( cc.getcols( 2 ) )

    hc = HomoCSVController(True,True,True)
    hc.read( "/home/cjason/library/guides/python/pysample/datagen/data0.csv")
    hc.typecast(float)
    hc.showcase()
    print()
    print( hc.getrows( [0,1] ) )
    print( hc.getcols( 1 ) )

    print("Test OK for",__file__)








