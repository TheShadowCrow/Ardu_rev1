class Navigate_handler:
	def __init__(self, mode, motordevice):
		self.minimal = 10
		self.motordriver = motordevice
		if(mode == "follow"):
			self.SetMode("follow")
		elif(mode == "evade"):
			self.SetMode("evade")
		elif(mode == "evaluate"):
			self.SetMode("evaluate")
	
	def SetMode(mode):
			self.mode = mode
		
	def Run_time(distance):
		if(distance <= self.minimal) && if(mode != "follow"): 
			motordriver.SetInternalCommand("Stop", 0)			
				if(self.mode == "evade"):
				motordriver.SetInternalCommand("Right", 0)		
				elif(self.mode == "evaluate"):
					#load evaluation module. 
		elif(distance <= self.minimal) && if(self.mode == "follow"): 
			motordriver.SetInternalCommand("Foreward", 0)