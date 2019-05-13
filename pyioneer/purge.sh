#!/bin/bash

#TODO: edit this for different projects
purgeTar="pyioneer"

#delete all possible site packages of the name
count=$(python3 -c "import site; print(len(site.getsitepackages()))")

#loop through the indexes
while [ $count -gt 0 ]
do
	count=$(( $count - 1 ))
	purline=$(python3 -c "import site; print(site.getsitepackages()[$count])")/$purgeTar
	echo "Perform purge on $purline ? (rm -rf $purline)"

	read yesno
	if [ $yesno = "y" ] || [ $yesno = "yes" ]
	then
		sudo rm -rf $purline
	else
		echo "Halted. thanks for your continued usage"
		exit 1;
	fi
done
echo "Purge complete."
exit 0;

