#!/bin/bash

#argument tester

if [ "$#" = 0 ]
then
	echo "Usage: arg1.sh [args]..."
	echo "example : ./arg1.sh hi hello howdy"
	exit 0
fi

echo "$# arguments given to this script, they are : $*"
total=$#
count=1
while [ "$count" -le "$total" ]
#while the amount of arguments is greater than 0
do
	echo "argument $count : $1"
	shift
	count=`expr $count + 1`
done
exit 0
