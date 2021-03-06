###############################################################################
# Project pyioneer 2019
# ToraNova chia_jason96@live.com
# This is the module's initializer
# current the packages are exported directly without the file's intervention
############################################################################## 

############################################################################## 
# METADATA
############################################################################## 
__author  = "ToraNova"
__mailto  = "chia_jason96@live.com"
__offname = "Pyioneer"
__version = "1.0"
__description = "Pyioneer is a library to support rapid python development"

############################################################################## 
# Module listings
############################################################################## 
__modules = [
        'pyioneer',
        'pyioneer.support',
        'pyioneer.constant',
        'pyioneer.variable',
        'pyioneer.variable.control',
        'pyioneer.variable.analytics',
        'pyioneer.network',
        'pyioneer.network.tcp'
        ]

############################################################################## 
# AUXILIARIES
############################################################################## 
def version():
    print(__offname,__version,__author)
############################################################################## 
