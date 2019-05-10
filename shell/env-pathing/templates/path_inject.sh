#!/bin/bash

#This script injects a directory onto the PATH variable.
#this script specifically inject the dir onto .profile
#under the tag
#<<<PATH_EDIT_INSERTION_TAG>>>

inject_tag_head="#<<<PATH_EDIT_INSERTION_TAG_HEAD>>>"
inject_tag_trail="#<<<PATH_EDIT_INSERTION_TAG_TRAIL>>>"

#specify the file to inject. please include the above tags to specify WHERE to inject
inject_target="$HOME/.profile"

#!WARNING, inject source is relative to $HOME as root!
#example injection on $HOME/bin
inject_src="bin"

inject_line="PATH=\"\$PATH:\$HOME/$inject_src\""

#verbosity
echo "Line to be injected onto $inject_target : $inject_line"

#get total custom pathings
let stn=$(cat $inject_target | grep "#<<<PATH_EDIT_INSERTION_TAG_HEAD>>>" -n | cut -d : -f 1)
let edn=$(cat $inject_target | grep "#<<<PATH_EDIT_INSERTION_TAG_TRAIL>>>" -n | cut -d : -f 1)

let tot="$edn-$stn -1"
echo "Total of $tot custom path edits made."

count=$(cat $inject_target | grep $inject_tag_head -A $tot | grep $inject_line | wc -l)

if [[ count -eq 0 ]];
then	
	echo "No previous entry of such edits detected. injecting line..."
	#core of the script. insert INJECT_LINE after INJECT_TAG_HEAD	
	sed -i -e "s@$inject_tag_head@$inject_tag_head\n$inject_line@" $inject_target
	let tot="$tot+1"
	cat $inject_target | grep $inject_tag_head -A $tot | grep $inject_tag_head --invert-match
else
	echo "The line has already been injected. Terminating without action."
fi

exit 0






