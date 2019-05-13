#!/bin/bash

# uninstalls the package by removing the installed files
# this script will automatically asks for root permission

echo "Removing the following files"
cat installed.txt

echo "Proceed ? y/n"
read yesno
if [ $yesno = "y" ] || [ $yesno = "yes" ]
then
echo "Removing pyioneer package from system library"
sudo xargs rm -f < installed.txt
else
echo "Halted. thanks for your continued usage"
fi
