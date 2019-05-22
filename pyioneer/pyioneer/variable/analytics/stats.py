################################################################################
# stats.py
# stats.py is the module that provides functionality for list/sets and other
# variable type analysis
# 
# @Author ToraNova
# @mailto chia_jason96@live.com
# @version 1.1
# @date 22 May 2019
# @changelogs
# 1.0: introduced
################################################################################

from pyioneer.support import Pam
from collections import namedtuple, Counter

class Statsmachine(Pam):

    def __init__(self,target,verbose=True,raw=True,debug=False):
        # construct the stats machine
        super().__init__(verbose=verbose,debug=debug)
        self.mc = Counter(target)
        self.ms = set(target)

    def getMostFrequent(self,n=3,vprint=False):
        '''gets the nth most frequent things, returns a dict of it'''
        out = self.mc.most_common(n)
        self.verbose("Most frequent n={}".format(n))
        if(vprint):
            for i in out:
                self.raw(i)
        else:
            self.raw(out)
        return out

    def getLeastFrequent(self,n=3,vprint=False):
        '''gets the nth least frequent things, returns a dict of it'''
        out = self.mc.most_common(n)[:-n:-1]
        self.verbose("Least frequent n={}".format(n))
        if(vprint):
            for i in out:
                self.raw(i)
        else:
            self.raw(out)
        return out

    def getUnique(self,vprint=False):
        '''gets the unique var in the target, returns a list of it'''
        out = self.ms
        self.verbose("Unique values :",len(out))
        if(vprint):
            for i in out:
                self.raw(i)
        else:
            self.raw(out)
        return list(out)

    def getCounts(self,vprint=False):
        '''returns the counter obj'''
        self.verbose("Occurrence count:")
        if(vprint):
            for k,i in self.mc.items():
                self.raw(k,i)
        else:
            self.raw(self.mc)
        return self.mc
