#!/usr/bin/python3

#paho-mqtt import
import paho.mqtt.client as mqtt

#util import
import time
import json

#defining callback behavior
def on_connect(client, userdata, flags, rc):
    print("Connected with result code",rc)

#actual script usage code
if __name__ == "__main__":

    #creates the mqtt client and attaches the callbacks
    client = mqtt.Client()
    client.on_connect = on_connect

    #sets a userdata
    client.connect( '127.0.0.1', 1883, 60)

    hostid = 1
    branch = 1

    client.loop_start()
    alert = {
            'id':hostid,
            'branch':branch,
            'type':1,
            'info': {'magnitude':'0xff','details':'blabla' }
            }

    client.publish( f'alert/{hostid}', json.dumps(alert) )
