#!/usr/bin/python3
# Python setup script
# Originally made to create c/c++ wrapper libraries for python
# Made to wrap PLASMA linalg library

from distutils.core import setup, Extension

#module name
# TODO : Replace your wrapper libname here
modname = "pyplasma"
#module version
# TODO : Change the package details here
version = 1.0
author = "ToraNova"
author_email = "chia_jason96@live.com"
description = "Pyplasma C/C++ library wrapper"

# TODO : change the swig interface file based on what u wanna compile
swig_ifile = "pyplasma.i"

# specify the name of the extension and source files
# required to compile the extension
fixed_extname = "_"+modname # this shouldn't be changed

# TODO : specify the sources
srclist = [swig_ifile]
srclist.append("src/irr.c")
srclist.append("src/test.c")

ext_mod0 = Extension(fixed_extname, sources=srclist)

# compile the actual module
setup(name = modname,version=version,
        author = author,
        author_email = author_email,
        description = description,
        ext_modules=[ext_mod0])
