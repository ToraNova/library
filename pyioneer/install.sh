#!/bin/bash

# Installs the python package to syslib and records the installed files
# requires root permission
echo "Running python3 setup.py install --record installed.txt..."
echo "Requesting for root permission"
sudo python3 setup.py install --record installed.txt
echo
echo "Installed files:"
cat installed.txt
