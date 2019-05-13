#!/bin/bash

#check for kernel ip forwarding
#this is useful if we wanna conduct MITM or spoof attacks

echo Kernel IP_Forward?
cat /proc/sys/net/ipv4/ip_forward
