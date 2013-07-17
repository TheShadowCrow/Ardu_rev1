import smbus
import sys 
import RPi.GPIO as GPIO
import zmq
from Libraries.ZMQ_Messages import Ardu_Message
from zmq.eventloop import ioloop, zmqstream
ioloop.install()
import json
import libraries.Sonar_URM37 as Sonar
from libraries.IIC_device import IIC_Device
from drivers.Arduino.Arduino_driver_10 import Arduino_driver_10

# om andere modules als aparte programma's te openen gebruik: import os os.startfile(path)
loaded_modules = []
devices = []
context = zmq.Context()
pub_socket = context.Socket(zmq.PUB)
sub_socket = context.Socket(zmq.SUB)


def Proces_incoming(msg):	
	Message = json.loads(msg)
	if msg.destination == "Core" || msg.destination == "*":
		if msg.type == "Command":
			#execute command
	
		elif msg.type == "State":
			#exec state 
			
		
def Sytem_setup():
	led_on()
	Sonar.setup()
	devices.append = IIC_Device(bus,4, Arduino_driver_10())
		
def System_run():
	while True:
		try:
			distance = Sonar.read()
			
		except: 
			print "Unexpected error:", sys.exc_info()[0]
			devices[0].setInternalCommand("Stop",0)

def led_on():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.OUT)
	GPIO.output(11, GPIO.HIGH)

def Test_run():
		try:
		
		except:
		

if __name__ ==  "__main__": 
	pub_socket.Bind("tcp://*%s" % 5560)
	sub_stream = zmqstream.ZMQStream(sub_socket)
	sub_stream.on_recv(Proces_incoming)
	ioloop.IOLoop.instance().start()
	System_setup()

		#program loop 
		Process(target = System_run).start()