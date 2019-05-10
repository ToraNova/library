#!/bin/bash

#This script snipes a directory from the PATH variable.
#this script specifically snipe the dir from .profile
#under the tag
#<<<PATH_EDIT_INSERTION_TAG>>>
#note that both snipe and insertion uses the same tag.

#script name
this_script_name="abs_psnipe.sh"

if [ $# -ne 1 ];
then
	echo "Usage: $this_script_name [PATH]"
	echo "example: $this_script_name $HOME/bin"
	echo "removes $HOME/bin from the environment PATH for $USER"
	exit 1
fi

snipe_tag_head="#<<<PATH_EDIT_INSERTION_TAG_HEAD>>>"
snipe_tag_trail="#<<<PATH_EDIT_INSERTION_TAG_TRAIL>>>"

#specify the file to snipe. please include the above tags to specify WHERE to snipe
snipe_target="$HOME/.profile"

#!WARNING, this uses absolute pathing
#example snipeion on $HOME/bin
snipe_src=$1

snipe_line="PATH=\"\$PATH:$snipe_src\""

#verbosity
echo "Line to be sniped from $snipe_target : $snipe_line"

#get total custom pathings
let stn=$(cat $snipe_target | grep "#<<<PATH_EDIT_INSERTION_TAG_HEAD>>>" -n | cut -d : -f 1)
let edn=$(cat $snipe_target | grep "#<<<PATH_EDIT_INSERTION_TAG_TRAIL>>>" -n | cut -d : -f 1)

let tot="$edn-$stn -1"
echo "Total of $tot custom path edits made."

count=$(cat $snipe_target | grep $snipe_tag_head -A $tot | grep $snipe_line | wc -l)

if [[ count -gt 0 ]];
then	
	echo "Target spotted. We may proceed to pull the trigger."
	#core of the script. snipe snipe_line after snipe_TAG_HEAD	
	sed -i "\@$snipe_line@d" $snipe_target
	let tot="$tot-1"
	echo 
	echo "Current custom pathing edits:"
	cat $snipe_target | grep $snipe_tag_head -A $tot | grep $snipe_tag_head --invert-match
else
	echo "No such line exists to be sniped. Terminating without action"
fi

exit 0






