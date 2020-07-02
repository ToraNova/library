#!/usr/bin/python

import requests
from requests.auth import HTTPDigestAuth

auth = HTTPDigestAuth('admin','test123')
res = requests.get('http://localhost:5000/', auth=auth)

print(res.status_code)
print(res.text)
