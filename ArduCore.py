import smbus
import RPi.GPIO as GPIO
import libraries.Sonar_URM37 as Sonar
import libraries.IIC_device
import drivers.Arduino.Arduino_driver_10
import * from Modules.Core.Handlers 

# om andere modules als aparte programma's te openen gebruik: import os os.startfile(path)
	loaded_modules = []
def Sytem_setup():
	led_on()
	Sonar.setup()
	MotorDriver = IIC_device(4, Arduino_driver_10())
	loaded_modules.append(Navigation_handler("evade",True, MotorDriver))
	
def System_run():
	try:
		distance = Sonar.read()
		nav.Run_time(distance)
		for m in loaded_modules:
			if m.running == True:
				m.Run()
	except: 
		print "Unexpected error:", sys.exc_info()[0]
		MotorDriver.setInternalCommand("Stop",0)

def led_on():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.OUT)
	GPIO.output(11, GPIO.HIGH)
	

if __name__ ==  "__main__": 
	System_setup()

    while true: #program loop 
		System_run()