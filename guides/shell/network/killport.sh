#!/bin/bash

tPort=$1

pidN=$(netstat -ltp | grep $tPort | cut -c81- | cut -d '/' -f 1)

echo $pidN

#use kill

