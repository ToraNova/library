#!/usr/bin/python3

# Simple python-gpio for raspberry pi GPIO detection
# uses callback events

import time, datetime, sys
import RPi.GPIO as gpio
import paho.mqtt.client as mqtt
from gpiomq import GPIOMQTT
from utilog import srvlog as log
import configparser #for config parsing

#defining callback behavior
def on_connect(client, userdata, flags, rc):
	client.connected_flag=True
	verbose_log("Connected to broker with rc:{}".format(rc),'i','sys')

def on_disconnect(client,userdata,rc):
	client.connected_flag=False
	verbose_log("Disconnected from broker with rc:"+str(rc),'e','sys')

def pkgprint(str):
	print("{}[MAIN] ".format(datetime.datetime.now()),str)

def verbose_log(str,logtype,logname):
	if(logtype == 'i'):
		log[logname].info(str)
	elif(logtype == 'e'):
		log[logname].error(str)
	elif(logtype == 'w'):
		log[logname].warning(str)
	else:
		verboseprint("Logtype error")
	verboseprint(str)

if __name__ == "__main__":

	# CONFIG PARSING ####################################################
	config = configparser.RawConfigParser()
	config.read("host.conf")
	hostaddr = config.get('conn','hostaddr')
	hostport = int(config.get('conn','port'))
	selfid = config.get('conn','clientid')
	b1pin = int(config.get('detc','b1_pin'))
	b2pin = int(config.get('detc','b2_pin'))
	en1 = True if  config.get('detc','en_1') == "1" else False
	en2 = True if  config.get('detc','en_2') == "1" else False
	verbose = True if config.get('detc','verbose') == "1" else False
	alcd_timer = int(config.get('detc','alcd')) #radar cooldown timer
	#####################################################################
	verboseprint = pkgprint if verbose else lambda *a, **k: None
	
	pinlist = [b1pin,b2pin]

	#creates the mqtt client and attaches the callbacks
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_disconnect = on_disconnect
	client.zid = selfid
	client.en1 = en1
	client.en2 = en2
	client.connected_flag = False

	# MQTT SETUP ########################################################
	verbose_log("System init, waiting for primary server...",'i','sys')
	verbose_log("Attempting to connect to host {} on port {}".format(hostaddr,hostport),'i','sys')
	while True:
	# keep trying until end of time
		try:
			client.connect(hostaddr,hostport,30) #CONNECT TO MQTT BROKER
			break
		except Exception as e:
			verbose_log("MQTT broker conn err: "+str(e),'e','sys')
			time.sleep(3)

	client.publish('zfence/wire',"{},{}".format(selfid,0))
	verbose_log("Starting loop...",'i','sys')
	ctime = datetime.datetime.now()
	rtime = datetime.datetime.now()

	try:
		m = GPIOMQTT(gpio, pinlist, client, verbose)
		while True:
			try:
				client.loop()
				cdelt =  datetime.datetime.now() - ctime
				rdelt = datetime.datetime.now() - rtime
				cdiff = divmod(cdelt.days * 86400 + cdelt.seconds, 60)
				rdiff = divmod(rdelt.days * 86400 + rdelt.seconds, 60)
				if(cdiff[1] > 30):
					#timer expired
					ctime = datetime.datetime.now() #reset timer
					client.publish('zfence/wire','{},{}'.format(selfid,0))
				if(rdiff[1] > 3 and not client.connected_flag):
					rtime = datetime.datetime.now()
					try:
						client.reconnect()
					except Exception as e:
						verbose_log("MQTT broker reconn err: "+str(e),'e','sys')
			except KeyboardInterrupt:
				verbose_log("Quitting loop...",'w','sys')
				raise KeyboardInterrupt #elevate it to the outer try catch block
	except KeyboardInterrupt:
		print("Loop terminated")
	except Exception as e:
		#catch all
		print("Error has occurred :",str(e))
	finally:
		gpio.cleanup()
	
	
