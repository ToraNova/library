#!/bin/bash

#wait_network is a blocking script that waits for network connectivity

# IP addr input as arg 1
if [ -z $1 ];
then
	echo "sample use ./waitnet 192.168.0.1"
	echo "wait until a ping to 192.168.0.1 returns true"
	exit
fi

# interval to wait before trying again
WAIT_DUR=3

while true
do
    if ping -c 1 -W 5 $1 1>/dev/null 2>&1 
    then
        echo "Connected!"
	exit
    fi
    sleep $WAIT_DUR
done
