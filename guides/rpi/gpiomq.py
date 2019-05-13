#-----------------------------------------------
#	Simple class to handle gpio events
#	and perform MQTT publish based on
#	those events
#	ToraNova 2019 chia_jason96@live.com
#----------------------------------------------
import time
import paho.mqtt.client

class GPIOMQTT:

	#moduename and a pkgprint define
	moduname = "1718_pinlisten_mosquitto"
	def pkgprint(self,*args,**kwargs):
		print("[{}]".format(self.moduname),*args)

	pubtopic = 'zfence/gz'
	def handle_event( self, channel ):
		self.verboseprint("Alert Event",channel) 
		if channel == 17:
			if(self.mclient.en1):
				pubstr = "{},1,0,0_0".format(self.mclient.zid)
				self.mclient.publish( self.pubtopic, pubstr)
				self.verboseprint("Publishing",pubstr) 
		elif channel == 18:
			if(self.mclient.en2):
				pubstr = "{},2,0,0_0".format(self.mclient.zid)
				self.mclient.publish( self.pubtopic, pubstr)
				self.verboseprint("Publishing",pubstr) 

	def __init__(self, gpio, pins, mqttclient, verbose=False):
		gpio.setmode(gpio.BCM) #setup board configuration mode
		self.verboseprint = self.pkgprint if verbose else lambda *a, **k: None
		self.mclient = mqttclient
		for p in pins:
			#gpio.setup(p, gpio.IN, pull_up_down=gpio.PUD_DOWN)
			#gpio.add_event_detect(p, gpio.RISING, callback=self.handle_event, bouncetime=100 )
			gpio.setup(p, gpio.IN, pull_up_down=gpio.PUD_UP)			
			gpio.add_event_detect(p, gpio.FALLING, callback=self.handle_event, bouncetime=100 )
		

