################################################################################
# ansicolor.py - a file to store constant color codings (especially for terms)
# ansicolor allows users to use ANSI escape sequences associated with
# some colors to enable colored printing on the terminal
# sourced from http://ozzmaker.com/add-colour-to-text-in-python/
# 
# @Author ToraNova
# @mailto chia_jason96@live.com
# @version 1.0
# @date 13 May 2019
################################################################################

''' 
A color sequence table
Foreground  Background
black 30    black 40
red   31    red 41
green 32    green 42
yellow 33   yellow 33
blue 34     blue 34
purple 35   purple 35
cyan 36     cyan 36
white 37    white 37

Text effects : 0-N/A, 1-Bold, 2-Underline, 3-Negative1, 4-Negative2
'''

class Eseq:

    normtext = "\033[m" # native color

    # bright color sequences
    # prepends these for color sequences
    defred = "\033[0;31m"        # bright red
    defgrn = "\033[0;32m"        # bright green
    defyel = "\033[0;33m"        # bright yellow
    defblu = "\033[0;34m"        # bright blue
    defmag = "\033[0;35m"        # bright magenta
    defcya = "\033[0;36m"        # bright cyan
    defwht = "\033[0;37m"        # use this to go back to normal text

    bolred = "\033[1;31m"        # bold red
    bolgrn = "\033[1;32m"        # bold green

    whtred = "\033[1;31;40m"    # pure red ?
    whtgrn = "\033[1;32;40m"    # pure green ?


# Test script
if __name__ == "__main__":
    
    # test colors
    print( Eseq.defred + "bright red" + Eseq.normtext )
    print( Eseq.defgrn + "bright grn" + Eseq.normtext )
    print( Eseq.defyel + "bright yel" + Eseq.normtext )
    print( Eseq.defblu + "bright blu" + Eseq.normtext )
    print( Eseq.defmag + "bright mag" + Eseq.normtext )
    print( Eseq.defcya + "bright_cya" + Eseq.normtext )
    print( Eseq.defwht + "weird" + Eseq.normtext )
    print( "Default text")

