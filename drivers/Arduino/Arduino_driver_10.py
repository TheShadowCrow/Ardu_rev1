# This is the version 1.0  of the arduino driver.
# it supports of driving the directions of the two motors and turning the 
# pan and tilt servo's for the head.
from Libraries.IIC_Command import IIC_Command

class Arduino_driver_10:
	def __init__(self):	
		self.out = [] #{"dir_left": ['l',False], "dir_right": ['r','false'], "h_turn": ['b', 45], "h_tilt": ['n', 45]}
		self.out.append(IIC_Command("turn_left", 'l',False))
		self.out.append(IIC_Command("turn_right", 'r',False))
		self.out.append(IIC_Command("foreward", 'f',False)) 
		self.out.append(IIC_Command("backward", 'b',False))
		self.out.append(IIC_Command("h_turn", 'h',45))
		self.out.append(IIC_Command("h_tilt", 'n',45))
		self.out.append(IIC_Command("stop_wheel", 's', True))
		self.state = ["Stopped", 45, 45] #motorstate h_turn, h_titl 
## Start section Internal driver command handling			
	def Stop(self):
		#self.out[6].data = True
		self.out[6].send = True
		self.state[0] = "Stopped"
		
	def Foreward(self):
		#self.out[2].data = True
		self.out[2].send = True
		self.state[0] = "Foreward"
		
	def TurnLeft(self):
		#self.out[0].data = False
		self.out[0].send = True
		self.state[0] = "Turning left"
	
	def TurnRight(self):
		#self.out[1].data = True
		self.out[1].send = True
		self.state[0] = "Turning right"
		
	def Backward(self):
		#self.out[3].data = True
		self.out[3].send = True
		self.state[0] = "Backward"
		
	def Head_tilt(self, angle):
		self.out[2].data = angle
		self.out[2].send = True
		self.state[1] = "angle"
		
	def Head_turn(self, angle):
		self.out[3].data = angle
		self.out[3].send = True
		self.state[2] = "angle"

## End section internam command handling.

	def setCommand(self, command, data):
		if command == "Stop":
			self.Stop()
		elif command == "Foreward":
			self.Foreward()
		elif command == "Backward":
			self.Backward()
		elif command == "Left":
			self.TurnLeft()
		elif command == "Right":
			self.TurnRight()
		elif command == "TurnHead":
			self.Head_turn(data)
		elif command == "TiltHead":
			self.Head_tilt(data)
		
	def setMainData(data):
		self.setInternalCommand(data, 0)
	
