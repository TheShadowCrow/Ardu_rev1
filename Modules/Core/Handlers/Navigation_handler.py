class Navigate_handler:
	def __init__(self, mode, running, motordevice, sonar, debug=False):
		self.minimal = 10
		self.motordriver = motordevice
		self.running = running
		self.name = "core_navigation_handler"
		self.debug = debug
		if(mode == "follow"):
			self.SetMode("follow")
		elif(mode == "evade"):
			self.SetMode("evade")
		elif(mode == "evaluate"):
			self.SetMode("evaluate")
	
	def SetMode(self, mode):
			self.mode = mode
		
	def Run(self):
		if(self.sonar.read() <= self.minimal) && if(mode != "follow"): 
			self.motordriver.setInternalCommand("Stop", 0)			
				if(self.mode == "evade"):
					self.motordriver.setInternalCommand("Right", 0)
					self.motordriver.SendData()
				elif(self.mode == "evaluate"):
					#load evaluation module. 
		elif(self.sonar.read() <= self.minimal) && if(self.mode == "follow"): 
			motordriver.setInternalCommand("Foreward", 0)
	
		printDebug()

	def printDebug(self):
		if self.debug:
			print "+++++++++++++++++" + self.name + "DEBUGGER +++++++++++++++++++++"
			print "Mode:" + self.mode
			print "Distance": + self.sonar.read()
			print "engine state:" + self.motordriver.getState()[0] 
			print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"