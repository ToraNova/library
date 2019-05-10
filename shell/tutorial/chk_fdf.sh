#!/bin/bash

#chk_fdf check file directory differences
#check the differences between the dir x and dir y with exclusion on -x
# "*.*~" implies foo.bar~ where foo and bar can be any string. * is a wildcard for string

#naive, assumes user inputs both arguments correctly
dir1=$1
dir2=$2

diff -rq $dir1 $dir2 -x "*.*~"


