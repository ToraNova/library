#!/usr/bin/python3

#This code is used more for publishing
#Checkout sub_mqtt.py for the receiving

#paho-mqtt import
import paho.mqtt.client as mqtt

#util import
import time

#defining callback behavior
def on_connect(client, userdata, flags, rc):
    print("Connected with result code",rc)

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

	#sets a userdata
	client.connect(hostaddr,default_port,conn_timeout)

	client.loop_start()
	time.sleep(1)
	while True:
		print("Enter String to send to",target_topic,end=":")
		sendstr = input()
		client.publish(target_topic,sendstr)
	#client.loop_start() #non blocking
	#client.loop() #must be called multiple times to process data (polling)
