#!/bin/bash
# setdns - a script to set the dns from commandline easily
# usage: setdns <nameservers...> <interface>
# ToraNova 2019
# chia_jason96@live.com

# if [[ $EUID > 0 ]]; then
#	echo "Please run as root."
#	exit 1
#fi

if [ $# -lt 2 ]; then
	echo "Please specify at least ONE nameserver and ONLY one interface"
	echo "setdns <nameservers...> <interface>"
	exit 1
fi

addstr=""

let ctr=1
for var in "$@"
do
	if [ $ctr -ge $# ]; then
		iface=$var
		break
	fi

	# ipv4 validity check
	if [[ $var =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
		echo "adding $var as nameserver to /etc/resolv.conf via resolvconf"
		addstr="${addstr}nameserver $var\n"
	else
		echo "$var is not a valid ipv4 address, skipping..."
	fi

	let ctr=$ctr+1
done

if [[ $addstr =~ ^nameserver.* ]]; then
	echo "Setting new nameservers on $iface..."
	printf "$addstr" | sudo resolvconf -a $iface
	echo
	echo
	echo "cat /etc/resolv.conf"
	cat /etc/resolv.conf
	exit 0
fi

echo "No valid ipv4 for nameservers, aborting..."
exit 1

