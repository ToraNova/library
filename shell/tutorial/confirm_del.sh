#!/bin/bash

#prompt for action script snippet

prompt_message="PERFORM ACTION ?"		#prompt message
prompt_action="performing action..." 		#show this when user input yes or y
prompt_inaction="not performing action..." 	#show this when user input otherwise

echo $prompt_message #prompt for removal
read yesno
if [ $yesno = "y" ] || [ $yesno = "yes" ]
then
echo $prompt_action
#ACTION GOES HERE
else
echo $prompt_inaction
#INACTION GOES HERE (OPTIONAL)
fi

