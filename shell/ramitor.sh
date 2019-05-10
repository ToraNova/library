#!/bin/bash

#simple bash script to watch the ram usage.
#please create the profile 'scripted_profile01' from the preferences
#This is ran using gnome-terminal
#requires wmctrl to be installed
echo "$(date) :-- Starting ramitor.sh" >> /home/cjason/cron/logs/run.log
gnome-terminal --geometry=79x6+1800+1000 --hide-menubar --title="RAMITOR" --window-with-profile=scripted_profile01 -- watch -n 3 free -m -h
gnome-terminal --geometry=79x4+1800+835 --hide-menubar --title="CPUITOR" --window-with-profile=scripted_profile01 -- watch -n 3 uptime
wmctrl -r "RAMITOR" -b add,above
wmctrl -r "CPUITOR" -b add,above
