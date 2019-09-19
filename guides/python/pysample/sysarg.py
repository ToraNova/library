#!/usr/bin/python3

# reads in system arguments with the sys module
# not using argparse to make the script faster

import sys

if __name__ == "__main__":

    print(sys.argv)

    if( len(sys.argv) > 0 ):
        print(sys.argv[0])
