#!/bin/bash

#unmount windows installation /dev/sda4
echo unmounting hdd installations
sudo umount /dev/sda3
sudo umount /dev/sda2
sudo umount /dev/sda1
sudo umount /dev/sdb4
sudo rm -d /media/cjason/Auxiliary -f
sudo rm -d /media/cjason/Persistence -f
sudo rm -d /media/cjason/Windows10 -f

