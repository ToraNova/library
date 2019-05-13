#!/bin/bash

# Simple script to switch off or off the LED of the backlight on the keyboard.
# chia_jason96@live.com

if [ -z $1 ];then
	echo "Please specify on/off with 1 or 0"
	echo "usage ./led.sh 1|0"
	echo "turns on or off the keyboard backlight."
	exit 1
fi
echo "keyboard backlight operation...$1"
echo $1 | sudo tee /sys/class/leds/dell\:\:kbd_backlight/brightness > /dev/null
