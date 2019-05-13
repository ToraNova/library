#!/bin/bash

#xfer.sh - trasnfer file to an authorized host via ssh-keygen authorization
#using scp - read more about authorization at kbase/know/service/ssh-keygen.info
#WARNING, this is only used on local networks

#./xfer-local <username> <host> <additional options like -v>

if [ -z "$1" ];
then
	target_user="rfid_admin"
else
	target_user=$1
fi

if [ -z "$2" ];
then 
	target_host="tingpi"
else
	target_host=$2
fi

sourceDir="$HOME/Public/$target_host-TX"
thdestDir="~/public/$USER-RX"

mkdir -p $sourceDir
echo "Xferring files to $target_host as $target_user"

if [ ! -z "$3" ];
#additional arguments
then
	if [ $3 = "s" ];
	then
	#enable sync mode, deletes thdestDir
	echo "sync mode enabled. this forces deletion of $thdestDir first..."
	timeout 3 ssh $target_user@$target_host.local "rm -r $thdestDir"
	fi
fi

#creating the missing directory if it does not exist timeout at 3 seconds
msg_len=$(timeout 3 ssh $target_user@$target_host.local "mkdir -p $thdestDir" | wc -c)
if [ $msg_len -ne 0 ];
then
	echo "Warning, $target_host requesting for auth. the operation will fail."
	exit 1
else
	scp -r $sourceDir/* $target_user@$target_host.local:$thdestDir
	echo 
	echo "Xfer completed."
	exit 0
fi



