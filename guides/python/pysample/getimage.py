#!/usr/bin/python3

# obtain an image from a url with python requests
import requests
from requests.auth import HTTPBasicAuth

# authentication
bauth = HTTPBasicAuth("admin","Admin123")

try:
    # obtain resposne
    #response = requests.get( "http://localhost:1996/static/snap_0.jpg", stream=True, auth=bauth)
    response = requests.get( "http://localhost:1996/static/snap_0.jpg", stream=True)

    # saving to file
    if(response.status_code == 200):
        rawb = response.raw.read()
        with open("download.jpg","wb") as f:
            f.write(rawb)
    print(f"result:{response.status_code}")
except Exception as e:
    print(e)
