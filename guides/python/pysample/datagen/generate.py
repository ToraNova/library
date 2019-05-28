# this is a script to generate a datasets based on functions
from pyioneer.variable import DataGen
from pyioneer.variable import mutator
import argparse

if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument("outfile", type=str, help="Output file name")
    ap.add_argument("--number","-n", type=int,default=1000,help="Number of lines to generate")
    ap.add_argument("--split","-l",type=int,help="Split the generated data")
    ap.add_argument("--transpose","-t",action="store_true", help="Transpose the generated data (used right before writing)")
    ap.add_argument("--shuffle","-s", action="store_true" ,help="Shuffle the data")
    ap.add_argument("--verbose","-v",action="count",help="Verbosity (1: show 5 samples; 2: show debugs)")
    ap.add_argument("--abs","-p",action="store_true", help="Only positive value generated")
    ap.add_argument("--mutator","-m",type=str,default="ranged",help="Used the mutator (simple,ranged,scaled,ranged_scaled")
    ap.add_argument("--header_skip","-a",action="store_true",help="Skip writing header")
    ap.add_argument("--wtar1","-w",action="store_true",help="Write target on 1 (split only)")
    ap.add_argument("--wind","-i",action="store_true",help="Write index on outfile (non split only)")
    args = ap.parse_args()

    #create 0-19 target vals
    t = [i+198+mutator.ranged(0.3,194,i) for i in range(args.number)] # these are the true targets
    gen = DataGen(t, args.mutator ,positive=args.abs,debug=args.verbose==2,verbose=args.verbose ==1)

    rules = [
            (gen.linear,[1,0,0.6,12]),
            (gen.random_int,[0,3]),
            (gen.constant,[4,0.2,2]),
            (gen.constant,[2,0.3,1]),
            (gen.random_int,[4,30]),
            (gen.expo,[0.03,1,0.2,3]),
            (gen.random_int,[0,1]),
            (gen.constant,[-1,0.1,2]),
            (gen.constant,[103,0.9,40]),
            (gen.constant,[34,0.863,14]),
            (gen.random_int,[77,267]),
            (gen.random_int,[0,1])
    ]

    gen.setup_rules(rules)
    gen.generate(args.shuffle)
    if(args.verbose is not None and args.verbose>=1):
        gen.dispmd()

    #transpose the data
    #gen.transpose_md()
    if( args.split is None):
        gen.write_dataset(args.outfile, write_headers = not args.header_skip , write_index=args.wind)
    else:
        gen.vsplit_write( args.outfile,split_point=args.split,write_target_1=args.wtar1)
