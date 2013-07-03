# This is the version 1.0  of the arduino driver.
# it supports of driving the directions of the two motors and turning the 
# pan and tilt servo's for the head.

class Arduino_driver_10:
	def __init__(self):	
		self._out{"dir_left": ['l',False], "dir_right": ['r','false'], "h_turn": ['b', 45], "h_tilt": ['n', 45]}

 
## Start section Internal driver command handling			
	def Stop():
	self._out["dir_left"][1] = 0
	self._out["dir_right"][1] = 0
		
	def Foreward():
        self._out["dir_left"][1] = True
        self._out["dir_right"][1] = True
		
	def TurnLeft():
        self._out["dir_left"][1] = False
        self._out["dir_right"][1] = True
	
	def TurnRight():
        self._out["dir_left"][1] = True
        self._out["dir_right"][1] = False 
		
	def Backward():
        self._out["dir_left"][1] = False
        self._out["dir_right"][1] = False 
	
	def Head_tilt(angle):
		self._out["h_tilt"][1] = angle
	
	def Head_turn(angle):
		self._out["h_turn"][1] = angle
## End section internam command handling.

	def setCommand(command, data):
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
	