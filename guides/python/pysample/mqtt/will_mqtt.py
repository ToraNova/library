#!/usr/bin/python3

#This code is used more to test the Will functionality

#paho-mqtt import
import paho.mqtt.client as mqtt

#defining callback behavior
def on_connect(client, userdata, flags, rc):
    client.publish( "test/will", "{\"status\":\"good\"}")
    client.subscribe( "test/msg" )
    print("Client up...")

#defining callback behavior upon message receive
def on_message(client, userdata, msg):
    print("Msg from topic",msg.topic," : ",msg.payload)

#actual script usage code
if __name__ == "__main__":

    default_addr = "localhost"
    default_port = 1883
    conn_timeout = 60

    #creates the mqtt client and attaches the callbacks
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.will_set( "test/will", payload="{\"status\":\"down\"}", qos=0, retain=True)

    try:
        #sets a userdata
        client.connect( default_addr, default_port, conn_timeout)
        client.loop_forever() #blocking
        #client.loop_start() #non blocking
        #client.loop() #must be called multiple times to process data (polling)
    except KeyboardInterrupt:
        print("Exit")
    except Exception as e:
        print(e)
