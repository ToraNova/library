#!/usr/bin/python3

#allows HTTP requests
import requests
#basic authentication from the same module
from requests.auth import HTTPBasicAuth

#this module disable printing of keystrokes
import getpass 

#target domain setup
host_domain_name = "mmls.mmu.edu.my"
https_url_format = "https://{}:{}"
https_req_portnm = 443

#http settings (not used)
http_url_format = "http://{}:{}"
http_req_portnm = 80

#filling in credentials
username = "1161300548"
print("Requesting with",username)
#print("Please enter password: ",end='') #deprecated
#passw = input() 
passw = getpass.getpass("Please enter password: ")

#the authentication object to be created
https_auth_obj = HTTPBasicAuth("1161300548",passw)

#sending the request
reply = requests.get( https_url_format.format(host_domain_name,request_port_num),auth = https_auth_obj)

#printing the replies
print(reply.status_code)
print(reply.text)
#others
#reply.json
#reply.raw.read()
