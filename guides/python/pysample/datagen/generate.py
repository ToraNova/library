# this is a script to generate a datasets based on functions
import random
import math
import csv
import sys
class DataGenMath():
        # simple math class

        def __init__(self,t,mutation="simple",positive=False):
                # initialize a math class which will generate n
                # datapoints upon any method calls
                self.targets = t
                self.pos_set = positive

                self.delim = ';'
                self.quotechar = '"'
                self.csvquoting = csv.QUOTE_MINIMAL

                if(mutation=="ranged"):
                        # set the class to run ranged mutation
                        self.mutate = self.ranged_mutate
                else:
                        # simple mutation
                        self.mutate = self.simple_mutate

        def setup_rules(self,r):
                self.rules = r

        def transpose_md(self):
                #python3 solution
                self.md = list(map(list, zip(*self.md)))
                #other pythonic solution (2)
                #map(list,zip(*self.md))

        def generate(self,shuffle=False):
                # generates the dataset based on the rules and the true values
                # the shuffle arg if set to true will shuffle the entire dataset
                # post generation
                self.md = []
                for t in self.targets:
                        trow = []
                        for r in self.rules:
                                #print("Calling",str(r[0]),"with",str(t),str(r[1]))
                                trow.append( r[0](t,r[1]) )
                        trow.append(t)
                        print(trow)
                        self.md.append(trow)
                #print(self.md)
                if(shuffle):
                        random.shuffle(self.md)

        def pumpin(self, data_src):
                # feeds into self.md using data_src
                # useful to load sklearn datasets or other
                # prebuilt datasets
                self.md = data_src

        def write_dataset(self,filename):
                # writes the dataset onto a file
                with open(filename,'w') as outfile:
                        csv_writer = csv.writer(outfile,
                                        delimiter=self.delim,quotechar=self.quotechar,
                                        quoting=self.csvquoting)
                        for i,rows in enumerate(self.md):
                                csv_writer.writerow( rows )

        def vsplit_write(self,filename,split_point=0,write_target_1=True):
                # splits the dataset vertically, then write to file
                # both file's final column is the target
                # set write target 1 to false if do not want the first
                # set to have the target appended on the last column
                with open(filename+'1','w') as outfile:
                        csv_writer = csv.writer(outfile,
                                        delimiter=self.delim,quotechar=self.quotechar,
                                        quoting=self.csvquoting)
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

        # DATA GENERATION FUNCTIONS
        def linear(self,xin,*args):
                ia = args[0]
                # arglist m=1,c=0,p=0,d=0
                # generates the linear output based on xin,m and c
                m = ia[0]
                c = ia[1]
                p = ia[2]
                d = ia[3]

                out = xin*m + c
                out += self.mutate(p,d)
                return out if not self.pos_set else abs(out)

        def expo(self,xin, *args):
                ia = args[0]
                k = ia[0]
                c = ia[1]
                p = ia[2]
                d = ia[3]
                # generates the exponential output based on xin,m,c
                out = math.exp(xin*k) + c + self.mutate(p,d)
                return out if not self.pos_set else abs(out)

        def constant(self,xin,*args):
                ia = args[0]
                c = ia[0]
                p = ia[1]
                d = ia[2]
                # generates a constant
                out = c + self.mutate(p,d)
                return out if not self.pos_set else abs(out)

        def random_int(self,xin,*args):
                ia = args[0]
                s = ia[0]
                e = ia[1]
                # generates the linear obj
                return random.randint(s,e)

        def simple_mutate(self,p,d):
                # p chance return +d or -d
                # integer
                roll = random.uniform(0,1)
                out = 0
                if(roll <= p):
                        roll = random.uniform(0,1)
                        if(roll > 0.5):
                                out += d
                        else:
                                out -= d
                return out

        def ranged_mutate(self,p,d):
                # p chance to return not more than +- abs 0-d
                # integer
                roll = random.uniform(0,1)
                out = 0
                if(roll <= p):
                        roll = random.uniform(0,1)
                        if(roll > 0.5):
                                out+= random.randint(0,d)
                        else:
                                out-= random.randint(0,d)
                return out

if __name__ == "__main__":

        if( len(sys.argv) < 2):
            print("Record length unspecified, using default 1000");
            rsize = 1000
        else:
            try:
                rsize = int(sys.argv[1])
            except Exception as e:
                print("Error parsing string",sys,argv[1],str(e))
                rsize = 1000

        #create 0-19 target vals
        t = [i for i in range(rsize)] # these are the true targets

        gen = DataGenMath(t,"ranged",positive=True)

        # rules = [
        #       (gen.linear,[1,-3,0.5,1]),
        #       (gen.random_int,[0,3]),
        #       (gen.constant,[4,0.2,2]),
        #       (gen.constant,[2,0.3,1]),
        #       (gen.expo,[0.03,1,0.2,3]),
        #       (gen.constant,[-1,0.1,2])
        # ]

        rules = [
                (gen.linear,[1,0,0.5,1]),
                (gen.random_int,[0,3]),
                (gen.constant,[4,0.2,2]),
                (gen.constant,[2,0.3,1]),
                (gen.expo,[0.03,1,0.2,3]),
                (gen.linear,[-1,100,0.3,2]),
                (gen.constant,[-1,0.1,2])
        ]

        #rules = [
        #        (gen.linear,[1,0,0.5,1]),
        #        (gen.random_int,[0,3]),
        #        (gen.constant,[4,0.2,3])
        #        ]

        gen.setup_rules(rules)
        gen.generate(False)

        #transpose the data
        #gen.transpose_md()

        gen.write_dataset("sample_10k.csv")
        #gen.vsplit_write("data1.csv",split_point=3,write_target_1=False)
