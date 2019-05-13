#!/bin/bash

#list the users registered in this system

cut -d ":" -f 1 /etc/passwd
#selects a portion from the file /etc/passwd
#using the delimiter option, anything after the `:` is removed
#-f 1 for selecting the first field, that is the names.
#using -f 2 will cause it to print lots of x
#refer the file for more indepth understanding
