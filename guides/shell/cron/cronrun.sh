#!/bin/bash

# CRONRUN.SH (originally powerlog.sh), made by cjason (ToraNova : chia_jason96@live.com)

# This script will check if /home/rfid_admin/roboconlab-master/main.py is launched. if not, it will launch it.
# This script is also used for the ZFENCE project
# This will be executed on cron.

TAR_DIR="/home/pi/zfence"
SCP_NAM="main.py"

searchline=$(ps -aux | grep -v grep | grep ./$SCP_NAM)
lineno=$(ps -aux | grep -v grep | grep ./$SCP_NAM | wc -l )
printf "%s -- %s\n" "$searchline" "$lineno"

mkdir -p $TAR_DIR/crons #Create the crons directory if it does not exist

if [ $lineno -eq 1 ];
then
	#main.py already launched.
	printf "%s--%s\t\t\t./$SCP_NAM is already launched.\n" "$(date +%D\ [%T])" "$0" | tee -a $TAR_DIR/crons/$(date +%y-%m-%d).log
	exit 0
else
	printf "%s--%s\t\t\t./$SCP_NAM is not launched. launching...\n" "$(date +%D\ [%T])" "$0" | tee -a $TAR_DIR/crons/$(date +%y-%m-%d).log
	cd $TAR_DIR
	mkdir -p debug # Create the directory if it does not exist
	./$SCP_NAM > $TAR_DIR/debug/$(date +%m-%d--%T).debug 2>&1
	exit 0
fi
