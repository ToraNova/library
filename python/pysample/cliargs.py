#!/usr/bin/python3

# Python ARGPARSE tutorial
# for command line based usages
# ToraNova 2019

import argparse

if __name__ == "__main__":
    #main sample code

    mp = argparse.ArgumentParser() #creates the argparser obj

    # define the arguments, types and defaults to expect
    # arguments without -- are NON optional
    # arugments with -- are optional, please set a default for them
    mp.add_argument("t_string", type=str, help="the string to repetitively print")
    mp.add_argument("-a","--t_amount", type=int, default=1, help="the amount of times to repeat")
    mp.add_argument("-n","--newline", action="store_true", default=False, help="print newlines")
    mp.add_argument("-v","--verbose", action="count", default=0, help="print some stats")

    # Parse the arguments
    args = mp.parse_args()

    if(args.verbose == 2):
        print("Beginning REPRINT")
    for i in range( args.t_amount ):
        print( args.t_string , end = '\n' if args.newline else '')

    if(args.verbose >= 1):
        print("Total characters printed :",len(args.t_string)*args.t_amount)
        if(args.verbose >= 2):
            print("Total times looped :",args.t_amount)
            print("Ending REPRINT")

    exit(0)



