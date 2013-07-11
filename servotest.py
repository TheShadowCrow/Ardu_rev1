#core test 
import Libraries.IIC_device
import smbus 
import drivers.Arduino.Arduino_driver_10
import sys, getopt
import time

bus = smbus.SMBus(0)

if __name__ == "__main__":
	arduino = IIC_Device(bus,4,Arduino_driver_10())
	# myopts, args = getopt.getopt(sys.argv[1:], "d:t:")
	# for o, a in myopts:
		# if o = '-d':
			#draai command
		# elif o == '-t':
			#tilt command
		
	while True:
		command = raw_input("Please enter your command")
		try:
			value = int(raw_input("please enter the data"))
		except ValueError: 
			print "Input not reconized as a number"
			value = 90 
	
		if command == "turn":
			arduino.setInternalCommand("TurnHead", value)
		elif command == "tilt":
			arduino.setInternalCommand("TiltHead", value) 
		else:
			print "Sorry but that command has not been reconized"
		time.sleep(5)