##################################################################
# The constant package provides constants
# it provides formats/ color sequesnces and/or other constants
# that is inconvenient to replicate too many times
#
# @Author ToraNova
# @mailto chia_jason96@live.com
# @version 1.0
# @date 13 May 2019
##################################################################

# bearing in mind inner classes from the modules such as
# Eseq, Dateformt are not packages, and so it's best if we they're
# imported as such (examples)
# import pyioneer.constant.ansicolor as ansicolor
# import pyioneer.constant.constring as constring
# One can also import Eseq directly, use
# import pyioneer.constant.ansicolor.Eseq as Eseq

from . import ansicolor
Eseq = ansicolor.Eseq

from . import constring
Dateformt = constring.Dateformt
