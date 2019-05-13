#!/bin/bash
#this script sets a desktop wallpaper

#FOR SUCCESSFUL CRONRUN - THIS MUST BE INCLUDED
PID=$(pgrep gnome-session)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

#location of wallpaper relative to user's home directory
local_wallpaper_dir="$HOME/Pictures/desktop"

#enumerate number of wallpapers (only jpg or jpeg files)
num_of_wp=$( find $local_wallpaper_dir -regextype posix-egrep -regex ".*\.(jpg|jpeg)$" | wc -l )

#random a wallpaper
choose=$(rand --max $num_of_wp)

#while [ $choose = '0' ];
#do
#	choose=$(rand --max $num_of_wp)
#done

if [ $choose = '0' ];
then
	choose=$num_of_wp
fi
target_wallpaper_file=$( ls $local_wallpaper_dir | head -n $choose  | tail -n 1)
target_wallpaper_loc="$local_wallpaper_dir/$target_wallpaper_file"

#specifically for cron logging
echo "$0 --- $(date +%F[%T]) --- applying gsettings onto $target_wallpaper_loc --- $choose"
gsettings set org.gnome.desktop.background picture-uri "file://$target_wallpaper_loc"

#automation using crontab (do not use any environment variables if using crontab)

#%crontab -e

