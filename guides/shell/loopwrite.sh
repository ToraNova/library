#!/bin/bash

if [ -z $1 ];
then
	echo "sample use ./loopwrite a"
	exit
fi

n=0
while true
do
	echo $1$n | tee out/$1$n
	sleep 1
	n=$((n+1))	
done
