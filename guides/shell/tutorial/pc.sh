#!/bin/bash

#pc -- process count
#this script will return the number of process by a designated user

#check if there is only exactly one argument passed
if [ "$#" = 0 ] || [ "$#" -ge 2 ]
#the second condition is only evaluated only if the first condition returns a 0 (true)
then
	echo "Usage: pc.sh [user]"
	echo "example : ./pc.sh root"
	exit 1
fi

#check if the user is logged in
logbool=$(who | grep -Fw $1 | wc -l)
#the -Fx matches a fixed string with exact match
if [ "$logbool" = 0 ]
then
	echo "user $1 is not logged in onto this system !"
	exit 1
fi

#prints output
so=$(ps -ef | grep -v grep | grep -v ps | grep -F $1 | wc -l)
echo "user $1 is running $so processes"
exit 0

