#!/usr/bin/python3

#This code is used more for listening rather than sending.
#Checkout pub_mqtt.py for the sending part

#paho-mqtt import
import paho.mqtt.client as mqtt

#defining callback behavior
def on_connect(client, userdata, flags, rc):
    print("Connected with result code",rc)
    client.subscribe(userdata)
    print("Subscribed to",userdata)

#defining callback behavior upon message receive
def on_message(client, userdata, msg):
    print("Msg from topic",msg.topic," : ",msg.payload)

#actual script usage code
if __name__ == "__main__":

    #user interface to obtain some important params
    print("Enter mqtt broker address",end=":")
    hostaddr = input()
    print("Enter topic to connect to",end=":")
    target_topic = input()

    default_port = 1883
    conn_timeout = 60

    #creates the mqtt client and attaches the callbacks
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    #sets a userdata
    client.user_data_set(target_topic)
    client.connect(hostaddr,default_port,conn_timeout)

    client.loop_forever() #blocking
    #client.loop_start() #non blocking
    #client.loop() #must be called multiple times to process data (polling)
