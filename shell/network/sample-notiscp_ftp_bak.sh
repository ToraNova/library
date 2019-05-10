#!/bin/bash

#this script will backup the .md files and the .sh files in the notice and script folder
#onto the HNET2108 FTP server. please pass the first argument as IP (192.168.0.109)

serv_ip="175.140.158.43"

echo "\$ noti_bu" | ftp $serv_ip 45000
echo notice backup operation completed...
echo "\$ scp_bu" | ftp $serv_ip 45000
echo script backup operation completed...

#to backup something new, goto ~/.netrc and add a new macro
#then access ftp on console, create the directory FIRST
#then only add the macro here.

exit 0

