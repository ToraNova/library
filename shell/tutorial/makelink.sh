#!/bin/bash

#creates a symbolic link to the desktop location on the windows installation
#ensure that it is mounted first !

#ln -r --symbolic -T /media/cjason/OS_Install/Users/chia_/Desktop desktop.link -f 
#ln -r --symbolic -T /media/cjason/OS_Install/Linux windows-linux-ext.link -f
#ln -r --symbolic -T /media/cjason/OS_Install OS_Install.link -f

ln -r --symbolic -T /media/cjason/Windows10/Users/chia_/Desktop desktop.link -f

ln -r --symbolic -T /media/cjason/Persistence/MMU/Academia academia.link -f
ln -r --symbolic -T /media/cjason/Persistence/Personal personal.link -f
ln -r --symbolic -T /media/cjason/Persistence/MMU MMU.link -f

ln -r --symbolic -T /media/cjason/Auxiliary/virtualbox-machines vm.link -f
ln -r --symbolic -T /media/cjason/Auxiliary aux.link -f
