#!/usr/bin/python3

# Test image posting onto a strapi server (using one of an API endpoint)

import requests
import datetime

huser = {'identifier':'Hostuser','password': '4dns9af8XR9mPm2'}

# obtain a token by logging in
r = requests.post("http://localhost:1337/auth/local", data=huser)
rj = r.json()
if(r.status_code == 200):
    jwt = rj['jwt']
    ntime = datetime.datetime.now().isoformat()
    a =  ('Bearer %s' % jwt)
    print('jwt :',jwt)
    print('time:',ntime)
else:
    print("Unable to log in",r.status_code, r.reason)
    exit(1)

r = requests.post("http://localhost:1337/alerts",
        json={
            'Reason': None,
            'OriginBranch':1,
            'fence_segment':1,
            'alert_model':1,
            'Details':{ 'info':'some info' }
            },
        headers={
            'Authorization': a
            }
        )
if(r.status_code == 200):
    aid = r.json()['id']
    print(r.json())
else:
    print(r.status_code, r.reason)

r = requests.post("http://localhost:1337/upload",
        data={
            'refId' : aid,
            'ref' : 'alert',
            'field' : 'Attachment'
            },
        files={'files': ('test.jpg', open('test.jpg','rb'),'image/jpg')
            },
        headers={'Authorization': a})
if(r.status_code == 200):
    fid = r.json()[0]['id']
    print(r.json())
else:
    print("Unable to upload",r.status_code, r.reason)
    exit(1)

