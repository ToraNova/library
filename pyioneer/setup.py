#!/usr/bin/python3

# This is the setup script for pyioneer
# allows the user to install pyioneer into
# the system library

from distutils.core import setup

# import package dependent vars
from pyioneer import __offname, __version, __modules 
from pyioneer import __author, __mailto, __description

setup(  
        name=__offname,
        version= __version,
        author=__author,
        author_email=__mailto,
        packages= __modules,
        description = __description
    )

