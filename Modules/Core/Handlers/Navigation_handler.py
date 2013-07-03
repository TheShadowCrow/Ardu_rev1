class Navigate_handler:
	def __init__(self, mode, running, motordevice, sonar):
		self.minimal = 10
		self.motordriver = motordevice
		self.running = running
		self.name = "core_navigation_handler"
		if(mode == "follow"):
			self.SetMode("follow")
		elif(mode == "evade"):
			self.SetMode("evade")
		elif(mode == "evaluate"):
			self.SetMode("evaluate")
	
	def SetMode(mode):
			self.mode = mode
		
	def Run():
		if(self.sonar.read() <= self.minimal) && if(mode != "follow"): 
			self.motordriver.setInternalCommand("Stop", 0)			
				if(self.mode == "evade"):
				self.motordriver.setInternalCommand("Right", 0)		
				elif(self.mode == "evaluate"):
					#load evaluation module. 
		elif(self.sonar.read() <= self.minimal) && if(self.mode == "follow"): 
			motordriver.setInternalCommand("Foreward", 0)
			