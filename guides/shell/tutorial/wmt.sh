#!/bin/bash

#mount windows installation /dev/sda4
echo mounting windows installation
#ubuntu default mounts will create a folder OS_Install <or drive name>
#on the dir /media/yzeison/
sudo mkdir /media/yzeison/OS_Install
sudo mount /dev/sda4 /media/yzeison/OS_Install

