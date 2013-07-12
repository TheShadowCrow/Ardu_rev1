#core test 
from Libraries.IIC_device import IIC_Device
import smbus 
from drivers.Arduino.Arduino_driver_10 import Arduino_driver_10
import sys, getopt
import time

bus = smbus.SMBus(1)


if __name__ == "__main__":
	arduino = IIC_Device(bus,0x04,Arduino_driver_10())
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
			#bus.write_byte(0x04,ord('b'))
			#bus.write_byte(0x04,value)
		elif command == "tilt":
			arduino.setInternalCommand("TiltHead", value)
			#c = [ord('n'),value]
			#bus.write_i2c_block_data(0x04, 0, c)
			#bus.write_byte(0x04,ord('n'))
			#bus.write_byte(0x04,value) 
		else:
			print "Sorry but that command has not been reconized"

		
