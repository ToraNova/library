#!/bin/bash

#mount windows installation /dev/sda4
echo mouting hdd installations...
#ubuntu default mounts will create a folder OS_Install <or drive name>
#on the dir /media/yzeison/
#the -p option will only create the directory if it is not there.
sudo mkdir -p /media/cjason/Auxiliary
sudo mkdir -p /media/cjason/Persistence
sudo mkdir -p /media/cjason/Windows10
sudo mount /dev/sda3 /home/cjason/misc/mpoint
sudo mount /dev/sda2 /media/cjason/Auxiliary
sudo mount /dev/sda1 /media/cjason/Persistence
sudo mount /dev/sdb4 /media/cjason/Windows10


