#!/bin/bash

# iron.sh - check if a process exist, run it if not (minimal version of cronrun.sh)
# This script will be run every 5 minutes. it is the final bastion to ensure both main.py are running

TAR_DIR='/home/pi/zfence'
TAR_SCP='main.py'

cd $TAR_DIR

if ps ax | grep -v grep | grep $TAR_SCP > /dev/null
then
	exit 0
else
	mkdir -p debug
	./$TAR_SCP > $TAR_DIR/debug/$(date +[%m-%d--%T]).debug 2>&1
fi
