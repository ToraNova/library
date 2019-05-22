##################################################################
# The control subpackage provides analytics of variables 
#
# @Author ToraNova
# @mailto chia_jason96@live.com
# @version 1.0
# @date 14 May 2019
##################################################################

# for non class functions, please refrain from re-exporting
# only perform re-export if they are classes to prevent something like
# import pyioneer.suppoer.pam.Pam which looks bad
from . import stats
Statsmachine = stats.Statsmachine
