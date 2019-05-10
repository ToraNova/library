#!/bin/bash

#ppc -- piped process count
#this script will return the number of process by a designated user

#----Experimental pipe read script------

IFS= read var << EOF
echo $var
EOF

