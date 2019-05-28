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
from pyioneer.support.pam import Pam
from pyioneer.variable import mutator
import random, math, csv

class DataGen(Pam):
    '''Class to generate series of data'''

    mutatelkup = {
            "simple":mutator.simple,
            "ranged":mutator.ranged,
            "scaled":mutator.scaled,
            "ranged_scaled":mutator.ranged_scaled
            }

    def __init__(self,t,mutation=None,positive=False,verbose=False,debug=False):
        # initialize a math class which will generate n
        # datapoints upon any method calls
        super().__init__(verbose=verbose,debug=debug)
        self.targets = t
        self.pos_set = positive

        if(mutation is not None):
            if( mutation in self.mutatelkup.keys()):
                self.debug("Using predefined mutation",mutation)
                self.mutate = self.mutatelkup[mutation]
            else:
                self.debug("Using custom mutation")
                self.mutate = mutation

    ###############################################################
    # Feed in methods
    ###############################################################
    def setup_rules(self,r):
        '''feed in the rule list for to allow generation later''' 
        self.rules = r

    def pumpin(self, data_src):
        '''pumpin external values (for sklearn built-in dset dumps'''
        self.md = data_src

    ###############################################################
    # internal manipulation
    ###############################################################
    def transpose_md(self):
        '''transpose the internal matrix'''
        #python3 solution
        self.md = list(map(list, zip(*self.md)))
        #other pythonic solution (2)
        #map(list,zip(*self.md))

    def generate(self,rule=None,shuffle=False):
        '''generates the dataset based on the rules and the true values
        the shuffle arg if set to true will shuffle the entire dataset
        post generation'''
        self.md = []
        for t in self.targets:
            trow = []
            for r in self.rules:
                self.debug("Calling",str(r[0]),"with",str(t),str(r[1]))
                trow.append( r[0](t,r[1]) )
            trow.append(t)
            self.debug(trow)
            self.md.append(trow)
        if(shuffle):
            random.shuffle(self.md)

    ###############################################################
    # Output methods
    ###############################################################
    def sample(self,n=5):
        '''returns N samples from the randomly generated set'''
        if(n > len(self.md)):
            self.error("N is larger than size of generated data!")
            return None
        self.verbose("Selecting",n,"samples")
        tmp = random.shuffle(self.md)[0:n]
        for t in tmp:
            self.raw(t)
        return tmp

    def dispmd(self,n=5):
        '''display first n rows of md'''
        if(n > len(self.md)):
            self.error("N is larger than size of generated data!")
            return None
        self.verbose("First",n,"data in md")
        for i in range(n):
            self.raw(i,":", self.md[i] )

    def write_dataset(self,filename,write_headers=True,write_index=True,
            delim=',',quotechar='"',csvquoting=csv.QUOTE_MINIMAL):
        '''writes the dataset onto a csv file, set write_headers to
        true to write the header.'''
        # writes the dataset onto a file
        with open(filename,'w') as outfile:
            csv_writer = csv.writer(outfile,
                        delimiter=delim,quotechar=quotechar,
                        quoting=csvquoting)
            if(write_headers):
                hdr = []
                if(write_index):
                    hdr.append("Index")
                for i in range( len(self.md[0]) ):
                    hdr.append( 'C'+str(i+1) )
                csv_writer.writerow(hdr)
            for i,rows in enumerate(self.md):
                if(write_index):
                    rows = [i] + rows
                csv_writer.writerow( rows )

    def vsplit_write(self,filename,split_point=0,write_target_1=True,
            delim=',',quotechar='"',csvquoting=csv.QUOTE_MINIMAL):
        '''splits the dataset vertically, then write to file
        both file's final column is the target
        set write target 1 to false if do not want the first
        set to have the target appended on the last column'''
        with open(filename+'1','w') as outfile:
            csv_writer = csv.writer(outfile,
                        delimiter=delim,quotechar=quotechar,
                        quoting=csvquoting)
            for i,rows in enumerate(self.md):
                rows = rows[:split_point]
                if(write_target_1):
                    #append the target onto file1
                    rows.append(self.targets[i])
                csv_writer.writerow( rows )

        with open(filename+'2','w') as outfile:
            csv_writer = csv.writer(outfile,
                        delimiter=self.delim,quotechar=self.quotechar,
                        quoting=self.csvquoting)
            for i,rows in enumerate(self.md):
                csv_writer.writerow( rows[split_point:] )

    ###############################################################
    # Data generators
    ###############################################################
    def linear(self,xin,arglist):
        # arglist m=1,c=0,p=0,d=0
        # generates the linear output based on xin,m and c
        m = arglist[0] # gradient
        c = arglist[1] # constant
        p = arglist[2] # probability of mutation
        d = arglist[3] # magnitude of mutation

        out = xin*m + c
        out += self.mutate(p,d,xin)
        return out if not self.pos_set else abs(out)

    def expo(self,xin, arglist):
        k = arglist[0] # e^(xk) -- k
        c = arglist[1] # the constant 
        p = arglist[2] # probability to mutate
        d = arglist[3] # magnitude of mutation
        # generates the exponential output based on xin,m,c
        out = math.exp(xin*k) + c + self.mutate(p,d,xin)
        return out if not self.pos_set else abs(out)

    def constant(self,xin,arglist):
        c = arglist[0] # constant
        p = arglist[1] # probability to mutate
        d = arglist[2] # magnitude of mutation
        # generates a constant
        out = c + self.mutate(p,d,xin)
        return out if not self.pos_set else abs(out)

    def random_int(self,xin,arglist):
        s = arglist[0] # start
        e = arglist[1] # end
        # generates the linear obj
        out = random.randint(s,e)
        return out if not self.pos_set else abs(out)

if __name__ == "__main__":

    rsize = 15
    t = [i+198+mutator.ranged(0.3,194,i) for i in range(rsize)] # these are the true targets
    gen = DataGen(t,"ranged_scaled",positive=True,verbose=True)

    rules = [
            (gen.linear,[1,0,0.6,12]),
            (gen.random_int,[0,3]),
            (gen.constant,[4,0.2,2]),
            (gen.constant,[2,0.3,1]),
            (gen.random_int,[4,30]),
            (gen.expo,[0.03,1,0.2,3]),
            (gen.constant,[-1,0.1,2]),
            (gen.constant,[103,0.9,40]),
            (gen.constant,[34,0.863,14]),
            (gen.random_int,[77,267]),
            (gen.random_int,[0,1])
    ]

    gen.setup_rules(rules)
    gen.generate(False)
    gen.dispmd(5)
    print("Test OK for",__file__)

