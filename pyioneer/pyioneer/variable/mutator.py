################################################################################
# mutator.py
# mutator.py provides some data mutation capabilities to introduce noise
# into a dataset
# 
# @Author ToraNova
# @mailto chia_jason96@live.com
# @version 1.0
# @date 28 May 2019
# @changelogs
# 1.0: introduced
################################################################################
from pyioneer.support.gpam import getgpam
from collections import namedtuple
import random

MutatorGPAM = getgpam()
class MutatorRule:
    '''This class is to control the mutations of the function here.
    they are armed with the function that will trigger upon a certain
    probability factor'''

    def __init__(self , p_mutate, p_positive=0.5):
        # chk okay
        chklist = [
                isinstance( p_mutate, float) or isinstance( p_mutate,int),
                isinstance( p_positive, float) or isinstance( p_positive,int)
                ]
        if( all(chklist) ):
            self.p_mutate = p_mutate
            self.p_positive = p_positive
            self.bi_activate = self.__bi_activate
        else:
            MutatorGPAM.error("Rule params invalid! p_mutate,p_positive",chklist)
            self.bi_activate = lambda *args: None

    def __bi_activate(self, func, *args):
        '''activate the mutator bidirectionally (positive and negative)'''
        roll = random.uniform(0,1) #check if we want to mutate or not
        if( roll <= self.p_mutate ):
            #yes
            roll = random.uniform(0,1)
            if(roll <= self.p_positive ):
                #mutate positively
                return func(*args) 
            else:
                #mutate negatively
                return func(*args)
        else:
            #no
            return 0

###############################################################
# Mutators
###############################################################
def simple(p,d,x):
    '''p chance to return +d or -d. (integer)
    @dummy - x'''
    f = lambda d:d
    m = MutatorRule(p)
    return m.bi_activate(f, d)

def ranged(p,d,x):
    '''p changed to mutate not more than +- abs 0->d
    returns integer @dummy - x'''
    f = lambda d: random.randint(0,d)
    m = MutatorRule(p)
    return m.bi_activate( f,d)

def scaled(p,d,x):
    '''random p chance to mutate d percentage of x'''
    f = lambda d,x: d*x 
    m = MutatorRule(p)
    return m.bi_activate( f, d, x)

def ranged_scaled(p,d,x):
    '''random p chance to mutate __upto__ d percentage of x'''
    f = lambda d,x: random.uniform(0,d)*x
    m = MutatorRule(p)
    return m.bi_activate( f, d, x)

if __name__ == "__main__":
    
    print("Testing Simple Mutations")
    print( simple( 'a', 5, 0 ) )
    print( simple( 0.6, 5, 0) )
    print( simple( 0.6, 5, 0) )
    print( simple( 0.4, 5, 0) )
    print( simple( 0.4, 5, 0 ) )
    
    print("Testing Ranged Mutations")
    print( ranged( 0.6, 5, 0) )
    print( ranged( 0.6, 5, 0) )
    print( ranged( 0.6, 5, 0) )
    print( ranged( 0.4, 5, 0) )
    print( ranged( 0.4, 5, 0) )

    print("Testing Scaled Mutations")
    print( scaled( 0.6, 0.2,1 ) )
    print( scaled( 0.6, 0.2,2 ) )
    print( scaled( 0.6, 0.2,3 ) )
    print( scaled( 0.4, 0.3,4 ) )
    print( scaled( 0.4, 0.3,5 ) )

    print("Testing Ranged Scaled Mutations")
    print( ranged_scaled( 0.6, 0.2,1 ) )
    print( ranged_scaled( 0.6, 0.2,2 ) )
    print( ranged_scaled( 0.6, 0.2,3 ) )
    print( ranged_scaled( 0.4, 0.3,4 ) )
    print( ranged_scaled( 0.4, 0.3,5 ) )
    print("Test OK for",__file__)
