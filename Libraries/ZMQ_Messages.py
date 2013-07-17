class Ardu_Message:
	def __init__(self, destination, origin,data):
		self.destination = destination
		self.origin = origin
		self.data = data
		self.type = "Message"
	
	def Command(self, command, data):
		self.command = command
		self.data = data
		self.type = "Command"
		
	def State(self, state, type="change"):
		self.state = state
		self.stateType = type 
	
	