#!/bin/bash

#SS purger - Screenshot purger
#chia jason 2018

picdir="$HOME/Pictures"

#alternative idea, accept input arguments to purge pictures x days old

#find files in ~/Pictures that has the starting word "Screenshot from " and is 28 days old
#delete them

ftr=$(find ~/Pictures -regextype posix-egrep -regex "$picdir/Screenshot from .*/.(png|jpg|jpeg)$" -mtime +28 | wc -l)
if [ $ftr -gt 0 ] 
then #mainif

echo "found $ftr files to remove"
echo "The following picture files from $picdir will be purged"
find ~/Pictures -regextype posix-egrep -regex "$picdir/Screenshot from .*/.(png|jpg|jpeg)$" -mtime +28

prompt_message="proceed with purging?"		#prompt message
prompt_action="purging files" 		#show this when user input yes or y
prompt_inaction="they will be spared..." 	#show this when user input otherwise

echo $prompt_message #prompt for removal
read yesno
if [ $yesno = "y" ] || [ $yesno = "yes" ]
then
echo $prompt_action
find ~/Pictures -regextype posix-egrep -regex "$picdir/Screenshot from .*/.(png|jpg|jpeg)$" -mtime +28 -delete
else
echo $prompt_inaction
#INACTION GOES HERE (OPTIONAL)
fi

else #else of mainif

echo "still too early to perform purging..."

fi #end of mainif
exit 0
