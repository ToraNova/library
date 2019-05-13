#!/bin/bash

#cadd - complete user add
#this script will add the user and also create a home directory for it.

#check if there is only exactly one argument passed
if [ "$#" = 0 ] || [ "$#" -ge 2 ]
#the second condition is only evaluated only if the first condition returns a 0 (true)
then
	echo "Usage: cadd.sh [user]"
	echo "example : ./cadd.sh newuser"
	exit 1
fi

sudo useradd $1
echo $1 is added as a user to the system...

sudo mkhomedir_helper $1
echo /home/$1 created...

exit 0
