#!/usr/bin/python3
# imports
import paho.mqtt.client as mqtt
import time

MQTT_PTOPIC="cmd/1"
MQTT_STOPIC="rep/1"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	client.subscribe( MQTT_STOPIC )
	print("Connected with result code "+str(rc))

if __name__ == "__main__":

	client = mqtt.Client()
	client.on_connect = on_connect
	client.connect("127.0.0.1", 1883, 60)
	client.loop_start()

	time.sleep(1) #wait for connection
	try:
		while True:
			print("Test string: ",end='')
			sendstr = input()
			print("Sending ",sendstr)
			client.publish( MQTT_PTOPIC , sendstr)
	except KeyboardInterrupt:
		print("Exit.")
		exit(0)
