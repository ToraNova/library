#!/bin/bash

#<TODO>

if [ $# -ne 1 ];
then
	echo "Usage: compression.sh <filename>"
	echo "example: ./compression.sh input.avi"
	echo "compress the avi file 'input.avi' and returns 'cmprd_input.avi'"
	echo "on the same directory; using -crf 24"
	exit 1
fi

ffmpeg -i $1 -vf scale=1280:-1 -c:v libx264 -preset veryslow -crf 24 cmprd_$1

echo "compression completed."

exit 0
