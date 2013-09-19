import smbus
import sys 
import RPi.GPIO as GPIO
import zmq
from zmq.eventloop import ioloop, zmqstream
ioloop.install()
import json
# import libraries.Sonar_URM37 as Sonar
# from libraries.IIC_device import IIC_Device
# from drivers.Arduino.Arduino_driver_10 import Arduino_driver_10
from Libraries.ZMQ_Messages import *
# From Libraries.speech import Speech  
#om andere modules als aparte programma's te openen gebruik: import os os.startfile(path)
loaded_modules = []
# devices = []




def Proces_Commands(msg):	
	try:
		Message = Message_Decoder.decode(json.loads(msg))
		if Message.destination == "Core" || msg.destination == "*":
		
	except e:
		print e 
					

def Proces_Module(msg):
	try:
		found = False
		Message = Message_Decoder.decode(json.loads(msg))
		if Message.destination == "Core" ||  Message.destination == "*":
			if Message.name == "Core" && Message.origin != "Core":
				SetMode(Message.mode, message.args)
			for m in loaded_modules:
				if m.Update(Message):
					found = True
					if Message.status == "stopped":
						#remove loaded module
			if !found:
				loaded_modules.append(Message)
	except e:
		print e


def SetMode(mode, args):
	if mode == "default":
	
	elif mode == "test":
		#shutdown drivers 
	
def Sytem_setup():
	loaded_modules.append(Loaded_Module("Core", 0, "Running"))
	# Sonar.setup()
	# devices.append = IIC_Device(bus,4, Arduino_driver_10())
		
# def System_run():
	# while True:
		# try:
			# distance = Sonar.read()
			
		# except: 
			# print "Unexpected error:", sys.exc_info()[0]
			# devices[0].setInternalCommand("Stop",0)

# def Test_run():
		# try:
		
		# except:
context = zmq.Context()
pub_socket = context.Socket(zmq.PUB)
commands_sub = context.Socket(zmq.SUB)
commands_sub.connect("tcp://*:5559")
commands_sub.socketopt(zmq.SUBSCRIBER, "Commands")
module_info_sub = context.Socket(zmq.SUB)
module_info_sub.connect("tcp://*:5559")
module_info_sub.socketopt(zmq.SUBSCRIBER, "Module Info")		

if __name__ ==  "__main__": 
	pub_socket.Bind("tcp://*%s" % 5560)
	commands_stream = zmqstream.ZMQStream(commands_sub)
	commands_stream.on_recv(Proces_Commands)
	
	module_info_stream = zmqstream.ZMQStream(module_info_sub)
	module_info_stream.on_recv(Proces_Module)
	ioloop.IOLoop.instance().start()
	System_setup()

		# program loop 
		# Process(target = System_run).start()
